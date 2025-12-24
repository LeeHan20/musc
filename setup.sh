#!/bin/bash
set -e

echo "[*] Installing system dependencies..."

# macOS 기준
if [[ "$OSTYPE" == "darwin"* ]]; then
    brew install ffmpeg yt-dlp
fi

echo "[*] Installing python dependencies..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "[*] Installing whisper.cpp..."
if [ ! -d whisper.cpp ]; then
    git clone https://github.com/ggerganov/whisper.cpp
    cd whisper.cpp
    make
    cd ..
fi

echo "[*] Linking mus command..."
chmod +x mus
sudo ln -sf "$(pwd)/mus" /usr/local/bin/mus

echo "[✓] Setup complete. Try: mus \"노래제목\""
