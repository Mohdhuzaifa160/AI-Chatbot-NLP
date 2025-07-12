import nltk
from nltk.chat.util import Chat, reflections

# Define conversation pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I’m a simple CodTech NLP chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm doing great! Thanks for asking."]
    ],
    [
        r"(.*) your name ?",
        ["I’m called CodBot 😊"]
    ],
    [
        r"(.*) (help|support)",
        ["Sure, I'm here to help. Please tell me your query."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day! 👋"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn’t understand that. Can you rephrase?"]
    ]
]

# Initialize and start chatbot
print("🤖 CodTech Chatbot: Type 'quit' to exit")
chatbot = Chat(pairs, reflections)
chatbot.converse()
