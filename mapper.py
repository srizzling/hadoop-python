#!/usr/local/bin/python
import sys
import datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = [x.strip() for x in line.split(',')]
    ts = float(words[0])
    word = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    print '%s\t%s' % (word, 1)