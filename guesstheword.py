import random

# A list of words that should be randomized for the game
#The computer will choose one of these words to be guessed
potential_words = ["example", "words", "someone", "can", "guess"]

#Generating a random from the list of potential words
word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
#Make a "_" for every letter in the word that was generated from the list potential_words
#If the word is "dog" then the list should be "_","_","_"
current_word =("_ "*len(word)) # TIP: the number of letters should match the word

# Some useful variables
#guesses will be a list of strings
guesses = []
#This is the mx number of wrong guesses you can make before you lose
maxfails = 7
#This variable is where we keep track of how many times the user made a wrong guess
fails = 0
print(word)
#This is a while loop that will run as long as the number of times a user fails is less than the max number of times they can fail
while fails < maxfails:
    #Tells the user to guess a letter
    #Whatever the user types in will be my variable guess
	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)


	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")