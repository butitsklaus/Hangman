import random

HANGMAN_ASCII_ART = """
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/
"""
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar ' \
        'coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk ' \
        'lion lizard llama mole monkey moose mouse mule newt otter owl panda ' \
        'parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep ' \
        'skunk sloth snake spider stork swan tiger toad trout turkey turtle ' \
        'weasel whale wolf wombat zebra'.split()
hints = {3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:4,10:4}

print(HANGMAN_ASCII_ART)
print("\nTotal Chances = 7")
life = 7
print("____"*50)
chances = 0
right = 0
def Hangman():
    word = random.choice(words)
    print("GUESS THE WORD BELOW:")
    word1 = list(word)
    spaces = ["_"]*len(word1)
    length = len(word1)
    if length in hints:
        done = []
        extra = 0
        removable = []
        while True:
            ra = random.randint(0,length-1)
            if ra not in done:
                done.append(ra)
                spaces[ra] = word1[ra]
                removable.append(ra)
                extra += 1
                if extra == hints[length]:
                    break
    word2 = []
    for i, value in enumerate(word1):
        if i in removable:
            continue
        else:
            word2.append(value)
    # print(word2)

    chances, right = 0, hints[length]
    tries = 1
    while True:
        flag = 0
        print(*spaces)
        guess = str(input("> "))
        if guess in word2:
            count_of_letter = word2.count(guess)
            l = 0

            for i,value in enumerate(word):
                if value == guess:
                    if spaces[i] == "_":
                        spaces[i] = guess
                        right += 1
                    if right == length:
                        print()
                        print(*spaces)
                        print(f"You did it in {tries} tries, it was `{word}`")
                        flag = 1
            if flag == 1:
                break
            word2.remove(guess)
        else:
            print(HANGMANPICS[chances])
            chances += 1
            if chances == 7:
                print(f"You lost, It was {word}")
                break
            print(f"Remaining lives = {life-chances}")
        print("___"*50)
        tries += 1


Hangman()