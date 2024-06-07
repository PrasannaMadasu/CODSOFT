import random
import re

def respond(input_text):
    input_text = input_text.lower()

    if re.search(r'\bhello\b', input_text):
        return random.choice(["Hi there! How can I help you today?", "Hello! What can I do for you?"])

    elif re.search(r'\bhow are you\b', input_text):
        return "I'm just a chatbot, but thanks for asking!"

    elif re.search(r'\b(?:goodbye|bye)\b', input_text):
        return random.choice(["Goodbye! Have a great day!", "See you later!"])

    elif re.search(r'\b(?:thank you|thanks)\b', input_text):
        return "You're welcome!"

    elif re.search(r'\b(?:help|assistance)\b', input_text):
        return "Sure, I'm here to help. What do you need assistance with?"

    elif re.search(r'\b(?:weather|forecast)\b', input_text):
        return "The weather today is sunny with a high of 25°C."

    elif re.search(r'\b(?:news|headlines)\b', input_text):
        return "Here are the latest news headlines..."

    elif re.search(r'\b(?:joke|funny)\b', input_text):
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif re.search(r'\b(?:music|song)\b', input_text):
        return "I love music! What's your favorite genre?"

    elif re.search(r'\b(?:age|old)\b', input_text):
        return "I'm a chatbot, so I don't have an age. But I'm here to assist you!"

    elif re.search(r'\b(?:movie|film)\b', input_text):
        return "What kind of movies do you enjoy watching?"

    else:
        return "I'm sorry, I didn't understand that."

def chat():
    print("Welcome to the interactive chatbot!")
    print("You can start chatting. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
