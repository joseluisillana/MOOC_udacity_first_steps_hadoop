#!/usr/bin/python

import sys

oldId = None
listFieldsA = []
listFieldsB = []
type = ""

id = ""
title = ""
tagnames = ""
node_type = ""
parent_id = ""
abs_parent_id = ""
added_at = ""
score = ""
reputation = ""
gold = ""
silver = ""
bronze = ""

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    #if len(data_mapped) == 6:
	#print ">>>> 6 %s" % data_mapped
    #elif len(data_mapped) == 10:
	#print ">>>> 10 %s" % data_mapped

    idVal = data_mapped[0]
    type = data_mapped[1]

    #print " DATOS {1}-{2}>>>>>> {0}".format(data_mapped,idVal,type)

    #print " LISTAS >>>>>> {0} >>>> {1}".format(listFieldsA,listFieldsB)

    try:
        listFields = data_mapped[2:(len(data_mapped))]
    except ValueError:
        continue
  
    #print " LISTA vals >>>>>> {0}".format(listFields)
 
    if oldId == idVal:
	if type == "\"A\"":
	    listFieldsA = listFields
        else:
	    listFieldsB = listFields
    else:
        if oldId:
 	    if type == "\"A\"" and len(listFieldsA) != 0:
		reputation = str(listFields[0])
		gold = str(listFields[1])
		silver = str(listFields[2])
		bronze = str(listFields[3])
	    elif type == "\"A\"":
		reputation = ""
                gold = ""
                silver = ""
                bronze = ""
	    elif type == "\"B\"" and len(listFieldsB) != 0:
		id = str(listFields[0])
		title = str(listFields[1])
		tagnames = str(listFields[2])
		node_type = str(listFields[3])
		parent_id = str(listFields[4])
		abs_parent_id = str(listFields[5])
		added_at = str(listFields[6])
		score = str(listFields[7])
	    else:
		id = ""
                title = ""
                tagnames = ""
                node_type = ""
                parent_id = ""
                abs_parent_id = ""
                added_at = ""
                score = ""
	    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(oldId,id,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze)        

        oldId = idVal
        if type == "\"A\"":
            listFieldsA = listFields
        else:
            listFieldsB = listFields

if oldId:
    if type == "\"A\"" and len(listFieldsA) != 0:
        reputation = str(listFields[0])
        gold = str(listFields[1])
        silver = str(listFields[2])
        bronze = str(listFields[3])
    elif type == "\"A\"":
        reputation = ""
        gold = ""
        silver = ""
        bronze = ""
    elif type == "\"B\"" and len(listFieldsB) != 0:
        id = str(listFields[0])
        title = str(listFields[1])
        tagnames = str(listFields[2])
        node_type = str(listFields[3])
        parent_id = str(listFields[4])
        abs_parent_id = str(listFields[5])
        added_at = str(listFields[6])
        score = str(listFields[7])
    else:
        id = ""
        title = ""
        tagnames = ""
        node_type = ""
        parent_id = ""
        abs_parent_id = ""
        added_at = ""
        score = ""
    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(oldId,id,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze)

