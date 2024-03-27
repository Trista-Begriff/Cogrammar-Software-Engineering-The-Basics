""" 
This is a programme that deliberately creates a logic error, 
Because input() creates a string, user inputs cannot directly be used for arithmetic. 
The user input is are erroneously converted to integers instead of a float, the quiz is thus impossible.
Strings are immutable, so attempting to convert a decimal string to an int gives a value error.
Because of the use of try/except, the code still compiles and runs.
This logic error creates a further user experience problem:
What is supposed to be a reassuring opportunity to retry the quiz becomes an infuriating inescapable loop.
The comments below are written from a perspective unaware of the error for realism. 
"""

while True:
    print("Welcome to my maths quiz! :)")
    print("Question One:")
    question_one = input("what is 3 divided by 2? ")        
    try: 
        if int(question_one) == 0.5:   #  question_one is converted to an int we can use == with a number.
            print("You got it correct!")
            break
        else:
            print("You got the answer wrong, but I believe in you, try again! :) ")
            # The user is given an opportunity to retry so they are not disheartened by failure!
            continue
    except:
        print("You got the answer wrong, but I believe in you, try again! :) ")
        continue      
    # try/except is used to prevent syntax errors from string inputs that cannot be converted to numbers.
   
    