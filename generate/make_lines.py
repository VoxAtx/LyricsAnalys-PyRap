
import datetime
import os
from pprint import pprint as pp
import sys
import time
import random

from generate import Generate


if __name__ == '__main__':
    '''
    y/n on lines

    once quit, save lines in 'savedlines/'
    '''
    conjunctions = ['and', 'but', 'yet', 'or', 'because',
                        'for', 'nor', 'so', 'rather than',
                        'as much as']

    compares = ['is better than',
              'is worse than',
              'could never defeat a',
              'would win in a fight with a',
              'could never fuck a',
              'always made me feel like a',
              'could never be as good as a']

    createstuff = Generate()
    createstuff.load_lines()

    lines = createstuff.lines

    save_lines = []
