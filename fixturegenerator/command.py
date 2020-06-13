#!/usr/bin/env python

import sys

from fixturegenerator import FixtureGenerator

def main():
    try:
        names = sys.argv[1].split(',')
    except IndexError:
        print('Please write the needed classes')
    else:
        fixtures = FixtureGenerator.from_list(names)
        for fixture in fixtures:
            fixture.print_all()
            print('')
