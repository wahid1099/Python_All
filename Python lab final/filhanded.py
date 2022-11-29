file = open('words.dat', 'w+')
word = ''
while True:
    word = input('Enter a word (enter Nothing to quit): ')
    if not word:
        break
    file.write(word + '\n')
