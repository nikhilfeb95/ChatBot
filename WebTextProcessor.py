import scrapper as scrap
import urllib.request
import Tokenizer as token
import GoogleLinkGetter as googly
from urllib.request import Request, urlopen

def StartWebtextProcessing(link,_question,result,index):
	url=link
	question=_question
#url = 'https://www.drugs.com/paracetamol.html'
#question="Cancer Cure"
#url=googly.getLinkForInputQuery(question)
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = urllib.request.urlopen(req).read()
	raw_data = scrap.text_from_html(html)

#filtered_question=token.Tokenize(question)
#filtered_answer
	stemmed_sentences_list=token.Tokenize(raw_data)
	stemmed_question_list=token.TokenizeQuestion(question)
	returnedSentenceAndConfidValAsTuple=token.ComputeSimilarity(stemmed_question_list,stemmed_sentences_list)
	result[index] = returnedSentenceAndConfidValAsTuple
	#print(returnedSentenceAndConfidValAsTuple)
	#return returnedSentenceAndConfidValAsTuple
#print(filtered_question_list)
#confidenceVal_List=token.ComputeSimilarity(filtered_question_list,filtered_sentences_list)
#sentencesCollection = raw_data.split('.')
#for sentence in sentencesCollection:
#	print(sentence)
