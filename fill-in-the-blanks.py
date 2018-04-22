# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

easy = '''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.'''

medium = '''A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.'''

hard = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?


# Place holder for each blaks
place_holder = ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', '__8__', '__9__', '__10__']


# -----------------------------------------------------------
def welcome_massage():
    """
    1. Give user welcome massage to play a game
    2. Inputs: -
    3. Outputs: -
    """
    print "Welcome to our fill_in_blank game!"


def define_difficulty():
    """
    1. Request user to define the difficulty level for a game
    2. Inputs: -
    3. Outputs: difficulty
    """
    request_user_difficulty = raw_input(
        'Please select a game difficulty by typing it in! \nPossible choices include easy, medium, and hard.\n')
    if request_user_difficulty in ("easy", "medium", "hard"):
        return request_user_difficulty
    else:
        print 'Dear user your choice is invalid! Please try again!\n'
        return define_difficulty()


def get_correct_answer(difficulty):
    """
    1. Define the correct answer for texts of different difficulty
    2. Inputs: difficulty
    3. Outputs: right answers of blanks for each level
    """
    if difficulty == 'easy':
        return ['world', 'python', 'print', 'html']
    if difficulty == 'medium':
        return ['function', 'arguments', 'None', 'list']
    else:
        return ['answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9',
                'answer10']


def start_game_massage(difficulty):
    """
   1. Give user the start massage and rules to play
   2. Inputs: difficulty
   3. Outputs: -
   """

    print "You have choose level " + difficulty + "!\nHere is the text for your game. Have fun :)\n"


def text_game(difficulty):
    """
   1. Give user the appropriate text to play
   2. Inputs: difficulty
   3. Outputs: text to play the appropriate level of game
   """
    if difficulty == 'easy':
        return easy
    if difficulty == 'medium':
        return medium
    else:
        return hard


def list_of_text_game(text_for_game):
    """
   1. Create a list from text of game
   2. Inputs:   #1 text_for_game - A text that contains blanks to play the game
   3. Outputs: A list with all words of text of the game
   """
    assert (text_for_game is not None), "No text for the game!"

    return text_for_game.split()


# check list_of_text_game and find blanks in this list
def find_blanks_in_list_of_game(list_of_text, place_holder_list, list_with_correct_answers):
    index_of_answer = 0
    for holder in place_holder_list:
        # print "\nlist of holder in place_holder_list: " + holder
        for words in list_of_text:
            # print "\nList of the words in List_of_text: " + words
            if holder in words:
                # return holder
                # ask user to fill out the blanks
                answer = raw_input("\nPlease fill out " + holder + " with the correct answer: ")
                correct_answer = list_with_correct_answers[index_of_answer]
                list_of_text = check_different_answers_of_user(list_of_text, holder, answer, correct_answer)
                if len(list_of_text) == 0:
                    return False
                break
        index_of_answer += 1
        # print index_of_answer
    return True


def check_different_answers_of_user(list_of_text, holder, new_answer, correct_answer):
    if not check_answer_of_user(new_answer, correct_answer):
        print "Dear user, your new_answer is wrong."
        new_answer = try_again_for_answer(correct_answer)
        if new_answer:
            # print "Success and now the next question :)"
            list_of_text = replace_the_correct_answer(list_of_text, holder, new_answer)
            print " ".join(list_of_text)
            return list_of_text
        else:
            return []
    else:
        list_of_text = replace_the_correct_answer(list_of_text, holder, new_answer)
        print " ".join(list_of_text)
        return list_of_text
        # print list_with_correct_answers
        # print index_of_answer


def check_answer_of_user(user_response, correct_answer):
    """
   1. Compare the answer of user with the list of right answers
   2. Inputs:   #1 user_response: the answer of user for each blanks
                #2 correct_answer: the correct answer for each blanks
   3. Outputs: Boolean - True if user's answer if as same as the correct answer and false if not.
   """
    # print "User_response: " + user_response + " and correct answer: " + correct_answer
    return user_response == correct_answer


def try_again_for_answer(correct_answer):
    """
   1. Give user more chance to try and give the right answer
   2. Inputs:  the correct answer for each blanks
   3. Outputs: new answer of user
   """
    index_of_false_answer = 0
    number_of_try = 3
    while index_of_false_answer < number_of_try:
        new_user_response = raw_input("\nPlease try again: ")
        if new_user_response == correct_answer:
            return new_user_response
        else:
            index_of_false_answer += 1
            print ('user try no. ' + str(index_of_false_answer))


def replace_the_correct_answer(list_of_text, holder, user_correct_response):
    """
   1. Replace the blanks with correct answers of user
   2. Inputs:   #1 list_of_text: The list of the text of the gae
                #2 holder: blanks of the text
                #3 user_correct_response: right answer of user
   3. Outputs: replace the blanks in text of game with answer of user
   """
    replaced = []
    # index = 0
    for word in list_of_text:
        if holder not in word:
            replaced.append(word)
        else:
            replaced.append(user_correct_response)
    return replaced


def congratulation_massage():
    """
    1. Replace the blanks with correct answers of user
    2. Inputs: -
    3. Outputs: -
    """
    return raw_input("\nDear user, congratulation! Do you like to play again? Y/N ")


def start_game():
    """
    1. Start the game to play
    2. Inputs: -
    3. Outputs: -
    """
    # Welcome to the user
    welcome_massage()

    # Get the difficulty from the user
    difficulty = define_difficulty()

    correct_answer_for_difficulty = get_correct_answer(difficulty)

    # Inform the user about the start and dificulty
    start_game_massage(difficulty)

    # Get the text for the dificulty
    text_for_game = text_game(difficulty)
    print text_for_game

    # Get the list out of the text
    list_of_the_text = list_of_text_game(text_for_game)

    # Ask the user questions till game over or win
    # Loop over list and give the method every single word
    result_of_game = find_blanks_in_list_of_game(list_of_the_text, place_holder, correct_answer_for_difficulty)

    # finish the game - congratulation massage to user
    if result_of_game:
        end_massage = congratulation_massage()
        if end_massage == "Y":
            start_game()
        else:
            return
    else:
        print "Game over!"


start_game()
