#python .\teach_chatbot.py
import json
import difflib
from typing import Optional  # Import Optional for compatibility

# Function defining loading json file
def load_chatbot_books_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data    

# Function to save the data in JSON files
def save_response_chatbot_books(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Function to get a close match from user response 
def get_close_match(user_questions: str, questions: list) -> Optional[str]:  # Updated here
    match = difflib.get_close_matches(user_questions, questions, n=1, cutoff=0.6)
    return match[0] if match else None

# Function to get a response for user questions
def get_ans_for_question(question: str, chatbot_books: dict) -> Optional[str]:  # Updated here
    for k in chatbot_books["questions"]:
        if k["question"] == question:
            return k["answer"]
    return None  # Explicitly return None if not found

# Defining function to call JSON files         
def chatbot():
    chatbot_books: dict = load_chatbot_books_file('chatbot_books.json')        

    while True:
        user_input = input("clients: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        
        best_match: Optional[str] = get_close_match(user_input, [k["question"] for k in chatbot_books["questions"]])

        if best_match:
            answer: Optional[str] = get_ans_for_question(best_match, chatbot_books)
            print(f"mostofa_bot: {answer} ")
        else: 
            print("I don't know the answer. Can you please teach me?")
            new_answer: str = input('Type your answer or "skip" to skip: ')
            if new_answer.lower() != 'skip':
                chatbot_books['questions'].append({"question": user_input, "answer": new_answer})
                save_response_chatbot_books('chatbot_books.json', chatbot_books)
                print("mostofa_bot: Thank you for being a good teacher!")

if __name__ == "__main__":
    chatbot()

#print("Hello, World!")
