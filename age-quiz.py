
# use while loop to repeat the code until a valid input is given
valid = False
while valid == False:
# use try to catch errors and repeat the while loop
    try:
# age = input "please enter your age as an integer"
        user_age = input("Please enter your age as an integer: ")
# if the user enters an age over 100, print " Sorry, you're dead."
        if int(user_age) > 100:
            print("Sorry, you're dead.")
            valid = True
# if the user is 65 or over print "enjoy your retirement"
        elif int(user_age) >= 65: 
            print("Enjoy your retirement.")
            valid = True
# if user is 40 or over, print "You're over the hill"
        elif int(user_age) >= 40:
            print("You're over the hill.")
            valid = True
# if the user is under 13 print "you qualify for the kiddie discount" 
        elif int(user_age) < 13:
            print("You qualify for the kiddie discount.")
            valid = True
# if the user is 21 print "Congrats on your 21st"
        elif int(user_age) == 21:
            print("Congrats on your 23rd")
            valid = True
# for any other age print "age is but a number"
        else:
            print("age is but a number")
            valid = True
    except:
        print("you did not enter an integer")
        