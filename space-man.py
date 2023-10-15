import random

#welcome the user
name = input("What is your name? ")
print("Hello, " + name, "Time to play!")
print("Start guessing...")

#select any word to play with
words = ['swoon', 'charm', 'gentleman', 'swoop', 'alarm']
word = random.choice(words)

guesses = ''

#determine the number of turns
turns = 10

#create a loop

#check if the turns are more than zero
while turns > 0:

    failed = 0

    for char in word:

        #see if the character is in the players guess
        if char in guesses:
            
            #print then out the character
            print (char,end=""),
        else:
            print("_",end="")
            failed += 1


    if failed == 0:
        print("You Won!")
        print("The word is:", word)
        break

#ask the user go guess a character
guess = input("guess a character")

#set the players guess to guesses
guesses += guess

#if the guess is not found in the secret word
if guess not in word:

    #turns counter decreases with 1 (now 9)
    turns -= 1

    print ("Wrong")

    #how many turns are left
    print("You have", + turns, 'more guesses')

    if turns == 0:

        print("You Lose")
