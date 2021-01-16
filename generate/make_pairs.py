
import datetime
import os
from pprint import pprint as pp
import sys
import time

from generate import Generate


if __name__ == '__main__':
    '''
    y/n on word pairs consisting of
    random([adj, adv, verb]) + TopicWord

    once quit, save lines in 'saved/'

    Parameters
    -------
    n_pairs: int
        - Number of pairs to generate
        - Ex: python make_pairs.py 420
    '''
    n_pairs = 100

    if len(sys.argv) > 1:
        n_pairs = int(sys.argv[1])

    pairs = Generate().pairs(n_pairs=n_pairs)

    pairs = [x[0] + ' ' + x[1] for x in pairs]
    pairs = list(sorted(pairs))
    pairs.sort(key=len)

    save_lines = []

    for p in pairs:
        os.system('clear')
        print(p, '\n', 'y/n?', '\n')
        inp = input()