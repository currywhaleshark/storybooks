param([string]$TextPath, [string]$OutPath)
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$s.SelectVoice('Microsoft Heami Desktop')
$s.Rate = -2
$s.Volume = 100
$text = Get-Content -LiteralPath $TextPath -Raw -Encoding UTF8
$s.SetOutputToWaveFile($OutPath)
$s.Speak($text)
$s.Dispose()