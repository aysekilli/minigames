# hangman
import random

movies = []
try:
    with open("movie_names.txt", "r") as f:
        for line in f:
            movies.append(line.strip())
except FileNotFoundError:
    print("movie_names.txt not found. Creating a new file with movie names.")
    with open("movie_names.txt", "w") as f:
        f.write(
            "the matrix\nprestige\ninception\ninterstellar\nmemento\nthe dark knight\nfight club\npulp fiction\nthe godfather\nthe shawshank redemption\nforrest gump\n"
            "the lord of the rings\nthe empire strikes back\nstar wars\nharry potter and the sorcerer's stone\navengers: endgame\nback to the future\ntitanic\njurassic park\n"
            "the silence of the lambs\nschindler's list\nbraveheart\nthe social network\nla la land\nparasite\njoker\nmad max: fury road\nthe wolf of wall street\n")
    with open("movie_names.txt", "r") as f:
        for line in f:
            movies.append(line.strip())

while True:
    movie_answer = random.choice(movies).lower()

    spaces = movie_answer.split()
    move = ""
    for char in movie_answer:
        if char == " ":
            move += " "
        else:
            move += "_"

    count_guess = 0
    score = 0
    foundNums = 0
    foundLetters = []
    mistakes = []
    guess = "."
    found = 0
    print("Movie:")
    print(move)
    while foundNums <= len(movie_answer):

        guess = input(
            "Enter a letter please. \n(If you want to guess the movie,type '10'. If not enter a letter:):   ").lower()

        if guess not in ["a", "b", "c", "d", "e", "f", "g", "h", "j", "i", "j", "k", "l",
                         "m", "n", "o", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z", "x", "w", "q", "10"]:
            print("Guess should be a letter. Try again please.")
            print(move)
            continue
        if guess == '10':
            guess_movie = input("What is your guess?: ")
            if guess_movie == movie_answer:
                print("Congrats! You won the game!!!")
                play_again = int(input("Do you want to play again?  Please enter 1 for retry 0 for exit. :"))
                if play_again == 1:
                    continue
                elif play_again == 0:
                    exit()
            elif guess_movie != movie_answer:
                print("Oh no it's wrong, try again please.")
                print(move)
                count_guess += 1
                if count_guess == 3:
                    print("You should be careful. You have only 2 guesses left.")
                if count_guess == 5:
                    print("Oh no, you lost the game!")
                    print('Movie was', movie_answer)
                    play_again = int(input("Do you want to play again?  Please enter 1 for retry 0 for exit. :"))
                    if play_again == 1:
                        continue
                    elif play_again == 0:
                        quit()
                continue

        if guess not in movie_answer:
            if guess in mistakes:
                print("You already tried this letter.")
            mistakes.append(guess)
            print(guess, "is not in the answer.")
            print("Mistakes made:", len(mistakes), mistakes)
            print(move)

        if guess in movie_answer:
            found = movie_answer.find(guess)
            foundLetters.append(guess)
            foundNums += 1
            move = move[0:found] + guess + move[found + 1:]
            #  birden çok bulunanlar bu kısma gidiyo
            currentStrCounter = 0
            while guess in movie_answer[found + 1:]:

                rest = movie_answer[found + 1:]
                found = found + 1 + rest.find(guess)
                move = move[:found] + guess + move[found + 1:]
                currentStrCounter += 1
                if guess not in foundLetters:
                    foundLetters.append(guess)
                    foundNums += 1
                print(currentStrCounter)

            print("It's correct! You found:", guess.capitalize())
            print(move)

            print("Total found:", foundLetters)

        if len(mistakes) >= 5:
            print("Oh no! You made", 5, " mistakes and hanged the man!!")
            print('Movie was', movie_answer)
            play_again = int(input("Do you want to play again?  Please enter 1 for retry 0 for exit. :"))
            if play_again == 1:
                continue
            elif play_again == 0:
                quit()
        if move == movie_answer:
            print("You won the game with", len(mistakes), "mistakes!")
            play_again = int(input("Do you want to play again?\nPlease enter 1 for retry 0 for exit."))
            if play_again == 1:
                continue
            elif play_again == 0:
                exit()