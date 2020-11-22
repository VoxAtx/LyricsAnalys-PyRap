#! /usr/bin/env python
from section import Section


class Song:

    def __init__(self, title='', artist='', theme=''):

        self.sections = {'Chorus': [],
                         'Verse': [],
                         'Hook': [],
                         'Bridge': [],
                         'Intro': [],
                         'Outro': []}
        self.title = title
        self.artist = artist
        self.theme = theme
        # list of tuples (section_name, index)
        self.arrangement = []

    def work_on_section(self, section):

        sec = self.sections[section]

        if len(s