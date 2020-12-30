
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