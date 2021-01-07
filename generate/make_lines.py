
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