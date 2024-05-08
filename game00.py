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

    guess = 

