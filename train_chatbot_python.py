import json
import difflib

class Learning_chatbot:  # learningchatbot class is defined to encapsulate all the functionality of the chatbot
    def __init__(self):
        self.conversation = {}  # To store learned responses
        pass

    def load_responses(self, filename='responses.json'):  # load existing responses from json file
        try:
            with open(filename, 'r') as file:
                self.conversation = json.load(file)
        except FileNotFoundError: 
            self.conversation = {}

    def save_response(self, filename='responses.json'):  # save current conversation to a json file
        with open(filename, 'w') as file:
            json.dump(self.conversation, file)

    def find_best_match(self, user_input):  # looking for best match in files
        responses = list(self.conversation.keys())
        best_match = difflib.get_close_matches(user_input, responses, n=1, cutoff=0.6)
        return best_match[0] if best_match else None

    def get_response(self, user_input):  # retrieve responses from user's input
        best_match = self.find_best_match(user_input)
        if best_match:
            return self.conversation[best_match]
        else:
            return "unable to find any best match at this moment"

    def learn_response_from_user(self, user_input, user_response):  # learn a new response from the user
        self.conversation[user_input] = user_response
        print("I have learned something new from user response... thank you so much")

#calling the class 

def main():
    bot = Learning_chatbot()
    bot.load_responses()  # calling methods 
    print("Hello, I'm a customer service automated AI chatbot. What would you like to talk about?")

    # continuous loop is initiated to keep the conversation going 
    while True:
        user_input = input("user: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        # user response passed to get the relevant reply also calling get_response function
        mostofa_response = bot.get_response(user_input)
        print(f"mostofa_chatbot: {mostofa_response}")

        # training the mostofa_bot to learn from user's input
        if mostofa_response == "unable to find any best match at this moment ":
            user_response = input("What should I say? ")
            while not user_response.strip():
                user_response=input("please enter a valid response")
            bot.learn_response_from_user(user_input, user_response)

    # Once the user decides to exit, the bot saves any new responses it has learned
    bot.save_response()

#This block checks if the script is being run directly (not imported as a module). If so, it calls the main() function to start the chatbot.
if __name__ == "__main__":
    main()

