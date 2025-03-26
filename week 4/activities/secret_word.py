"""
    this is a game where a scret word is store in a variable and the user has to guess it
    
"""

secret_word = "Lucky"
guessed_word=""
number_of_guesses = 0
length_of_scret_word = len(secret_word)
under_score = '_ ' *length_of_scret_word

#using while loop to compare entered word
while guessed_word != secret_word:
        guessed_word = input(f"Guess the word {under_score}")
        number_of_guesses +=1
        if guessed_word != secret_word:
                print(f"guessed word {guessed_word} is incorrect")
                
print(f"{guessed_word} is correct and you guessed {number_of_guesses} times")
