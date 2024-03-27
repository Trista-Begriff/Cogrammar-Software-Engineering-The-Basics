total_entered = 0
repeats_count = 0
while True:  # Starts while loop.
   user_input = input("Please enter a number: ")
   try: float(user_input)  # Ensures input is float.
   except: print("This is not a valid input, try again.") ; continue
   if user_input == "-1":
      break  # Moves to final print statement, skipping total_entered, so the final -1 is not included.
   total_entered += float(user_input)  # Adds input to previous inputs. 
   repeats_count += 1
try: total_entered = total_entered / repeats_count ; print(f"Mean average of entered numbers: {total_entered}")
except(ZeroDivisionError): print("You guessed in one try!")  # Catches error from if -1 is entered immediately.