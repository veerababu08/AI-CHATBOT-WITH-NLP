from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('FreeBirdsBot')

trainer = ListTrainer(chatbot)

# Train the chatbot with some example conversations
trainer.train([
    'Hi',
    'Hello',
    'How are you?',
    'I am fine, and you?',
    'Great',
    'What are you doing?',
    'Nothing, just roaming around.'
])

# Keep chatting until user exits
print("Type 'exit' to stop chatting\n")
while True:
    input_data = input("You: ")
    if input_data.lower() == "exit":
        print("FreeBirdsBot: Goodbye! 👋")
        break
    response = chatbot.get_response(input_data)
    print("FreeBirdsBot:", response)
