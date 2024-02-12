import argparse
from gtts import gTTS
import os
import tempfile
import platform
import subprocess

def text_to_speech(text, output_file, lang='en', slow=False, format='mp3'):
    """
    Convert text to speech using Google Text-to-Speech API.

    Args:
        text (str): The text to convert to speech.
        output_file (str): The output file path for the converted audio.
        lang (str, optional): Language code (default: 'en').
        slow (bool, optional): Speak slowly if True (default: False).
        format (str, optional): Output audio format ('mp3' or 'wav') (default: 'mp3').
    """
    tts = gTTS(text, lang=lang, slow=slow)
    tts.save(output_file)
    print(f"Text converted to speech and saved to {output_file}")

def play_audio(output_file):
    """
    Play the audio file.

    Args:
        output_file (str): The path to the audio file.
    """
    system = platform.system()
    if system == "Windows":
        os.startfile(output_file)
    else:  # Linux
        subprocess.call(["xdg-open", output_file])

def list_languages():
    """List supported languages."""
    print("Supported languages:")
    for lang in gTTS.LANGUAGES:
        print(f"{lang}: {gTTS.LANGUAGES[lang]}")

def main():
    parser = argparse.ArgumentParser(description="Convert text to speech and play audio")
    parser.add_argument("text", type=str, help="Text to convert to speech")
    parser.add_argument("-o", "--output", type=str, default="output.mp3", help="Output file name (default: output.mp3)")
    parser.add_argument("-l", "--lang", type=str, default="en", help="Language code (default: en)")
    parser.add_argument("-s", "--slow", action="store_true", help="Speak slowly")
    parser.add_argument("-f", "--format", type=str, default="mp3", choices=["mp3", "wav"], help="Output audio format (default: mp3)")
    parser.add_argument("-p", "--play", action="store_true", help="Play audio after conversion")
    parser.add_argument("-ls", "--list-languages", action="store_true", help="List supported languages")
    args = parser.parse_args()

    if args.list_languages:
        list_languages()
        return

    temp_dir = tempfile.gettempdir()
    output_file = os.path.join(temp_dir, args.output)

    text_to_speech(args.text, output_file, args.lang, args.slow, args.format)

    if args.play:
        play_audio(output_file)

if __name__ == "__main__":
    main()
