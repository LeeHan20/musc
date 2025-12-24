import subprocess
import os

TMP_AUDIO = "tmp/audio.wav"

def download_audio(query):
    os.makedirs("tmp", exist_ok=True)

    if os.path.exists(TMP_AUDIO):
        os.remove(TMP_AUDIO)

    cmd = [
        "yt-dlp",
        f"ytsearch1:{query}",
        "--extract-audio",
        "--audio-format", "wav",
        "-o", TMP_AUDIO
    ]

    subprocess.run(cmd, check=True)
    return TMP_AUDIO
