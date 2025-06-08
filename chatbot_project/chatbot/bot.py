import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

def get_response(text):
    text = text.lower().strip()

    if any(greet in text for greet in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]):
        return "I am doing very well, thank you for asking."
    elif "how are you" in text:
        return "I am doing very well, thank you for asking."
    elif text == "you're welcome" or text == "youre welcome":
        return "Do you like hats?"
    elif "thank you" in text or "thanks" in text:
        return "You're welcome."
    elif "do you like hats" in text:
        return "Yes, I think hats are quite stylish!"
    elif text == "exit":
        return "Goodbye!"
    else:
        return "That's interesting! Tell me more."

def main():
    print("Chatbot is ready! Type something (or 'exit' to quit):")
    while True:
        user_input = input("user: ")
        if user_input.lower() == "exit":
            print("bot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"bot: {response}")

if __name__ == "__main__":
    main()
