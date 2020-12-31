
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

        if not self.pos_dict:
            self.load_pos_words()

        if not self.topic_dict:
            self.load_topics()

        if topic:
            topic_list = self.topic_dict[topic]
        else:
            topic_list = []
            for k, v in self.topic_dict.items():
                topic_list.extend(v)

        pairs = []

        for i in range(0, n_pairs):
            # Same starting letter
            topic = random.choice(topic_list)
            startswith = topic.lower()[0]
            pos = random.choice(['adj', 'adv', 'verb'])
            word_list = self.pos_dict[pos]

            word_list = [x for x in word_list
                        if x.lower().startswith(startswith)]
            if not word_list:
                continue

            modifier = random.choice(word_list)

            pairs.append([modifier, topic])

        return pairs

    def load_topics(self):
        '''
        Get all topic words from "../topics/"

        Returns
        -------
        Set self.topic_dict with self.topic_dict[topic] = topic_words
        '''
        for f in os.listdir('../topics/'):
            topic = f.split('.')[0]

            with open(('../topics/' + f), 'r') as text:
                topic_words = text.readlines()
