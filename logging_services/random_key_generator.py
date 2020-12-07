#!/usr/bin/env python3
# pylint: disable=all
"""
Generate a random string of length N where N is a number passed as
an argument in a command line call

e.g. $./random_key_generator.py 11; will generate a key of length 11 chars.
"""
from string import ascii_letters, digits
from random import randint
import sys


def generate_key(n):
    choices = ascii_letters + digits
    k = [choices[randint(0, len(choices) - 1)] for _ in range(n)]
    return ''.join(k)


if __name__ == '__main__':
    try:
        n = sys.argv[1]
    except IndexError:
        n = 1
    print(generate_key(int(n)))
