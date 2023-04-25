from termcolor import colored
from collection import getWordsCollection
import os
import random

randomWord = random.choice(getWordsCollection(1))

WORD = randomWord
canTry = True
attempts = 6
win = False
guesses = []

while(canTry and attempts > 0):
    guess = input()
    if guess not in getWordsCollection():
        print('Palavra inválida! Tente novamente:')
        continue

    coloredGuess = ''
    os.system('cls' if os.name == 'nt' else 'clear')

    for i,letter in enumerate(guess):
        if letter == WORD[i]:
            coloredGuess += colored(letter, "green")
        elif letter in WORD:
            if colored(letter, "yellow") not in coloredGuess and colored(letter, "green") not in coloredGuess and WORD.count(letter) > 1:
                coloredGuess += colored(letter, "yellow")
            else:
                coloredGuess += letter
        else:
            coloredGuess += letter

    guesses.append(coloredGuess)

    for temp in guesses:
        print(temp)

    if guess == WORD:
        canTry = False
        win = True
    else:
        attempts -= 1


print(f'\nA palavra era {WORD}!\n')

print('Venceu!!!' if win else 'Perdeu!')