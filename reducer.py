#!/usr/local/bin/python

from operator import itemgetter

import sys

current_word = None
current_count = 0
current_protocol= None
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count_string = line.split('\t', 1)

    count, protocol = count_string.split(":");

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word and current_protocol == protocol:
        current_count += count
    else:
        if current_word and current_protocol:
            # write result to 
            print '%s\t%s:%s' % (current_word, current_count, current_protocol)
        current_count = count
        current_word = word
        current_protocol = protocol

    # do not forget to output the last word if needed!
if current_word == word and current_protocol == protocol:
    print '%s\t%s:%s' % (current_word, current_count, current_protocol)