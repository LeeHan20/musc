import subprocess
import os

MODEL = "models/ggml-base.bin"
SRT_OUT = "tmp/audio.srt"

def speech_to_text(audio_path):
    if os.path.exists(SRT_OUT):
        os.remove(SRT_OUT)

    cmd = [
        "./whisper.cpp/build/bin/whisper-cli",
        "-m", MODEL,
        "-f", audio_path,
        "-osrt",
        "-of", "tmp/audio"
    ]

    subprocess.run(cmd, check=True)
    return SRT_OUT
