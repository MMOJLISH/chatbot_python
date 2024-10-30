

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new ChatterBot instance
chatbot = ChatBot('chatbot', read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

# Define a list of conversations to train the bot
conversation = [
    "Hello! Raju is there we are having a project issues ",
    "Hi he is not here yet once he back we will  ask him to reach out to you  ",
    "we are missing some mgm points",
    "sure once raju back we wil lask him to assist   you"
    "thank you we appricate that ",
    "my pleasure anything else i can help you with ",
    "i m good for now ",
    "ali is not in the office today",
    "if ali is not here then i will call back ",
    "ok See you later!"
]

conversation_2 = [
    "hey  basir  you  there ?",
    "basir is busy with other work ",
    "ask basir to reach out to me",
    "once he back i will let him know "
    "What's your name?",
    "my name is mostofa , i m here to help you .",
    "i want to ali",
    "ali is not in the office today",
    "if ali is not here then i will call back ",
    "ok See you later!"
]

# Set up the ListTrainer
list_trainer = ListTrainer(chatbot)

list_trainer .train(conversation)
list_trainer .train(conversation_2)

# Train the bot with the defined list
#list_trainer.train(conversation)

# Main loop to chat with the bot
while True:
    user_response = input(":customer: ")
    if user_response.lower() == 'exit':
        print("Goodbye!")
        break
    print("chatbot: " + str(chatbot.get_response(user_response)))


