import subprocess


def download_audio(video: str):
    try:
        # ignore errors, audio only, quiet output, resume downloads, no warnings, output file, audio
        # format, output progress bars in new line
        subprocess.run([
            'youtube-dl', '-ixc', '--no-warnings', '-o',
            music_path+'%(title)s.%(ext)s', '--audio-format', 'mp3', f'{video}'
        ], check=True)
        return True
    except Exception:
        return False


def read_file(file_path: str) -> list:
    with open(file_path, 'r') as f:
        return [l.split(',') for l in f.read().splitlines()]
