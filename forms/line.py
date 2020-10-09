
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
        self.char_count = len(self.line.replace(' ',''))
        self.start_char = self.line[0].lower()
        self.end_word = self.line[-1]
        self.word_pos = self.pos()
        self.pos_stats = ['%s: %s' % (pos, len(words)) for pos, words
                         in self.word_pos.items()]
        self.stats = {'Word Count': self.word_count,
                      'Character Count': self.char_count,
                      'Starting Letter': self.start_char,
                      'Ending Word:': self.end_word,
                      'POS used:': '\n'.join(self.pos_stats)}

    def __str__(self):
        return ' '.join(self.line)[1:]
