import pdb
import os
from utils import download_audio, read_file
from models import Song


def valid_folder_name(name: str) -> bool:
    with open('blocked_names.txt', 'r') as f:
        if name in f.read().split('\n'):
            return False
        return True


def get_folders(songs: list):
    folders = dict()
    for s in songs:
        for g in s.genres:
            if g not in folders:
                folders[g] = [s]
            else:
                folders[g].append(s)
    return folders


def create_folders(base_path: str, folders: dict):
    for folder in folders.keys():
        if valid_folder_name(folder):
            os.makedirs(os.path.join(base_path, folder), exist_ok=True)


if __name__ == "__main__":
    song_list = [Song(s) for s in read_file('song.txt')]
    folders = get_folders(song_list)
    base_path = os.path.join(os.path.expanduser('~'), 'Music', 'playlists')
    create_folders(base_path, folders)
