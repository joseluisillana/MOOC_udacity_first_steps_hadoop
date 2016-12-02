#!/usr/bin/python

import sys

numTotal = 0
salesTotal = float(0)
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", numTotal, "\t", salesTotal
        oldKey = thisKey
        salesTotal = float(thisSale)
        numTotal = 0
        continue
    elif oldKey and oldKey == thisKey:
        salesTotal += float(thisSale)
        numTotal+=1
        continue

    print "entro"
    oldKey = thisKey
    salesTotal = float(thisSale)
    numTotal += 1
if oldKey != None:
    print oldKey, "\t", numTotal, "\t", salesTotal

