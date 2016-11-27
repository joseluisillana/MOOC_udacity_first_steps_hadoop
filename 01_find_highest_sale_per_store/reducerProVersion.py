#!/usr/bin/python

import sys


oldStoreKey = None
oldItemKey = None
salesTotalPerStore = 0
itemMaxSalesPerStore = None
salesMaxAtMoment = 0
salesTotalPerItem = 0


# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisStoreKey, thisItemKey, thisSale = data_mapped

    if oldStoreKey and oldStoreKey != thisStoreKey:
	print oldStoreKey, "\t", itemMaxSalesPerStore, "\t", salesMaxAtMoment
        oldStoreKey = thisStoreKey
        oldItemKey = None
        salesTotalPerItem = float(thisSale)
        salesTotalPerStore = salesTotalPerItem
        salesMaxAtMoment = salesTotalPerItem
        itemMaxSalesPerStore = thisItemKey

    if oldStoreKey and oldItemKey and oldItemKey != thisItemKey:
    	if salesMaxAtMoment <= salesTotalPerItem:
		salesMaxAtMoment = salesTotalPerItem
		itemMaxSalesPerStore = thisItemKey
		#print oldStoreKey, "\t", oldItemKey, "\t", salesTotalPerItem
	oldItemKey = thisItemKey;
	salesTotalPerItem = float(thisSale)
        salesTotalPerStore = salesTotalPerItem

    elif oldStoreKey and oldItemKey and oldItemKey == thisItemKey:
	salesTotalPerItem += float(thisSale)
	#salesTotalPerStore += salesTotalPerItem
	salesMaxAtMoment = salesTotalPerItem
        itemMaxSalesPerStore = thisItemKey 



    if oldStoreKey == None and oldItemKey == None:
    	oldStoreKey = thisStoreKey
        oldItemKey = thisItemKey
	salesTotalPerItem = float(thisSale)
	salesTotalPerStore = salesTotalPerItem
	#if salesMaxAtMoment <= salesTotalPerItem:
	salesMaxAtMoment = salesTotalPerItem
	itemMaxSalesPerStore = thisItemKey


if oldStoreKey != None and oldItemKey != None:
    print oldStoreKey, "\t", oldItemKey, "\t", salesTotalPerItem

