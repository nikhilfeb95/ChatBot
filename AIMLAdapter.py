import aiml
import sys

mybot = aiml.Kernel()
mybot.setBotPredicate("name","MediBot")
mybot.learn('disease.aiml')
while True:
	message = input("Ask me any question?")
	if message == "quit":
		exit()
	else:
		bot_response = mybot.respond(message.upper())
		if bot_response == "":
			print("error")
		else:
			print(bot_response)

		