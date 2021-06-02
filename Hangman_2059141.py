#Coding challenge Hangman 3
# student name ; Anil panjiyar
#student number: 2059141
import random, pickle, pathlib

score_dict = {}
score = 0

WORDLIST_FILENAME = "words.txt"
SCORE_FILE = "scores3.txt"


def Load_words():
    # this function returns the value from the list words .
    # which is all in lowercase
    wordlist = []
    print("Loading word list from file...")
    # File: file to open for reading .
    File = open("C:\\Users\\Hp\\Downloads\\words.txt" ,'r')
    content = File.read()
    for i in content.split():
        wordlist.append(i)
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_random_word(wordlist):
# This function will returns random words from wordlist

    return random.choice(wordlist)

wordlist = Load_words()


def Is_word_guessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word that the user is attempting to guess
    lettersGuessed: list, to check  what letters have been guessed  till now
    which return boolean true if the letters of secretword are in lettergussed
    else it returns false
    '''
    c = 0
    for i in lettersGuessed:
        if i in secretWord:
            c += 1
    if c == len(secretWord):
        return True
    else:
        return False


def Get_guessed_word(secretWord, lettersGuessed):
    '''
    secretword = the word  user is guessing

    lettersGuessed= the letter user have gusssed and compaeres,
    and displays the underscore

    '''
    s = []
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans


def Get_remaining_letters(lettersGuessed):
    '''
    This function it tells the what letter has been guessed so far
    '''
    import string
    answer = list(string.ascii_lowercase)
    for i in lettersGuessed:
        answer.remove(i)
    return ''.join(answer)


def get_score(name):
    if pathlib.Path(SCORE_FILE).exists():
        with open(SCORE_FILE, 'rb') as file:
            score_dict = pickle.load(file)

            if name in score_dict:
                return score_dict[name]
            else:
                return 0
    else:
        print("SCORE FILE DOES NOT EXIST!")


def save_score(name, score):
    global score_dict
    score_dict[name] = score

    if pathlib.Path(SCORE_FILE).exists():
        with open(SCORE_FILE, 'rb') as file:
            dic = pickle.load(file)

        if dic[name] < score:
            option = input("A new Personal Best! Would you  like to  Save your  score? (y/n) ")
            if option.lower().startswith("y"):
                dic[name] = score
                with open(SCORE_FILE, 'wb') as file:
                    pickle.dump(dic, file)
                print("Ok, your score has been saved.")

            else:
                pass

        if dic[name] > score:
            pass

        else:
            pass


    else:
        print("Score file does not exist! Creating Now...")
        with open(SCORE_FILE, 'wb') as file:
            pickle.dump(score_dict, file)
        print("Score saved!")


def view_scores():
    if pathlib.Path(SCORE_FILE).exists():
        with open(SCORE_FILE, 'rb') as file:
            score_dict = pickle.load(file)

        for k, v in score_dict.items():
            print(f"{k}\t\t{v}")

    else:
        print("Score file does not exist!... You need to save a score first")


def hangman(secretWord):
    '''

    secretWord: the secret word the user will guess
    Starting ot the game
    1 First it is displayed the user that  numbers of letters secretwords contains
    2Asking user to enter the guessing lettere one at a time from availabel letters
    3 The user gets informed if their guess appears in the computer's word instantly after each guess
    4 Displaying the guessed the number by user also the displaying the letters not guessed by the user
    for every round


    '''
    print("Welcome to Hangman Ultimate Edition")
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    global lettersGuessed
    global score
    mistakeMade = 0
    lettersGuessed = []

    while 6 - mistakeMade > 0:

        if Is_word_guessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break

        else:
            print("-------------")
            print("You have", 6 - mistakeMade, "guesses left.")
            print("Available letters:", Get_remaining_letters(lettersGuessed))
            guess = str(input("Please guess a letter: ")).lower()

            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", Get_guessed_word(secretWord, lettersGuessed))

            elif guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                score += 2
                print("Good guess:", Get_guessed_word(secretWord, lettersGuessed))

            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:", Get_guessed_word(secretWord, lettersGuessed))

        if 6- mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.", secretWord)
            break

        else:
            continue


def welcome():
    print("Welcome to Hangman Ultimate Edition")
    while True:
        print("Do you want to Play (p) View the leaderboard (l) or quit (q): \n")
        choice = input()
        if choice == 'p':
            name = input("What is your name? ")
            secretWord = choose_random_word(wordlist).lower()
            hangman(secretWord)
            print("Your total score for this game is:", score)
            save_score(name, score)

        elif choice == 'l':

            print("Name\t\tScore")
            view_scores()


        elif choice == 'q':
            print("Thanks for playing, goodbye!")

            import sys
            sys.exit()

        else:
            print("Invalid choice!")

welcome()
if __name__ == "__main__":
    word = choose_random_word(wordlist)
    hangman(word)
#word = choose_random_word(all_words).lower()
#hangman(word)

