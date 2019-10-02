'''
def urlParser(uriList):
	from urllib.parse import urlparse
	# from urlparse import urlparse  # Python 2
    new_link_list=[]
	for uri in uriList:		
		parsed_uri = urlparse(uri)
		result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

		print(result)

# gives
#'http://stackoverflow.com/'
'''