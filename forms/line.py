
#! /usr/bin/env python
from nltk import *


class Line:
    '''
    Class for managing a single line(list) of words
    '''
    def __init__(self, line=[]):

        if isinstance(line, str):
            self.words = line.split()
        else:
            self.words = line
        self.line = ' '.join(self.words)[1:]
        self.clean_line = self.clean_line()
        self.word_count = len(self.words)