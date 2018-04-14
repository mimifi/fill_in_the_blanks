# check list_of_text_game and find blanks in this list
def find_blanks_in_list_of_game(list_of_text, place_holder_list):
    # Loop over text (A)
    for text_word in list_of_text:
        print "Loop Text Word: " + text_word
        # Loop over placeholder list
        # placeholder word != word for A 
        for place_holder_word in place_holder_list:
            print "Loop Placeholderword " + place_holder_word
            # check if the placeholder_word (__1__) is in word (A) (false)
            if place_holder_word in text_word:
                print "placeholderword is in list_of_text: " + place_holder_word            
                # Ask the user and instead of return save all answers in a list                            
                return raw_input("Please answer the correct question " + place_holder_word + ": ")
    # Return None only if all placeholder words are not contained in the words of
    return None