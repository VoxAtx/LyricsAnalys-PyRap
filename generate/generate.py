
import os
import sys
import random

from PyDictionary import PyDictionary
from nltk.corpus import wordnet as wn

if '../' not in sys.path:
    sys.path.append("../")

from util.wordutil import WordUtil as WU


class Generate:

    def __init__(self):
        self.pos_dict = {}
        self.topic_dict = {}
        self.topic_words = []
        self.line_topics = {}
        self.lines = []
        self.conjunctions = ['and', 'but', 'yet', 'or', 'because',
                            'for', 'nor', 'so', 'rather than',
                            'as much as']

    def pairs(self, n_pairs=100, topic=None):
        '''
        Generate pairs of words using the
        formula `pair = topic_word + random[adj, adv, verb]`

        Parameters
        -------
        n_pairs: int
            - Number of pairs to generate
        '''