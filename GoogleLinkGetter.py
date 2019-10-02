def getLinkForInputQuery(queryInput):
	from googlesearch  import search
	#query="what is paracetomol"
	query=queryInput
	relevant_link_list=[]
	for link in search(query, tld="co.in", num=3, stop=1, pause=2):
		#print(link)
		if "pdf" in link or "youtube" in link or "jpeg" in link or "png" in link:
			continue
		relevant_link_list.append(link)
		##Bro take each link and pass to webtext processor url variable using threds
	return relevant_link_list
