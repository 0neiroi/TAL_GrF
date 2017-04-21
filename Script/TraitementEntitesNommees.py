import nltk
from nltk import tag
from xml.dom import minidom
import xml.etree.ElementTree as etree
import csv

def getAttribs(pos):
#retourne une liste de mot dont le tag correspond à celui en entrée
	listReturned = []
	for document in root:
		for sentences in document:
			for sentence in sentences:
				for tokens in sentence:
					for token in tokens:
						tag = token.find('POS').text
						if (tag == pos):
							name = token.find('word').text
							listReturned.append(name)

	return listReturned

def getFNNP(listOfNPP):
	listReturned = []
	for i in range(len(listOfNPP)):
		if (listOfNPP[i][:1].lower() == "f"):
			listReturned.append(listOfNPP[i])
	return listReturned

def checkDoublon(listOfName):
	listReturned = []
	for i in range(len(listOfName)):
		if (lookInTheReturnedList(listReturned, listOfName[i])):
			listReturned.append(listOfName[i])
	return listReturned

def lookInTheReturnedList(actualList, name):
	for i in range(len(actualList)):
		if (actualList[i].lower() == name.lower()):
			return False
	return True

def printAList(theList):
	for i in range(len(theList)):
		print(theList[i])

#nom des corpus
corpusTokenized='Wikipedia_F_only_Tokenizé par CoreNLP.xml'
corpusEN='Wikipedia_F_only_NamedEntities.tsv'
#ouverture des corpus
##xmldoc = open(corpusTokenized,'r', encoding = 'utf-8')
##tree = etree.parse(xmldoc)
##root = tree.getroot()

tsvdoc=open(corpusEN)
reader=csv.reader(tsvdoc)
data=list(reader)
for i in range (0,10):
        print(data[i])


##nnp = getAttribs("NNP")
##list_Of_F_Names = getFNNP(nnp)
##list_Of_F_Names = checkDoublon(list_Of_F_Names)
##printAList(list_Of_F_Names)
