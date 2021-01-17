
import sys
import os
import random
from pprint import pprint as pp

if '../' not in sys.path:
    sys.path.append("../")

from genius.lyrics import ConvertLyrics as cl
from util.wordutil import WordUtil as wu
from generate import Generate as gen


class Replace:

    def __init__(self, artist=''):
        self.r = wu()
        self.c = cl()
        self.artists = self.r.artists
        if not artist:
            artist = self.artists[random.randrange(0, len(self.artists))]
        self.artist = artist

    def replace_rap(self):
        '''
        Get topic and words and try to replace all tagged POS in songs
        '''