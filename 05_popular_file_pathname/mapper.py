#! /usr/bin/env python

#Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working
import sys
import re

#madafakaaaaaa['10.223.157.186', '-', '-', '[15/Jul/2009:15:50:35', '-0700]', '"GET', '/assets/js/lowpro.js', 'HTTP/1.1"', '200', '10469']

def mapper():
    stringToFind = "http://www.the-associates.co.uk"
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split(" ")

        #print "madafakaaaaaa{0}".format(data)

        # This is the place you need to do some defensive programming
        # what if there are not exactly 6 fields in that line?
        if len(data) != 10:
            print "madafakaaaaaa"
            continue

        # this next line is called 'multiple assignment' in Python
        # this is not really necessary, we could access the data
        # with data[2] and data[5], but we do this for conveniency
        # and to make the code easier to read
        ipclient, id, user, datetime, timezone, verb, request, protocol, statuscode, size = data
        datetime = datetime[:1]
        timezone = timezone[:-1]
        verb = verb[:1]
        protocol = protocol[:-1]
        
        result = stringToFind in request
 
        #print "MIRA\t{0}\t{1}\t{2}".format(result,request,request[31:])
        if result:
	    request = request[31:]

        # Now print out the data that will be passed to the reducer
        #print "{0}\t{1}\t{2}\t{3}\t{4}\t{5\t{6}".format(ipclient, id, user, datetime, request, statuscode, size)
        print "{0}\t{1}".format(request,1)

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__

mapper()
