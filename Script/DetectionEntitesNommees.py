import nltk
from nltk import tag
from xml.dom import minidom
import xml.etree.ElementTree as etree

xmldoc = open('Wikipedia_F_only_Tokenizé par CoreNLP.xml','r', encoding = 'utf-8')
tree = etree.parse(xmldoc)
root = tree.getroot()

def getAttribs(pos):
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

nnp = getAttribs("NNP")
list_Of_F_Names = getFNNP(nnp)
list_Of_F_Names = checkDoublon(list_Of_F_Names)
printAList(list_Of_F_Names)
