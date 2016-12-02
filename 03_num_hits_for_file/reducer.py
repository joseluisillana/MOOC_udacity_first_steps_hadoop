#!/usr/bin/python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# Loop around the data
# It will be in the format key\tval
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    word, count = data_mapped

    try:
        count = int(count)
    except ValueError:
        continue
   
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print "{0}\t{1}".format(current_word,current_count)
        current_count = count
        current_word = word

if current_word:
    print "{0}\t{1}".format(current_word,current_count)

