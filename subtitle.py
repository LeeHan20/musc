import time

def parse_time(t):
    h, m, s = t.replace(',', '.').split(':')
    return int(h)*3600 + int(m)*60 + float(s)

def play_subtitle(srt_path):
    with open(srt_path) as f:
        blocks = f.read().strip().split("\n\n")

    prev = 0.0

    for block in blocks:
        lines = block.splitlines()
        if len(lines) < 3:
            continue

        start, _ = lines[1].split(" --> ")
        text = " ".join(lines[2:])

        cur = parse_time(start)
        time.sleep(max(0, cur - prev))
        print(text, flush=True)

        prev = cur
