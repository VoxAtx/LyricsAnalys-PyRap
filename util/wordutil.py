
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
        self.artists = ['Kendrick Lamar', 'Drake', 'Chance The Rapper', 'J. Cole',
                        'Logic', 'Future', 'Chief Keef', 'Eminem', 'Kanye West',
                        'JAY-Z', 'Big Sean', 'Lil Uzi Vert', 'Tyler, The Creator',
                        'Earl Sweatshirt', '2 Chainz', 'G-Eazy', 'ScHoolboy Q',
                        'Young Thug', 'Joey Bada$$', 'PnB Rock', 'Flatbush Zombies',
                        'A$AP Rocky', 'A$AP Ferg', 'Dumbfoundead', 'Tory Lanez',
                        'Waka Flocka Flame', 'Nas', 'A Tribe Called Quest', 'Vic Mensa',
                        '$UICIDEBOY$', 'Denzel Curry', 'Maxo Kream', 'Isaiah Rashad',
                        'Mike Stud', 'Mac Miller', 'Yonas', 'Childish Gambino', 'Rich Chigga',
                        'Three 6 Mafia', 'Azizi Gibson', 'RiFF RAFF', 'Lil Dicky',
                        'Lil Wayne', 'Tyga', 'Gucci Mane', 'Rick Ross', 'Asher Roth',
                        'Travis Scott', 'Migos', 'Rihanna', 'Bryson Tiller', '21 Savage',
                        'Rae Sremmurd', 'French Montana', 'Miley Cyrus', 'XXXTENTACION',
                        'Lil Pump', 'Ski Mask the Slump God', 'Xavier Wulf', 'SmokePurpp',
                        'A Boogie Wit Da Hoodie', 'Playboi Carti', 'Ugly God', 'Wiz Khalifa',
                        'Justin Bieber', 'Beyoncé', 'Nicki Minaj', 'Meek Mill']

    def definition(self, word):
        '''
        Function to get the definition of a word

        Parameters
        -------
        word: str
        '''

        dictionary = PyDictionary()

        definition = dictionary.meaning(word)

        if definition:
            for k, v in definition.items():
                definition[k] = ''.join(v)

        return definition

    def synonym(self, word, startswith=''):
        '''
        Function to get synonym word given a word

        Parameters
        -------
        word: str
        startswith: str
        '''
        dictionary = PyDictionary()

        synonyms = dictionary.synonym(word)

        if startswith:
            synonyms = [x for x in synonyms if x.startswith(startswith)]

        return synonyms

    def antonym(self, word, startswith=''):
        '''
        Function to get antonyms word given a word

        Parameters
        -------
        word: str
        startswith: str
        '''
        dictionary = PyDictionary()

        antonyms = dictionary.antonym(word)

        if startswith:
            antonyms = [x for x in antonyms if x.startswith(startswith)]

        return antonyms

    def pronouncing_rhyme(self, word, startswith=''):
        '''
        Function to get rhyming word from
        Pronouncing package given a word

        Parameters
        -------
        word: str
        startswith: str
        '''
        rhymes = pronouncing.rhymes(word)

        if rhymes:
            if startswith:
                rhymes = [x for x in rhymes if x.startswith(startswith)]

        return rhymes

    def get_rhyme(self, word, startswith=''):
        '''
        Function to get rhyming word from RhymeZone
        given a word

        Parameters
        -------
        word: str
        startswith: str

        Returns
        -------
        words: list
            - List of rhyming words

        TODO sort by syllable count, need to scrape page for syllable title
        '''
        url = 'https://www.rhymezone.com/r/rhyme.cgi?Word=%s&typeofrhyme=perfect' % word

        page = req.get(url)
        soup = BS(page.text, "html.parser")

        tags = soup.find_all('a')
        words = []

        for t in tags:
            if t.parent.name == 'b' and 'class' in t.attrs.keys():
                text = t.text
                text = re.sub(r'[^\x00-\x7F]+', ' ', text)
                words.append(text)