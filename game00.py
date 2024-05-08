import random

# list of bollywood movies
movies = ['dilwaale dulhaniya le jayenge' , 'Dhoom' , 'kabhi khushi kabhi gham' , 'Lagaan']

# choose a random movie from the list 
movie_to_guess = random.choice(movies)
word_length = len(movie_to_guess)
display = ['_'] * word_length
guessed_letters = []
remaining_lives = 6

print("welcome to Hangman game! let's play with Bollywood movies.")
print(f"The movie title has {word_length} letters.")

while True:
    print(f"\nLives remaining {remaining_lives}")
    print(' '.join(display))

    if '_' not in display:
        print(f"congratulations! you guessed the movie '{movie_to_guess}'.")
        break

    if remaining_lives == 0:
        print(f"Game Over! The movies was '{movie_to_guess}'.")
        break

    guess = input("Guess a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in movie_to_guess.upper():
        indices = [i for i, letter in enumerate(movie_to_guess.upper()) if letter == guess]
        for index in indices:
            display[index] = movie_to_guess[index]
    else:
        remaining_lives -= 1
        print(f"'{guess}' is not in the movie title.")

