#chatbot
def Chat(responses):
    reply = {
        'hi':'Hello my name is jarves !',
        'time': 'Current time is 12:12UTC',
        'feedback':'This is our feedback form',
        'good':'Thank you'
    }
    if responses in reply:
        print(reply[responses])
    else:
        print("Sorry I did not understand")
        
def greet():
    print("Hello My name is Jarvis, How can I help you?")
def by():
    print("Thank you for comming!")
    exit()

greet()
while True:
    
    userin = input('User : ')
    user_input = userin.lower()
    
    if user_input == 'by':
        by()
        break

    Chat(user_input)
        
