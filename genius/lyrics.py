
from nltk.corpus import wordnet
import nltk

import os
import re
import pickle
import random


class Lyrics:

    def __init__(self):
        self.lyrics_path = '../lyrics/'
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

    def clean_title(self, title):
        return re.sub(r'[^\x00-\x7F]+', ' ', title)

    def get_artist_songs(self, artist):
        '''
        Get the organized lyrics for all of an artist's songs

        Parameters
        -------
        artist: str

        Returns
        -------
        songs: dict
            - Dict of organized lyrics by song title
        '''
        lyric_p = [self.lyrics_path + x for x in
                   os.listdir(self.lyrics_path)
                   if x.replace('.pickle', '').replace('_', ' ') == artist][0]

        with open(lyric_p, 'rb') as f:
            song_dict = pickle.load(f)

        songs = {}

        for title, lyrics in song_dict.items():
            organized_lyrics = self.get_lyrics(lyrics)
            title = self.clean_title(title)
            songs[title] = organized_lyrics

        return songs

    def get_lyrics(self, song_lyrics):
        '''
        Convert string of lyrics into Verses, Choruses, Hooks, and Bridges

        Parameters
        -------
        song_lyrics: str
            - Giant string of lyrics for one song

        Returns
        -------
        organized_lyrics: dict
            - Dict of lyrics by Verse, Chorus, Hook, and Bridge
            - Each section (dict key) can have multiple sections
                - Ex: multiple verses, multiple choruses
        '''
        verse_lines = []
        chorus_lines = []
        hook_lines = []
        bridge_lines = []

        lines = song_lyrics.splitlines()

        for l in range(len(lines)):
            line = lines[l].lower()

            if line == '\n':
                continue

            if '[' in line and 'verse' in line:
                section_lines = []
                count = l + 1
                done = False
                while count < len(lines) and not done:
                    if '[' not in lines[count]:
                        if lines[count] != '':
                            section_lines.append(lines[count])
                        count += 1
                    else:
                        done = True
                verse_lines.append(section_lines)

            elif '[' in line and 'chorus' in line:
                section_lines = []
                count = l + 1
                done = False
                while count < len(lines) and not done:
                    if '[' not in lines[count]:
                        if lines[count] != '':
                            section_lines.append(lines[count])
                        count += 1
                    else:
                        done = True
                chorus_lines.append(section_lines)

            elif '[' in line and 'hook' in line:
                section_lines = []