import pyjokes


def tell_some_jokes():
    while True:
      chatbot=input("Say something...")
      print(pyjokes.get_joke())


tell_some_jokes()
