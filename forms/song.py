#! /usr/bin/env python
from section import Section


class Song:

    def __init__(self, title='', artist='', theme=''):

        self.sections = {'Chorus': [],
                         'Verse': [],
                         'Hook': [],
                         'Bridge': [],
                         'Intro': [],
                         '