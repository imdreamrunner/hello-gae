"""
       Once there is a boy and an Apple Tree.

        Title: Apple Tree
  Description: A simple hangman game written in Python.
       Author: Zhou Xinzi (FS2)
"""

# You can edit the words dictionary here.
word_dic = {
        "FRUIT":   ["APPLE", "BANANA", "PEACH", "ORANGE", "WATERMELON"],
        "COUNTRY": ["SINGAPORE", "CHINA", "JAPAN", "INDONESIA", "ENGLAND"],
        "VEGETABLE": ["POTATO", "CAPSICUM", "BEETROOT", "CABBAGE", "CARROT"],
        "SNACK": ["MINT", "CRACKER", "BISCUIT", "BONBON", "PUDDING"]
    }


import random


class Game(object):
    def __init__(self, arg):
        self.chance = 9
        self.word = None
        self.correct_letters = []
        self.wrong_letters = []
        self.message = None
        if len(arg) == 4:
            self.chance = arg[0]
            self.word = arg[1]
            self.correct_letters = arg[2]
            self.wrong_letters = arg[3]

    def get_states(self):
        return [self.chance, self.word, self.correct_letters, self.wrong_letters]

    def get_output(self):
        if self.message is not None:
            return self.message
        if self.word is None:
            self.print_word_list()
            return self.message
        else:
            return "your word is " + self.word

    def set_input(self, input_string):
        print "set_input"
        if self.word is None:
            self.choose_word(input_string)
        else:
            print "set input here"
            self.guess_letter(input_string)

    def choose_word(self, input_string):
        topic_list = list(word_dic.keys())
        try:
            choice = int(input_string)
        except ValueError:
            self.print_word_list()
            self.message += "  - Sorry, please enter the number before the topic you would like to choose."
            return
        self.message = ""
        if 0 < choice <= len(word_dic):
            # If user's input makes sense, start the game.
            # Otherwise, do nothing and the program will ask for input again
            self.word = random.choice(word_dic[topic_list[choice - 1]])
            self.message += "  - The story begins...\n"
            self.message += "  - Now you are to guess a word about {}."\
                            .format(topic_list[choice - 1]) + "\n\n"
            self.print_tree()
        else:
            self.print_word_list()
            self.message += "  - Sorry, please enter the number before the topic you would like to choose."

    def guess_letter(self, input_string):
        letter = None
        if len(input_string) > 0:
            letter = input_string[0]
        if letter is None or not letter.isalpha():
            self.print_tree()
            self.message += "  - Sorry, please enter a letter.\n"
            return
        letter = letter.upper()
        self.trial(letter)

    def trial(self, letter):
        if letter in self.correct_letters or letter in self.wrong_letters:
            self.print_tree()
            self.message += "  - You have already tried letter " + letter + ".\n"
            return
        if letter in self.word:
            self.correct_letters.append(letter)
            if self.check_status():
                self.print_result(True)
                return
            self.print_tree()
            self.message += "  - You have enter " + letter + ".\n"
            self.message += "  - Congratulation!" + "\n"
        else:
            self.wrong_letters.append(letter)
            self.chance -= 1
            if self.chance == 0:
                self.print_result(False)
                return
            self.print_tree()
            self.message += "  - You have enter " + letter + ".\n"
            self.message += "  - Guess fails :(" + "\n"

    def check_status(self):
        """
        Returns: <boolean> whether the user successfully guesses all the letters.
        """
        # Assume the user has guessed all the letters.
        all_guessed = True

        for currentLetter in self.word:
            if not (currentLetter in self.correct_letters):
                # If there is letter still to be guessed, set return value to be False.
                all_guessed = False

        return all_guessed

    def print_result(self, is_win):
        """
        Displays whether the user wins or loses.
        Arguments: <integer> chance: the number of chance(s) user still has.
                   <boolean> isWin: True if the user wins.
        """
        self.message = ""
        self.message += "*" * 50 + "\n"
        self.message += "*  {} {:^28}  *".format(self.get_line(0), " ") + "\n"
        self.message += "*  {} {:^28}  *".format(self.get_line(1), " ") + "\n"
        self.message += "*  {} {:^28}  *".format(self.get_line(2), " ") + "\n"
        if is_win:
            self.message += "*  {} {:^28}  *".format(self.get_line(3), "You WIN!!!") + "\n"
        else:
            self.message += "*  {} {:^28}  *".format(self.get_line(3), "You LOSE.") + "\n"
        self.message += "*  {} {:^28}  *".format(self.get_line(4), " ") + "\n"
        self.message += "*  {} {:^28}  *".format(self.get_line(5), "The word is " + self.word) + "\n"
        self.message += "*  {} {:^28}  *".format(self.get_line(6), " ") + "\n"
        self.message += "*  {} {:^28}  *".format(self.get_line(7), " ") + "\n"
        self.message += "*" * 50 + "\n"

        # restart
        self.print_word_list()
        self.word = None
        self.correct_letters = []
        self.wrong_letters = []
        self.chance = 9

    def print_word_list(self):
        if self.message is None:
            self.message = ""
        topic_list = list(word_dic.keys())

        # welcome message
        self.message += "=" * 50 + "\n"
        self.message += ">>>{:^44}<<<".format("Welcome to AppleTree") + "\n"
        self.message += "=" * 50 + "\n"

        self.message += "  Please choose a topic by entering its number:\n"
        for index, topic in enumerate(topic_list):
            self.message += "{:>6d}: {}".format((index + 1), topic) + "\n"
        self.message += "\n"

    def get_line(self, line):
        """
        Makes the strings which will become the "apple tree".
        Arguments: <integer> number: the number of apples in the
                   <integer> line: which line to be return.
        Returns: <string> a line of an apple tree made of characters.
        """
        number = self.chance
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

    def get_word(self):
        """
        Returns: <string> the word with "_" and letters user has guessed.
        """

        # Initialize a blank list to store all letters to be printed.
        print_list = []

        for currentLetter in self.word:
            # Add each letter (or "_" if not guessed) to the list.
            if currentLetter in self.correct_letters:
                print_list.append(currentLetter)
            else:
                print_list.append("_")

        # Convert the list to a string and then print it.
        return " ".join(print_list)

    def get_wrong_letter(self):
        """
        Returns: <string> all incorrect guesses.
        """
        return " ".join(self.wrong_letters)

    def print_tree(self):
        """
        Displays the number of chances the user has, the word to be guessed and those incorrect guesses.
        Arguments: <integer> chance: the number of chance(s) user still has.
        """
        self.message = ""
        self.message += " " + "-" * 48 + "\n"
        self.message += "|  {} {:^28}  |".format(self.get_line(0), " ") + "\n"
        self.message += "|  {} {:^28}  |".format(self.get_line(1), " ") + "\n"
        # Decide whether to use "chances" or "chance" by checking whether variable chance is greater than one.
        if self.chance > 1:
            self.message += "|  {} {:^28}  |"\
                .format(self.get_line(2), "You have " + str(self.chance) + " chances") + "\n"
        else:
            self.message += "|  {} {:^28}  |"\
                .format(self.get_line(2), "You have " + str(self.chance) + " chance") + "\n"
        self.message += "|  {} {:^28}  |".format(self.get_line(3), " ") + "\n"
        self.message += "|  {} {:^28}  |".format(self.get_line(4), self.get_word()) + "\n"
        self.message += "|  {} {:^28}  |".format(self.get_line(5), " ") + "\n"
        self.message += "|  {} {:^28}  |".format(self.get_line(6), "Miss: " + self.get_wrong_letter()) + "\n"
        self.message += "|  {} {:^28}  |".format(self.get_line(7), " ") + "\n"
        self.message += " " + "-" * 48 + "\n"
