
import pickle
import os
import sys
import re
from pprint import pprint as pp

from bs4 import BeautifulSoup as BS
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary
import pronouncing
import requests as req

from genius.lyrics import ConvertLyrics as lyrics


class WordUtil:

    def __init__(self):
        '''
        Class to interface with all external writing tools

        Lookup:
            - Definitions: definition(word) -> return definition
            - Synonyms: synonym(word) -> return synonym
            - Antonyms: antonym(word) -> return antonym
            - Lyrics: get_lyrics(artist) -> self.artist_lyrics
        '''
        self.pos_dict = {}
        self.lyrics = lyrics()
        self.get_artist = self.lyrics.convert_artist