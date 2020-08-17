from youtube_search import YoutubeSearch
import pandas as pd
import requests

yt_url = 'https://www.youtube.com'
api_key = "9004f269ad8798f401e6759ad8ca55c3"  # LAST FM KEY


class Song():
    def __init__(self, lst: list):
        self.song = lst[1].strip()
        self.artist = lst[0].strip()

    @property
    def url(self):
        res = YoutubeSearch(f'{self.artist} {self.song}',
                            max_results=10).to_dict()
        for v in res:
            v['views'] = int(v['views'].split(' ')[0].replace(',', ""))
        df = pd.DataFrame.from_dict(res).sort_values(by='views')
        return str(yt_url+df.iloc[-1]['url_suffix'])

    @property
    def genres(self):
        query = f'http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={api_key}&artist={self.artist}&track={self.song}&format=json'
        res = requests.get(query).json()
        try:
            return [
                tag['name'].lower()
                for tag in res['track']['toptags']['tag']

            ]
        except Exception as e:
            return []

    def to_str(self):
        return f"{self.song} by {self.artist}"
