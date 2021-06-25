
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