import random

#welcome the user
name = input("What is your name? ")
print("Hello, " + name, "Time to play!")

#select any word to play with
word_list = ['swoon', 'charm', 'gentleman', 'swoop', 'alarm']

#code has to choose a word
def choose_random_word():
    return random.choice(word_list)

def play_game():
    word_to_guess = choose_random_word()
    guessed_letters = []
    #choose how many turns 
    attempts = 10

    while attempts > 0:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if set(guessed_letters) == set(word_to_guess):
                print(f"Congratulations! You guessed the word: (word_to_guess)")
                break
        else:
            print("Incorrect guess.")
            attempts -= 1
        
    if attempts == 0:
        print(f"Sorry, you're out of tries. The word was: (word_to_guess)")
if __name__ == "__main__":
    play_game()
    

