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


#Place holder for each blaks
place_holder = ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', '__8__', '__9__', '__10__']

#-----------------------------------------------------------
# welcome massage for user to play a game
def welcome_massage():
    print "Welcome to our fill_in_blank game!"

# request user to define the difficulty level of this game
def define_difficulty():
    request_user_difficulty = raw_input('Please select a game difficulty by typing it in! \nPossible choices include easy, medium, and hard.\n')
    if request_user_difficulty == 'easy' or request_user_difficulty == 'medium' or request_user_difficulty == 'hard': 
        return request_user_difficulty
    else:
        print 'Dear user your choise is invalid! Please try again!\n'
        return define_difficulty()

# define the correct answer of different difficulty
def get_correct_answer(difficulty):
    if difficulty == 'easy':
        return ['world', 'python', 'print', 'html']
    if difficulty == 'medium':
        return ['function', 'arguments', 'None', 'list']
    else:
        return ['answer1','answer2','answer3','answer4','answer5', 'answer6', 'answer7', 'answer8', 'answer9', 'answer10' ]
        
# give the user the start massage and rule to play
def start_game_massage(difficulty):
    print "You have choosen level " + difficulty + "!\nHere is the text for your game. Have fun :)\n" 

# give the user the appropriate text to play
def text_game(difficulty):
    if difficulty == 'easy':
        return easy
    if difficulty == 'medium':
        return medium
    else:
        return hard

# create a list from text_game
def list_of_text_game(text_for_game):
    assert (text_for_game != None), "No text for the game!"

    return text_for_game.split()

# check list_of_text_game and find blanks in this list
def find_blanks_in_list_of_game(list_of_text, place_holder_list, list_with_correct_answers):
    index_of_answer = 0
    for holder in place_holder_list:
        #print "\nlist of holder in place_holder_list: " + holder
        for words in list_of_text:
            #print "\nList of the words in List_of_text: " + words 
            if holder in words:
                #return holder
                #ask user to fill out the blanks
                answer= raw_input("\nPlease fill out " + holder+ " with the correct answer: ")
                if not check_answer_of_user(answer, list_with_correct_answers[index_of_answer]):
                    print "Dear user, your answer is wrong."
                    answer = try_again_for_answer(list_with_correct_answers[index_of_answer])  
                    if answer:
                        print "Success and now the next question :)"
                    else:
                        print "Game over!"
                        return False
                #print list_with_correct_answers
                #print index_of_answer
                break
        index_of_answer += 1
        #print index_of_answer
        print replace_the_correct_answer(list_of_text, place_holder_list, answer)
    return None

#compare the answer of user with the list of answers
def check_answer_of_user(user_response, correct_answer): 
    #print "User_response: " + user_response + " and correct answer: " + correct_answer
    return user_response == correct_answer

#give user more chance to give the right answer
def try_again_for_answer(correct_answer):
    index_of_false_answer = 0
    number_of_try = 3
    while index_of_false_answer < number_of_try:
        new_user_response = raw_input("\nPlease try again: ")
        if new_user_response == correct_answer:
            return new_user_response
        else:
            index_of_false_answer += 1
            print ('user try no. '+ str(index_of_false_answer))
        

def replace_the_correct_answer(list_of_text, list_of_place_holder, user_correct_response):
    replaced = []
    #index = 0
    for word in list_of_text:
        for holder in list_of_place_holder:
            if not holder in word:
                replaced.append(word)
            else:
                replaced.append(user_correct_response)
            break
    return " ".join(replaced)


    
        
            

        
    
 

def start_game():
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
    find_blanks_in_list_of_game(list_of_the_text, place_holder, correct_answer_for_difficulty)





start_game()