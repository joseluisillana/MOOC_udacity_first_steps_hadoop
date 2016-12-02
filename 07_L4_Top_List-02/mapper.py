#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    mapAll = {}
    for line in reader:

        # YOUR CODE HERE
            
        #writer.writerow(line)
        data = line

        if len(data) >= 6:
            try:
                id, title, tagnames, authorId, body, nodeType = data
                if not ("?\n" in body or "!\n" in body or ". " in body ):
                    mapAll["\"{0}\"\t\"{1}\"\t\"{2}\"\t\"{3}\"\t\"{4}\"\t\"{5}\"".format(id, title, tagnames, authorId, body, nodeType)] = len(body)
                    #mapAll = sorted(mapAll.items(), key= lambda x: x[1])
                    #print "\"{0}\"\t\"{1}\"\t\"{2}\"\t\"{3}\"\t\"{4}\"\t\"{5}\"".format(id, title, tagnames, authorId, body, nodeType)
                    #print"{0}".format(body)
            except ValueError:
                print "Error7\t{0}\t{1}".format(data,len(data))
                continue
        else:
            continue
    for element in sorted(mapAll.items(), key= lambda x: x[1])[1:11]:
        print element[0]



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
main()
