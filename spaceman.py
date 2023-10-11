import random
# library that we use in order to choose on random words from a list of words

name = input("What is your name?")
print("Good Luck!", name)

words = ['swoon', 'charm', 'gentleman', 'swoop', 'alarm']
# function will choose one random word from the list of words
word = random.choice(words)

print ("Guess the letters")

guesses = ''
# any number of guesses can be done here
turns = 12

