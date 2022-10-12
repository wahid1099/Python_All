"""
Chatbot
steps:
1.Input/listen
2.Process/decide
3.Output/talkback
"""
greet_words=['hi', 'hellp','yo','hey']

bye_words=['bye', 'tata','hasta_la_vista']

def listen():
    return input("Say something: ")


def decide(command):
   command=command.lower()
   browken_words=command.split(" ")

   for word in browken_words:
       if word in greet_words:
          talkback("he said greeting")
          break
       elif word in bye_words:
          talkback("He said bye")
          break

def talkback(response):
    print(response)



command=listen()
decide(command)
# print(command)