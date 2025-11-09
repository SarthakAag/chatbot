# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bunch of Python code, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm PyBot, your friendly chatbot assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure I understand. Could you rephrase that?"

def chat():
    print("PyBot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("PyBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("PyBot:", response)

if __name__ == "__main__":
    chat()

