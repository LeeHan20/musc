import sys
from yt import download_audio
from stt import speech_to_text
from subtitle import play_subtitle

def main():
    if len(sys.argv) < 2:
        print("usage: mus \"song title\"")
        return

    query = sys.argv[1]

    audio_path = download_audio(query)
    srt_path = speech_to_text(audio_path)
    play_subtitle(srt_path)

if __name__ == "__main__":
    main()
