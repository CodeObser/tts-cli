# Text-to-Speech CLI Tool

Convert text to speech using Google Text-to-Speech API in your terminal!

## Installation

Make sure you have Python3 and pip installed.

```bash
pip install -r requirements.txt

```
## Usage

```bash
python tts.py "Hello, this is a test." -o output.mp4
```


## Options
• `-o, --output <output_file> `: Specify the output file name (default: output.mp3).
• `-l, --lang <language_code>` : Specify the language code (default: en).
• `-s, --slow: Speak slowly.-f, --format <audio_format>` : Specify the output audio format (choices: mp3, wav; default: mp3).
• `-p, --play` : Play audio after conversion.
• `-ls, --list-languages` : List supported languages.
