import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
import string

#Tokenizing raw data and filtering based  on punctuation and stop words
#stopwords = nltk.corpus.stopwords.words('english')
#stopwords.extend(string.punctuation)
#stopwords.append('')
# Create tokenizer and stemmer
#tokenizer = nltk.tokenize.punkt.PunktWordTokenizer()

def JacardCompare(raw_tokens,input_tokens,threshold=0.5):
	try :		
		jacardRatio=len(set(raw_tokens).intersection(input_tokens)) / float(len(set(raw_tokens).union(input_tokens)))
		return(jacardRatio)
	except:
		print("couldn't generate valid confidence match")
	#return (jacardRatio >= threshold)