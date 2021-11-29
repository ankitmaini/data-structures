# So this a program to remove all the punctuation from a given sentence
def remove_punctuation(user_string,punc_list=None):
    # The function takes a string like "Let's go have some snacks!!!." and removes all the punctutation marks
    import string
    final_string = ""
    for char in user_string:
        if char in (string.ascii_letters+str(' ')):
            final_string += char
    
    return final_string+'.'
import time
print(time.time)
print(remove_punctuation("Let's go have some snacks!!!."))
print(time.time)

    
