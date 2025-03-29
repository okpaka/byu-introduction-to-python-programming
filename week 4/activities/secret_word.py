# """
# this is an example of a while loop
# """

# # initialize the variable
# Number = int(input("Enter a positive number: "))

# # check if the input is a not a negative number

# while Number < 0:
#     Number = input("Enter a positive number")
#     Number = int(Number)
# print("You entered a positive number ", Number)

def get_hint(secret_word, guess):
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:  # Correct letter and correct position
            hint += guess[i].upper()
        elif guess[i] in secret_word:  # Correct letter but wrong position
            hint += guess[i].lower()
        else:  # Letter not in the secret word
            hint += "_"
    return hint

def main():
    secret_word = "python"  # The secret word
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print(f"The secret word has {len(secret_word)} letters.")
    
    while not guessed_correctly:
        guess = input("Please enter your guess: ").strip()

        # Check if the guess has the same number of letters as the secret word
        if len(guess) != len(secret_word):
            print(f"Your guess must be {len(secret_word)} letters long.")
            continue

        attempts += 1

        if guess == secret_word:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the word '{secret_word}' in {attempts} attempts.")
        else:
            hint = get_hint(secret_word, guess)
            print(f"Hint: {hint}")

if __name__ == "__main__":
    main()