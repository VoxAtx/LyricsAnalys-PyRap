
#! /usr/bin/env python
from line import Line


class Section:

    def __init__(self, lines=[], name='', topic=''):
        '''
        Sections are 3D matrix
            - Ex: Chorus: [chorus1, chorus2]
            - chorus1: [['words', words'],
                        ['words', 'words']]