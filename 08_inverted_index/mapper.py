#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv

def findOccurences(phrase, word):
    return [(i,len(i)) for i, letter in enumerate(phrase) if letter == word]

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_NONE)
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    fantasticTotal = 0
    fantastically_list = []

    mapAll = {}
    for line in reader:

        # YOUR CODE HERE
            
        #writer.writerow(line)
        data = line

        #print ">>>>>vienen:" + str(len(data)) + "\t" + str(data)
        
	# if only a portion of body comes
        if len(data) <= 1:
            try:
		body = data[0]
		continue
            except ValueError:
                continue
        elif len(data) <= 5:
            try:
		id = data[0]
                body = data[4]
            except ValueError:
                continue
        elif len(data) <= 15:
            try:
                body = data[0]
		continue
            except ValueError:
                continue
        elif len(data) <= 19:
            try:
                id = data[0]
                body = data[4]
            except ValueError:
                continue
        else:
	    continue	
	
	import re
	words = re.finditer(r"[\w']+", body)
        #print words
	#words = map(lambda x: x.lower(), words)
        for word in words:
	    if "fantastic" == word.group(0).lower() or "fantastically" == word.group(0).lower():
	        print "\"{0}\"\t{1}\t{2}\t{3}".format(word.group(0),1,id,(word.start(0),word.start(0)))		
        else:
            continue
    for element in sorted(mapAll.items(), key= lambda x: x[1])[1:11]:
        print element



test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__
mapper()
