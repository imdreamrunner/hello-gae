"""
       Once there is a boy and an Apple Tree.

        Title: Apple Tree
  Description: A simple hangman game written in Python 3
       Author: Zhou Xinzi (FS2)
"""

# You can edit the words dictionary here.
word_dic = {
        "FRUIT":   ["APPLE", "BANANA", "PEACH", "ORANGE", "WATERMELON"],
        "COUNTRY": ["SINGAPORE", "CHINA", "JAPAN", "INDONESIA", "ENGLAND"],
        "VEGETABLE": ["POTATO", "CAPSICUM", "BEETROOT", "CABBAGE", "CARROT"],
        "SNACK": ["MINT", "CRACKER", "BISCUIT", "BONBON", "PUDDING"]
    }


import random, time


def chooseWord ():
    """
    Displays the welcome messages and the topics list,
             and ask user to choose a topic.
    Returns: <string> a random word from the topic user chooses.
    """

    topicList = list(word_dic.keys())

    # Print the welcome message.
    print("=" * 50)
    print(">>>{:^44}<<<".format("Welcome to AppleTree"))
    print("=" * 50)

    # Print the topic list.
    print("  Please choose a topic by entering its number:")
    for index, topic in enumerate(topicList):
        print ("{:>6d}: {}".format((index + 1), topic))
        # (index + 1) instead of index was printed because only programmers will count from zero :)

    # Keep asking user to choose a topic until a choice was made.
    while True:
        try:
            choice = int(input("  Your choice: "))
            if 0 < choice <= len(word_dic):
                # If user's input makes sense, start the game.
                # Otherwise, do nothing and the program will ask for input again
                print("  - The story begins...")
                print("  - Now you are to guess a word about {}.".format(topicList[choice - 1]))
                time.sleep(0.6)
                break
        except ValueError:
            # When the user input something other than digit,
            # simply so nothing and the program will ask for input again.
            pass

        # The following line will only be printed if there is an error.
        print("  - Sorry, please enter the number before the topic you would like to choose.")

    return random.choice(word_dic[topicList[choice - 1]])


def getWord ():
    """
    Returns: <string> the word with "_" and letters user has guessed.
    """

    # Initialize a blank list to store all letters to be printed.
    printList = []

    for currentLetter in word:
        # Add each letter (or "_" if not guessed) to the list.
        if currentLetter in correctLetters:
            printList.append(currentLetter)
        else:
            printList.append("_")

    # Convert the list to a string and then print it.
    return " ".join(printList)


def getWrongLetters ():
    """
    Returns: <string> all incorrect guesses.
    """
    return " ".join(wrongLetters)


def checkStatus ():
    """
    Returns: <boolean> whether the user successfully guesses all the letters.
    """
    # Assume the user has guessed all the letters.
    allGuessed = True

    for currentLetter in word:
        if not (currentLetter in correctLetters):
            # If there is letter still to be guessed, set return value to be False.
            allGuessed = False

    return allGuessed


def getLetter (chance):
    """
    Asks user to input her/his guess.
    Arguments: <integer> chance: the number of chance(s) user still has.
    Returns: <string> a letter that user guess.
    """

    while True:
        printBox(chance)

        # Get the user input and convert it to upper case.
        letter = input("  Your guess: ").upper()

        # If user input more than one character, the first character would be used. - Why? - Secret :)
        if len(letter) > 1:
            letter = letter[0]

        # Returns the letter if it is an English letter.
        if letter.isalpha():
            return letter

        print("  - Sorry, please enter a letter.")


def getLine (number, line):
    """
    Makes the strings which will become the "apple tree".
    Arguments: <integer> number: the number of apples in the 
               <integer> line: which line to be return.
    Returns: <string> a line of an apple tree made of characters.
    """
    pattern = {
        0: "_._",
        1: "/   \\",
        2: "/   {}   \\",
        3: "/  {} {} {}  \\",
        4: "/ {} {} {} {} {} \\",
        5: "\\___________/",
        6: "| |",
        7: "| |"
    }

    string = pattern[line]

    if line == 2:
        if number > 0:
            string = string.format("o")
        else:
            string = string.format("*")

    if line == 3:
        if number < 2:
            string = string.format("*", "*", "*")
        elif number == 2:
            string = string.format("o", "*", "*")
        elif number == 3:
            string = string.format("o", "o", "*")
        else:
            string = string.format("o", "o", "o")

    if line == 4:
        if number < 5:
            string = string.format("*", "*", "*", "*", "*")
        elif number == 5:
            string = string.format("*", "*", "*", "*", "o")
        elif number == 6:
            string = string.format("*", "*", "*", "o", "o")
        elif number == 7:
            string = string.format("*", "*", "o", "o", "o")
        elif number == 8:
            string = string.format("*", "o", "o", "o", "o")
        else:
            string = string.format("o", "o", "o", "o", "o")

    return "{:^15}".format(string)


