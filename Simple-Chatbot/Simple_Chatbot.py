welcome_msg = 'Hello! Welcome to my chatbot.'
replies = "You can say 'hello', 'how are you', or 'bye'."

def overview():
    print('\n=== Simple Chatbot ===')
    print('Chatbot: ',welcome_msg)
    print('Chatbot: ',replies)

def chatbot(msg):
        if msg == 'hello':
            print('Chatbot: Hi!')
        elif msg == 'how are you':
            print("Chatbot: I'm fine, thanks!")
        elif msg == 'bye':
            print('Chatbot: Goodbye!')
        else:
            print("Chatbot: Sorry, I don't understand.")

overview()

while True:
     msg = input('\nYou: ').lower().strip()
     chatbot(msg)
     if msg == 'bye':
          break 
              
