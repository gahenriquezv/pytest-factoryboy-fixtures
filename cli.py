import sys

from fixturegenerator import FixtureGenerator

if __name__ == '__main__':
    names = sys.argv[-1].split(',')
    fixtures = FixtureGenerator.from_list(names)

    for fixture in fixtures:
        fixture.print_all()
        print('')
