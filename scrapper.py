import chatterbot as ch
import requests
import sys
import urllib.request
from bs4 import BeautifulSoup

from bs4.element import Comment

#words_filtered = "x"
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
'''
def text_from_html(body):
	VALID_TAGS = ['p']
	soup = BeautifulSoup(value)
	for tag in soup.findAll('p'):
	if tag.name not in VALID_TAGS:
		tag.replaceWith(tag.renderContents())
'''
def text_from_html(body):
	words_filtered = ""
	soup = BeautifulSoup(body, 'html.parser')
	texts = soup.findAll({'p':True})	
	visible_texts = filter(tag_visible, texts)
	print(words_filtered) 	
	#return u" ".join(t.strip() for t in visible_texts)
	for t in visible_texts:
		words_filtered += str(t.text)
	#print(words_filtered)
	return words_filtered


#print(text_from_html(html))

def fetchdata():

	url = "http://www.nytimes.com/2009/12/21/us/21storm.html"
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html,'html.parser')
	for script in soup(['script', 'style', 'head', 'title', 'meta', '[document]']):
		script.extract()
	text = soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = '\n'.join(chunk for chunk in chunks if chunk)
	print(text.encode('utf-8'))
