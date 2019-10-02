import GoogleLinkGetter as goog
import WebTextProcessor as process
import UrlParser as parse
import aiml
import sys
import logging
import urllib
import threading
from threading import Thread
from json import JSONDecoder
from multiprocessing import Pool
'''
print("Ask me anything")
userQuestion=input()
'''
class ConsoleEntry:
	def __init__(self):
		global mybot
		mybot = aiml.Kernel()
		mybot.setBotPredicate("name","MediBot")
		mybot.learn('startup.xml')
		#Calling load aiml b for loading all AIML files
		mybot.respond('load aiml b')
#p here specifies the multiprocessing pool being used
	def MedBot(self,userQuestion):
		threads = []
		while True:
			#userQuestion = input("Ask me any question?")
			if userQuestion == "quit":
				exit()
			else:
				bot_response = mybot.respond(userQuestion.upper())
				if bot_response != "":
					return bot_response
				else:
					print("Fetching Data with scrapper ...")
					##check for userquestion in aiml
					##if yes print answer 
					##if no
					#url="https://www.google.com/search?q=paracetomol"
					tupleReceivedList=[]
					search_link_list=goog.getLinkForInputQuery(userQuestion)

					#filtered_searchLink_list=[]
					#index=0
					#for eachLink in search_link_list:
						#filtered_link= parse.urlParser(eachLink)
						#if filtered_link in filtered_searchLink_list:
						#if eachLink  in filtered_searchLink_list:
						#	continue
						#filtered_searchLink_list.append(eachLink)
						#index+=1

					#print(filtered_searchLink_list[0])
					#print(filtered_searchLink_list[1])
					#print(filtered_searchLink_list[2])	

					#print(search_link_list[0])
					#print(search_link_list[1])
					#print(search_link_list[2])
					#with Pool(3) as p:
						#tupleReceived=p.map(process.StartWebtextProcessing(link,userQuestion),search_link_list)
					#result_threads stores the return from the thread
					thread = [None]*3
					results = [None]*3
					for i in range(0,3):
						try:							
							thread[i] = Thread(target = process.StartWebtextProcessing, args = [search_link_list[i],userQuestion,results,i])
							thread[i].daemon = True
							thread[i].start()
							thread[i].join()
						except:
							continue
					#for i in range(len(thread)):
						
					#process = Thread(target = process.StartWebtextProcessing, args = [link,userQuestion])
					#tupleReceivedList.append(tupleReceived)
					final_answer=""
					#index=len(results)
					print(len(results))
					##new editing
					#for result in results:
					#	for i in range(0,3):
					#		if result[i]==result[i+1]:
					#			if result[i+1]==result[i+2]:
					#				final_answer=result[i]
					#for result in results:
					#	if(result[]) 
					##new editing
					for result in results:
						if result!=None:
							final_answer+=str("\n")
							final_answer+=str("\n")
							final_answer+=str(result[0])
						#for answer in result:
							#final_answer+=str(answer)
							#return answer
					print(final_answer)
					return(final_answer)
					for answer in tupleReceivedList:
						print(answer[1])
						print(answer[0])



