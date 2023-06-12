import random


class Chatbot:
    def __init__(self):
        self.greetings = ["Hi there!", "Welcome!", "How can I help you today?"]
        self.goodbyes = ["Have a nice day!", "Goodbye!", "See you later!"]
        self.responses = {
            "What is your name?": "My name is MyChatbot.",
            "What can you do?": "I can answer your questions about our products and services.",
            "How can I get a refund?": "You can request a refund by contacting our customer service department at 1-800-555-1212.",
            "I'm having trouble with my order": "I'm sorry to hear that. Please contact our customer service department at 1-800-555-1212 and they will be happy to help you.",
            "I'm interested in your product": "Great! I can tell you more about it.",
            "I'm not interested in your product": "That's okay. I hope you find something you like.",
        }

    def greet(self):
        greeting = random.choice(self.greetings)
        print(greeting)

    def goodbye(self):
        goodbye = random.choice(self.goodbyes)
        print(goodbye)

    def respond(self, message):
        if message in self.responses:
            print(self.responses[message])
        else:
            print("I'm not sure what you mean. Can you please rephrase your question?")


def main():
    chatbot = Chatbot()
    chatbot.greet()
    while True:
        message = input("\nWhat can I do for you?\n")
        if message == "goodbye":
            chatbot.goodbye()
            break
        chatbot.respond(message)


main()
