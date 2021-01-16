
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
