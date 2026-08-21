from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return float(json.loads(result.stdout)["format"]["duration"])


def video_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=duration",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return float(json.loads(result.stdout)["streams"][0]["duration"])


def audio_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "a:0",
            "-show_entries",
            "stream=duration",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return float(json.loads(result.stdout)["streams"][0]["duration"])


def concat_file_line(path: Path) -> str:
    escaped = path.resolve().as_posix().replace("'", "'\\''")
    return f"file '{escaped}'\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="장면 세그먼트에 세 곡의 배경음악을 구간별로 믹싱합니다.")
    parser.add_argument("--segment-dir", required=True, type=Path)
    parser.add_argument("--music", required=True, nargs=3, type=Path, metavar=("THEME1", "THEME2", "THEME3"))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--skip", nargs="*", type=int, default=[])
    parser.add_argument("--breaks", nargs=2, type=int, default=[8, 13], metavar=("THEME2_START", "THEME3_START"))
    parser.add_argument("--music-volume", type=float, default=0.12)
    args = parser.parse_args()

    all_segments = sorted(
        (path for path in args.segment_dir.glob("*.mp4") if path.stem.isdigit()),
        key=lambda path: int(path.stem),
    )
    skip = set(args.skip)
    segments = [path for path in all_segments if int(path.stem) not in skip]
    if not segments:
        raise RuntimeError("사용할 장면 세그먼트가 없습니다.")
    if any(not path.exists() for path in args.music):
        raise FileNotFoundError("배경음악 파일을 찾을 수 없습니다.")

    first_break, second_break = args.breaks
    groups = [
        [path for path in segments if int(path.stem) < first_break],
        [path for path in segments if first_break <= int(path.stem) < second_break],
        [path for path in segments if int(path.stem) >= second_break],
    ]
    if any(not group for group in groups):
        raise RuntimeError("세 음악 구간 중 비어 있는 구간이 있습니다.")

    segment_durations = {path: video_duration(path) for path in segments}
    group_durations = [sum(segment_durations[path] for path in group) for group in groups]
    total_duration = sum(group_durations)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="tts_bgm_", dir=args.output.parent) as temp_name:
        temp_dir = Path(temp_name)
        concat_list = temp_dir / "narration_segments.txt"
        concat_list.write_text("".join(concat_file_line(path) for path in segments), encoding="utf-8")
        narration_video = temp_dir / "narration_without_skipped_scenes.mp4"
        run(
            [
                "ffmpeg",
                "-nostdin",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(concat_list),
                "-c",
                "copy",
                str(narration_video),
            ]
        )

        prepared_voice = temp_dir / "narration.wav"
        run(
            [
                "ffmpeg",
                "-nostdin",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-i",
                str(narration_video),
                "-map",
                "0:a:0",
                "-af",
                "apad",
                "-t",
                f"{total_duration:.3f}",
                "-ar",
                "48000",
                "-ac",
                "2",
                "-c:a",
                "pcm_s16le",
                str(prepared_voice),
            ]
        )

        prepared_music: list[Path] = []
        for index, (music, section_duration) in enumerate(zip(args.music, group_durations), start=1):
            fade_out_start = max(0.0, section_duration - 2.5)
            prepared = temp_dir / f"theme_{index}.wav"
            source_duration = duration(music)
            common_filter = (
                f"atrim=duration={section_duration:.3f},asetpts=PTS-STARTPTS,"
                f"volume={args.music_volume:.4f},afade=t=in:st=0:d=1.5,"
                f"afade=t=out:st={fade_out_start:.3f}:d=2.5"
            )
            prepare_command = ["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-y"]
            if section_duration > source_duration:
                crossfade_duration = 3.0
                if section_duration > source_duration * 2 - crossfade_duration:
                    raise RuntimeError(f"{music.name}은 두 번 연결해도 담당 구간보다 짧습니다.")
                prepare_command.extend(
                    [
                        "-i",
                        str(music),
                        "-i",
                        str(music),
                        "-filter_complex",
                        f"[0:a][1:a]acrossfade=d={crossfade_duration:.1f}:c1=tri:c2=tri,"
                        f"{common_filter}[out]",
                        "-map",
                        "[out]",
                    ]
                )
            else:
                prepare_command.extend(["-i", str(music), "-af", common_filter])
            prepare_command.extend(
                ["-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(prepared)]
            )
            run(prepare_command)
            prepared_music.append(prepared)

        command = [
            "ffmpeg",
            "-nostdin",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(narration_video),
            "-i",
            str(prepared_voice),
        ]
        for music in prepared_music:
            command.extend(["-i", str(music)])

        filters = [
            "[1:a]aresample=48000,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[voice]"
        ]
        music_labels: list[str] = []
        for index in range(3):
            label = f"music{index + 1}"
            filters.append(f"[{index + 2}:a]asetpts=PTS-STARTPTS[{label}]")
            music_labels.append(f"[{label}]")
        filters.append(f"{''.join(music_labels)}concat=n=3:v=0:a=1[bed]")
        filters.append(
            "[bed][voice]sidechaincompress=threshold=0.040:ratio=6:attack=15:release=350:makeup=1[ducked]"
        )
        filters.append(
            "[voice][ducked]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[aout]"
        )

        mixed_draft = temp_dir / "mixed_draft.mp4"
        command.extend(
            [
                "-filter_complex",
                ";".join(filters),
                "-map",
                "0:v:0",
                "-map",
                "[aout]",
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                "-b:a",
                "192k",
                "-ar",
                "48000",
                "-ac",
                "2",
                "-t",
                f"{total_duration:.3f}",
                "-movflags",
                "+faststart",
                str(mixed_draft),
            ]
        )
        run(command)

        mixed_audio_duration = audio_duration(mixed_draft)
        missing_duration = max(0.0, total_duration - mixed_audio_duration)
        if missing_duration <= 0.05:
            shutil.copy2(mixed_draft, args.output)
        else:
            tail_start = max(0.0, group_durations[-1] - missing_duration)
            run(
                [
                    "ffmpeg",
                    "-nostdin",
                    "-hide_banner",
                    "-loglevel",
                    "error",
                    "-y",
                    "-i",
                    str(mixed_draft),
                    "-i",
                    str(prepared_music[-1]),
                    "-filter_complex",
                    f"[0:a]asetpts=PTS-STARTPTS[main];"
                    f"[1:a]atrim=start={tail_start:.3f}:duration={missing_duration:.3f},"
                    f"asetpts=PTS-STARTPTS[tail];"
                    f"[main][tail]concat=n=2:v=0:a=1[aout]",
                    "-map",
                    "0:v:0",
                    "-map",
                    "[aout]",
                    "-c:v",
                    "copy",
                    "-c:a",
                    "aac",
                    "-b:a",
                    "192k",
                    "-ar",
                    "48000",
                    "-ac",
                    "2",
                    "-t",
                    f"{total_duration:.3f}",
                    "-movflags",
                    "+faststart",
                    str(args.output),
                ]
            )

    elapsed = 0.0
    for index, (group, section_duration) in enumerate(zip(groups, group_durations), start=1):
        print(
            f"theme_{index}: segments={group[0].stem}-{group[-1].stem} "
            f"start={elapsed:.3f}s duration={section_duration:.3f}s"
        )
        elapsed += section_duration
    print(f"skipped={','.join(str(index) for index in sorted(skip)) or 'none'}")
    print(f"output={args.output.resolve()}")
    print(f"duration={duration(args.output):.3f}s")


if __name__ == "__main__":
    main()
