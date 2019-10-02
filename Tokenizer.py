import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import JacardComparer as comparer
import CosineComparer as cosineCompare


def Tokenize(raw_data):
	#Tokenizing raw data and filtering based  on punctuation and stop words
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	stemmer=nltk.stem.snowball.SnowballStemmer('english')
	global eachSentence
	eachSentence = [token.lower().strip(string.punctuation) for token in sent_detector.tokenize(raw_data)]
	#universal_ratio stores the highest ratio of the sentence
	universal_ratio = 0
	counter = 0
	sentence_no = 0	
	stemmed_sentence_List=[]
	for sentence in eachSentence:
		eachSentenceAsWords=tokensInEachSentence=nltk.word_tokenize(sentence)		
		stop_words = set(stopwords.words('english'))		
		word_tokens = eachSentenceAsWords
		filtered_sentence = [w for w in word_tokens if not w in stop_words]
		filtered_sentence = []
		for w in word_tokens:
			if w not in stop_words:
				filtered_sentence.append(w)
		#filtered_sentence.remove('(')
		#filtered_sentence.remove(')')
		#print(filtered_sentence) 
		#stem_b = ['paracetamol ','overdose','appetite','nausea','vomiting','stomach pain','confusion']
		question="queryInput"
		filteredQuestion=TokenizeQuestion(question)
		#stem_b = ['paracetamol']
		#stems_b = [stemmer.stem(token) for token in filteredQuestion]
		stems_a = [stemmer.stem(token) for token in filtered_sentence]
		#print(stems_a)
		stemmed_sentence_List.append(stems_a)
		#confidence_ratio = comparer.JacardCompare(stems_a,stems_b)
		#confidence_ratio = cosineCompare.CosineCompare(sentence,question)
		#print(stems_a)
		#print(confidence_ratio)
		
		#if (confidence_ratio > universal_ratio):
		#	universal_ratio = confidence_ratio
		#	sentence_no = counter			
		#counter += 1		
	#sentence_no holds the sentence with the highest ratio --> store to DB with the question
	#print(stemmed_sentence_List)
	#print(counter)
	#print(sentence_no)
	#print(eachSentence[sentence_no])
	
	return stemmed_sentence_List
#Tokenize Question and return question as tokens in a list
def TokenizeQuestion(question):
	#Tokenizing raw data and filtering based  on punctuation and stop words
	stemmed_question_Token_List=[]
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	stemmer=nltk.stem.snowball.SnowballStemmer('english')
	eachQuestion = [token.lower().strip(string.punctuation) for token in sent_detector.tokenize(question)]
	#universal_ratio stores the highest ratio of the sentence
	universal_ratio = 0
	counter = 0
	sentence_no = 0	
	for sentence in eachQuestion:
		eachSentenceAsWords=tokensInEachSentence=nltk.word_tokenize(sentence)		
		stop_words = set(stopwords.words('english'))	
		word_tokens = eachSentenceAsWords
		filtered_question = [w for w in word_tokens if not w in stop_words]
		filtered_question = []
		for w in word_tokens:
			if w not in stop_words:
				filtered_question.append(w)
				#question_Token_List.append(filtered_question)
		#filtered_sentence.remove('(')
		#filtered_sentence.remove(')')
		#print(filtered_sentence) 
		#stem_b = ['paracetamol ','overdose','appetite','nausea','vomiting','stomach pain','confusion']	
		stems_b = [stemmer.stem(token) for token in filtered_question]
		stemmed_question_Token_List.append(stems_b)
	return stemmed_question_Token_List
def ComputeSimilarity(StemmedQuestionTokensList,StemmedAnswerSentencesTokenizedList):
	#universal_ratio stores the highest ratio of the sentence
	universal_ratio = 0
	counter = 0
	sentence_no = 0	
	for eachStemmedQuestionAsToken in StemmedQuestionTokensList:
		for eachStemmedSentenceAsTokens in StemmedAnswerSentencesTokenizedList:
			confidence_value=comparer.JacardCompare(eachStemmedSentenceAsTokens,eachStemmedQuestionAsToken)
			#print(confidence_value)
			if(confidence_value!=None):
				if(confidence_value>universal_ratio):
					universal_ratio=confidence_value
					sentence_no=counter
				counter+=1
	#print(sentence_no)
	#print(eachSentence)
	#thistuple=(eachSentence[sentence_no],universal_ratio)
	thisset = [eachSentence[sentence_no],universal_ratio]
	return thisset
	#print(eachSentence[sentence_no])
	


		
		

