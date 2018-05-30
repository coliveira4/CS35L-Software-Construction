#!/usr/bin/python

"""
shuf.py
Christina Oliveira
UID:20480448
"""
import argparse
import random, sys
"""from optparse import OptionParser

class randline:
    def __init__(self, filename):
        f = open(filename, 'r')
        self.lines = f.readlines()
        f.close()

    def chooseline(self):
        return random.choice(self.lines)
"""
def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE

    Output randomly shuffled lines"""

    parser = argparse.ArgumentParser(description='shuffle the input.')
    parser.add_argument("-n", "--numlines",
                      action="store", dest="numlines",
                      help="output at most COUNT lines")
    parser.add_argument("-e", "--echo", dest="echolines", default=None, nargs='+',
                      action="store", help="treat each ARG as an input line")
    parser.add_argument("-r", "--repeat", dest="repeat", default=False, const=True,
                      action="store_const", help="whether to shuffle with replacement or without")
    args = parser.parse_args()
    input_lines = args.echolines #input lines
    try:
        numlines = int(args.numlines)
    except:
        numlines = len(input_lines)
    if numlines < 0:
        parser.error("negative count: {0}".
                     format(numlines))
    if args.repeat:
        for i in range(numlines):
            line=random.choice(input_lines)
            print(line)
    else:
        lines=random.sample(input_lines, numlines)
        for line in lines:
            print(line)

if __name__ == "__main__":
    main()
