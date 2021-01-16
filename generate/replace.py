
import sys
import os
import random
from pprint import pprint as pp

if '../' not in sys.path:
    sys.path.append("../")

from genius.lyrics import ConvertLyrics as cl
from util.wordutil import WordUtil as wu
from generate import Generate as gen
