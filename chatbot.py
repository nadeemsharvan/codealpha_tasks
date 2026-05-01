def reply(msg):
    msg = msg.lower()
    if msg == 'hello':
        return 'Hi!'
    elif msg == 'how are you':
        return "I'm fine, thanks!"
    elif msg == 'bye':
        return 'Goodbye!'
    else:
        return "I don't understand that."

print('=== Basic Chatbot ===')
print("Type 'bye' to exit")

while True:
    user = input('You: ')
    bot = reply(user)
    print('Bot:', bot)
    if user.lower() == 'bye':
        break
