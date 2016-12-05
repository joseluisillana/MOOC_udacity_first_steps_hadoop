#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL)
    #reader.next()

    for line in reader:
        data = line

	if len(data) > 0 and (data[0] == "id" or data[0] == "user_ptr_id"):
	    continue
	#print len(data)
        if len(data) == 5:
            try:
		#print ">>> VIENEN 5: %s" % str(data)
		user_ptr_id = data[0]
                reputation = data[1]
		gold = data[2]
		silver = data[3]
		bronze = data[4]
		print "\"{0}\"\t\"A\"\t\"{1}\"\t\"{2}\"\t\"{3}\"\t\"{4}\"".format(user_ptr_id,reputation,gold,silver,bronze)
            except ValueError:
                continue
        elif len(data) == 19:
            try:
		#print ">>> VIENEN 19: %s" % str(data)
                id = data[0]
		title = data[1]
		tagnames = data[2]
		author_id = data[3]
		node_type = data[5]
		parent_id = data[6]
		abs_parent_id = data[7]
		added_at = data[8]
		score = data[9]
		print "\"{0}\"\t\"B\"\t\"{1}\"\t\"{2}\"\t\"{3}\"\t\"{4}\"\t\"{5}\"\t\"{6}\"\t\"{7}\"\t\"{8}\"".format(author_id,id,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score)
            except ValueError:
                continue
        else:
	    continue	
	



mapper()
