import nltk
from nltk import tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from xml.dom import minidom
import xml.etree.ElementTree as etree


listOfVerbsInText = []
lmtzr = WordNetLemmatizer()

#place les verbes du texte dans la liste globale listOfVerbsInText
def getVerbs(pos):
#retourne une liste de mot dont le tag correspond à celui en entrée
	for document in root:
		for sentences in document:
			for sentence in sentences:
				for tokens in sentence:
					for token in tokens:
						tag = token.find('POS').text
						if (tag == pos):
							name = token.find('word').text
							listOfVerbsInText.append(name)

def turnVerbsInLemmas(listToLemmatize):
	listOfLemmatizedVerbs = []
	for verbs in listToLemmatize:
		#Si c'est un mot :
		#verbs = lmtzr.lemmatize(verbs)
		#Si c'est un Synsets
		verbs = lmtzr.lemmatize(verbs.lemmas()[0].name())
		listOfLemmatizedVerbs.append(verbs)
	return listOfLemmatizedVerbs



def initKilledSynsets():
	listOfKilledSynsets = []
	for syn in wn.synsets('killed'):
		listOfKilledSynsets.append(syn)
	listOfKilledSynsets = checkDoublonSynsets(listOfKilledSynsets)
	return listOfKilledSynsets

#Retourne une liste avec tous les synonymes du mot "killed"
#param lch_threshold : le seuil de ressemblance
def synKilled(listOfKilledSynsets, lch_threshold=2.26):
	finalList = []
	#on stocke les synsets du mot dans syn
	for syn in listOfKilledSynsets:
		finalList.append(syn)
		#on stocke tous les synsets qui existe
		for allsyn in wn.all_synsets():
			#print('allsyn : ', allsyn.lemmas()[0].name())
			try:
				#on stocke la valeur de ressemblance entre les synsets du mot et le synsets testé
				lch = syn.lch_similarity(allsyn)
			except:
				continue
			# Si la valeur de ressemblance est supérieure à la valeur seuil
			if lch >= lch_threshold:
				#finalList.append({syn1, allsyn, lch})
				finalList.append(allsyn)
	return finalList


#trouve les verbes synonymes du mot killed dans la liste des verbes du texte
def findKillVerbsInText():
	finalList = []
	listOfVerbs = putTextInList('Text des verbes.txt')
	listOfSyn = putTextInList('Text des synonymes de killed.txt')
	#On fait le tour de la liste de verbe du texte
	for index in range(len(listOfVerbs)):
		#synsetVerb = wn.synsets(listOfVerbs[i])
		#On fait le tour de la liste des synsets de 'killed'
		for j in range(len(listOfSyn)):
			if(listOfVerbs[index] == listOfSyn[j]):
				finalList.append([listOfVerbs[index], index])
	return finalList


def putListInTxt(listToTxt, nameOfTheTxtFile):
	textOfList = open(nameOfTheTxtFile, 'w', encoding = 'utf-8')
	for i in range(len(listToTxt)):
		#print(listToTxt[i])
		#Si c'est un Synset à ajouter :
		#textOfList.write(listToTxt[i].lemmas()[0].name().lower())
		#Si c'est un mot à ajouter :
		textOfList.write(listToTxt[i])
		textOfList.write('\n')
	textOfList.close()

def putTextInList(txt):
	finalList = []
	verbsText = open(txt, 'r', encoding = 'utf-8')
	for line in verbsText:
		finalList.append(line)
	return finalList

def checkDoublonSynsets(listToCheck):
	listReturned = []
	for i in range(len(listToCheck)):
		if (lookInTheReturnedList(listReturned, listToCheck[i])):
			listReturned.append(listToCheck[i])
	return listReturned

def lookInTheReturnedList(actualList, word):
	for i in range(len(actualList)):
		if (actualList[i].lemmas()[0].name().lower() == word.lemmas()[0].name().lower()):
			return False
	return True

def printAListOfSynsets(theList):
	for i in range(len(theList)):
		print(theList[i].lemmas()[0].name())

def printAList(theList):
	for i in range(len(theList)):
		print(theList[i])


#ouverture des corpus
corpusTokenized='Wikipedia_F_only_Tokenizé par CoreNLP.xml'
xmldoc = open(corpusTokenized,'r', encoding = 'utf-8')
tree = etree.parse(xmldoc)
root = tree.getroot()


#getVerbs("VB")
#getVerbs("VBD")
#getVerbs("VBG")
#getVerbs("VBN")
#getVerbs("VBZ")
#listOfVerbsInText = turnVerbsInLemmas()
#putListInTxt(listOfVerbsInText, "Text des verbes.txt")

#listOfKillSyn = initKilledSynsets()
#listOfKillSyn = synKilled(listOfKillSyn)
#listOfKillSyn = checkDoublonSynsets(listOfKillSyn)
#listOfKillSyn = turnVerbsInLemmas(listOfKillSyn)
#putListInTxt(listOfKillSyn, "Text des synonymes de killed.txt")

killVerbsInText = findKillVerbsInText()
#printAList(killVerbsInText)
#print(len(killVerbsInText))
#putListInTxt(killVerbsInText, 'Liste syn Kill dans Corpus.txt')