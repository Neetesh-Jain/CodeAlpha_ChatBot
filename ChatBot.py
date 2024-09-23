import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK resources (if you haven't done it before)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?", "Hi %1! What can I do for you?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you!", "You can call me Chatbot."]
    ],
    [
        r"how are you?",
        ["I'm just a program, but thanks for asking!", "I'm here to help you!"]
    ],
    [
        r"what can you do?",
        ["I can assist you with various queries. What do you need help with?", "I'm here to answer your questions and provide assistance."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "I told my computer I needed a break, and now it won't stop sending me beach wallpapers!"]
    ],
    [
        r"bye|exit",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Glad to help!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you please rephrase that?", "Could you clarify your question?"]
    ]
]

# Suggestions based on responses
suggestions = {
    "Hello! How can I assist you?": ["Can you tell me a joke?", "What can you do?"],
    "Hi there! What can I do for you?": ["Tell me about yourself.", "What is your name?"],
    "I'm just a program, but thanks for asking!": ["That's okay, I just wanted to check in.", "What can you help me with?"],
    "I can assist you with various queries. What do you need help with?": ["Can you help me with programming?", "What's your favorite color?"],
    "Why don't scientists trust atoms? Because they make up everything!": ["That's funny! Do you have another one?", "Can you tell me something else?"],
    "Goodbye! Have a great day!": ["See you soon!", "Take care!"],
    "You're welcome!": ["Can you help me with something else?", "That's great! Thanks again!"],
    "I'm not sure I understand. Can you please rephrase that?": ["Let me try again.", "Okay, I will rephrase my question."]
}

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Main chatbot loop
def chatbot_loop():
    print("Chatbot: Hi, how can I assist you? (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print("Chatbot:", chatbot.respond(user_input))
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        
        # Print suggestions for user replies
        if response in suggestions:
            print("Suggestions:", ", ".join(suggestions[response]))

# Run the chatbot
if __name__ == "__main__":
    chatbot_loop()
