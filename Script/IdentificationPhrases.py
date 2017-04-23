import nltk
from nltk import tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from xml.dom import minidom
import xml.etree.ElementTree as etree
import RecuperationVerbesSynKill

#1 récupérer emplacement verbe dans une phrase
#2 regarder si on trouve un nom en F faisant partie de la liste d'alexis dans la phrase
#3 si oui, regarder quelle date
#4 regarder la vicitime
#Bonus : si il trouve pas, on regarde la phrase d'après

listOfVerbsInText = RecuperationVerbesSynKill.findKillVerbsInText()
lmtzr = WordNetLemmatizer()

#place les verbes du texte dans la liste globale listOfVerbsInText
def getVerbs(pos):
	listOfIndex = []
#retourne une liste de mot dont le tag correspond à celui en entrée
	for document in root:
		for sentences in document:
			for sentence in sentences:
				for tokens in sentence:
					for token in tokens:
						tag = token.find('POS').text
						if (tag == pos):
							if (wordIsSameAsKillLemmas(token.find('word').text)):
								#print(token.find('word').text)
								listOfIndex.append(sentence.find('id').text)
								#print(listOfIndex.append(token.find('id').text))
	return listOfIndex


def wordIsSameAsKillLemmas(wordToTest):
	for index in range(len(listOfVerbsInText)):
		#print(listOfVerbsInText[index][0].lower())
		if (lmtzr.lemmatize(wordToTest).lower() == listOfVerbsInText[index][0].lower()):
			return True 
	return False



#ouverture des corpus
corpusTokenized='Wikipedia_F_only_Tokenizé par CoreNLP.xml'
xmldoc = open(corpusTokenized,'r', encoding = 'utf-8')
tree = etree.parse(xmldoc)
root = tree.getroot()

getVerbs("VB")
getVerbs("VBD")
getVerbs("VBG")
getVerbs("VBN")
getVerbs("VBZ")