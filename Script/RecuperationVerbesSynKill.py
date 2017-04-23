import nltk
from nltk import tag
from nltk.corpus import wordnet as wn
from xml.dom import minidom
import xml.etree.ElementTree as etree
import csv


listReturned = []


def getAttribs(pos):
#retourne une liste de mot dont le tag correspond à celui en entrée
	for document in root:
		for sentences in document:
			for sentence in sentences:
				for tokens in sentence:
					for token in tokens:
						tag = token.find('POS').text
						if (tag == pos):
							name = token.find('word').text
							listReturned.append(name)

def synKilled(word, lch_threshold=2.26):
	finalList = []
	#on stocke les synsets du mot dans net1
	for syn1 in wn.synsets(word):
		#on stocke tous les synsets qui existe
		for allsyn in wn.all_synsets():
			try:
				#on stocke la valeur de ressemblance entre les synsets du mot et le synsets testé
				lch = syn1.lch_similarity(allsyn)
			except:
				continue
			# Si la valeur de ressemblance est supérieure à la valeur seuil
			if lch >= lch_threshold:
				#finalList.append({syn1, allsyn, lch})
				finalList.append(syn1)
	return finalList

def findKillSyn(listOfVerbs, listOfSynsets, lch_threshold=2.26):
	finalList = []
	for i in range(len(listOfVerbs)):
		synsetVerb = wn.synsets(listOfVerbs[i])
		for syn in wn.synsets(listOfVerbs[i]):
			for allsyn in wn.all_synsets():
				#on stocke la valeur de ressemblance entre les synsets du mot et le synsets testé
				lch.wn.synsets() = listOfVerbs[index].lch_similarity(allsyn)
				if(lch >= lch_threshold):
					finalList.append(listOfVerbs[i])
		return finalList

def printAList(theList):
	for i in range(len(theList)):
		print(theList[i])


#ouverture des corpus
corpusTokenized='Wikipedia_F_only_Tokenizé par CoreNLP.xml'
xmldoc = open(corpusTokenized,'r', encoding = 'utf-8')
tree = etree.parse(xmldoc)
root = tree.getroot()


getAttribs("VB")
getAttribs("VBD")
getAttribs("VBG")
getAttribs("VBN")
getAttribs("VBZ")
listOfKillSyn = synKilled('killed')
printAList(listOfKillSyn)