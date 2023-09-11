
import pickle
import os
import sys
import re
from pprint import pprint as pp

from bs4 import BeautifulSoup as BS
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary
import pronouncing
import requests as req

from genius.lyrics import ConvertLyrics as lyrics


class WordUtil:

    def __init__(self):
        '''
        Class to interface with all external writing tools