def printBox (chance):
    """
    Displays the number of chances the user has, the word to be guessed and those incorrect guesses.
    Arguments: <integer> chance: the number of chance(s) user still has.
    """
    print()
    print(" " + "-" * 48)
    print("|  {} {:^28}  |".format(getLine(chance, 0), " "))
    print("|  {} {:^28}  |".format(getLine(chance, 1), " "))
    # Decide whether to use "chances" or "chance" by checking whether variable chance is greater than one.
    if chance > 1:
        print("|  {} {:^28}  |".format(getLine(chance, 2), "You have " + str(chance) + " chances"))
    else:
        print("|  {} {:^28}  |".format(getLine(chance, 2), "You have " + str(chance) + " chance"))
    print("|  {} {:^28}  |".format(getLine(chance, 3), " "))
    print("|  {} {:^28}  |".format(getLine(chance, 4), getWord()))
    print("|  {} {:^28}  |".format(getLine(chance, 5), " "))
    print("|  {} {:^28}  |".format(getLine(chance, 6), "Miss: " + getWrongLetters()))
    print("|  {} {:^28}  |".format(getLine(chance, 7), " "))
    print(" " + "-" * 48)


def printResult (chance, isWin):
    """
    Displays whether the user wins or loses.
    Arguments: <integer> chance: the number of chance(s) user still has.
               <boolean> isWin: True if the user wins.
    """
    print("*" * 50)
    print("*  {} {:^28}  *".format(getLine(chance, 0), " "))
    print("*  {} {:^28}  *".format(getLine(chance, 1), " "))
    print("*  {} {:^28}  *".format(getLine(chance, 2), " "))
    if isWin:
        print("*  {} {:^28}  *".format(getLine(chance, 3), "You WIN!!!"))
    else:
        print("*  {} {:^28}  *".format(getLine(chance, 3), "You LOSE."))
    print("*  {} {:^28}  *".format(getLine(chance, 4), " "))
    print("*  {} {:^28}  *".format(getLine(chance, 5), "The word is " + word))
    print("*  {} {:^28}  *".format(getLine(chance, 6), " "))
    print("*  {} {:^28}  *".format(getLine(chance, 7), " "))
    print("*" * 50)
    time.sleep(0.6)


def trial (chance):
    """
    Asks user for a guess by calling function getLetter, and then display whether the guess is correct or not.
    Arguments: <integer> chance: the number of chance(s) user still has.
    Returns: <boolean> True if the user guesses correctly or the letter has been tried.
                       False if user guesses incorrectly.
                       If the return value is False, user's chance will minus one.
    """
    letter = getLetter(chance)

    if letter in wrongLetters or letter in correctLetters:
        print("  - You have already tried letter " + letter)
        time.sleep(0.6)
        return True

    if letter in word:
        correctLetters.append(letter)
        print("  - Congratulation!")
        time.sleep(0.4)
        return True
    else:
        wrongLetters.append(letter)
        print("  - Guess fails :(")
        time.sleep(0.4)
        return False


def play ():
    """
    This is the whole game loop.
    Returns: <boolean> True if user choose to play next round.
    """
    global word, correctLetters, wrongLetters, word_dic

    word = chooseWord()

    # Initializes other global variables.
    correctLetters = []
    wrongLetters = []
    currentStatus = False

    for chance in range(9, -1, -1):
        if chance == 0:
            printResult(chance, False)
            break

        while trial(chance):
            currentStatus = checkStatus()
            if currentStatus:
                break

        if currentStatus:
            printResult(chance, True)
            break

    # Ask user to decide whether to start again.
    print("  Do you want to start a new journey?")
    print("  - Enter Y for yes, or press enter to leave.")
    restartString = input("  Your choice: ")
    if restartString.upper() == "Y":
        # Leave the game if user input anything other than "y" or "Y".
        return True
    else:
        return False


def main ():
    """
    This is the function will be called once the program runs.
    """

    # Keep calling the game loop until the user leave the game.
    while play():
        pass
    else:
        print("  - See you :)")


main()
