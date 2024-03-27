#sets condition for the while loop
password_match = False
#creates the list for storing incorrect entries
mistake_list = []
#request input from user
#store input into variable called "password" 
password = input("please create a password: ")
# request second input from user and save to entry variable
while password_match == False:
    entry = input("please enter your password: ")
    if entry == password:
        #end the while loop
        password_match = True
        print("password correct: " + password)
        print ("incorrect entries: " + str(mistake_list))
    elif entry != password:
        #add incorrect password to mistake_list
        mistake_list.append(entry)
        print ("incorrect entries: " + str(mistake_list))
        print("password incorrect, please try again")
        