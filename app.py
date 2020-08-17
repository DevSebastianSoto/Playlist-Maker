from utils import download_audio, read_file
from models import Song


if __name__ == "__main__":
    song_list = [Song(s) for s in read_file('song.txt')]
    print([s.to_str() for s in song_list])
