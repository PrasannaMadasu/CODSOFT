import random
import re

class RuleBot:
    negative_responses = ("no", "nope", "not a chance", "sorry", "nay", "nothing")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell")

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\s*product.*',
            'technical_support': r'.*technical.*support.*',
            'about_returns': r'.*return policy.*',
            'general_query': r'.*how can i help.*',
        }

    def greet(self):
        self.name = input("Welcome! I'm here to assist you. May I know your name?\n")
        will_help = input(f"Hi {self.name}, how can I assist you today?\n")
        if will_help.lower() in self.negative_responses:
            print("RuleBot: Alright, have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("RuleBot: Thank you for reaching out. Have a wonderful day!")
                return True
        return False

    def chat(self):
        reply = input("Please tell me your query: ").lower()
        while not self.make_exit(reply):
            reply = input("RuleBot: " + self.match_reply(reply) + "\n")

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == 'ask_about_product':
                return self.ask_about_product()
            elif found_match and intent == 'technical_support':
                return self.technical_support()
            elif found_match and intent == 'about_returns':
                return self.about_returns()
            elif found_match and intent == 'general_query':
                return self.general_query()
        return self.respond(reply)

    def ask_about_product(self):
        responses = [
            "Our products are of high quality and have received great feedback from customers.",
            "You can explore our range of products on our website."
        ]
        return random.choice(responses)

    def technical_support(self):
        responses = [
            "Please visit our technical support page on our website for detailed assistance.",
            "You can also reach out to our technical support team via email or phone."
        ]
        return random.choice(responses)

    def about_returns(self):
        responses = [
            "We have a hassle-free 30-day return policy for our products.",
            "If you're not satisfied with your purchase, you can return it within 30 days."
        ]
        return random.choice(responses)

    def general_query(self):
        responses = [
            "Is there anything else I can help you with?",
            "How else may I assist you today?"
        ]
        return random.choice(responses)

    def respond(self, input_text):
        responses = [
            (r'\bhello\b', ["Hi there! How can I help you today?", "Hello! What can I do for you?"]),
            (r'\bhow are you\b', ["I'm just a chatbot, but thanks for asking!"]),
            (r'\b(?:goodbye|bye)\b', ["Goodbye! Have a great day!", "See you later!"]),
            (r'\b(?:thank you|thanks)\b', ["You're welcome!"]),
            (r'\b(?:help|assistance)\b', ["Sure, I'm here to help. What do you need assistance with?"]),
            (r'\b(?:weather|forecast)\b', ["The weather today is sunny with a high of 25°C."]),
            (r'\b(?:news|headlines)\b', ["Here are the latest news headlines..."]),
            (r'\b(?:joke|funny)\b', ["Why don't scientists trust atoms? Because they make up everything!"]),
            (r'\b(?:music|song)\b', ["I love music! What's your favorite genre?"]),
            (r'\b(?:age|old)\b', ["I'm a chatbot, so I don't have an age. But I'm here to assist you!"]),
            (r'\b(?:movie|film)\b', ["What kind of movies do you enjoy watching?"]),
        ]

        for pattern, response_list in responses:
            if re.search(pattern, input_text):
                return random.choice(response_list)
        return "I'm sorry, I didn't understand that."

    def no_match_intent(self):
        responses = [
            "I'm sorry, I didn't quite catch that. Could you please provide more details?",
            "Apologies, I couldn't understand your query. Can you rephrase it?"
        ]
        return random.choice(responses)

def chat():
    bot = RuleBot()
    bot.greet()

if __name__ == "__main__":
    chat()
