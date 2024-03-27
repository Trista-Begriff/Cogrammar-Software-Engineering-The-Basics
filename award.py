# store the racer's name in "name" variable to use in later outputs
name = input("please enter participant's name: ")

# store racer's swimming time as "swimming" variable and convert to int
# use while loop and try-except to catch errors
swim_valid = False
while swim_valid == False:
    try:
        swimming = input(f"please enter {name}'s swimming time in minutes: ")
        swimming = int(swimming)
        swim_valid = True
    except:
        print(f"Please enter {name}'s swimming time as an integer: ")

# store racer's cyclinging time as "cycling" variable and convert to int
# use while loop and try-except to catch errors
cycle_valid = False
while cycle_valid == False:
    try:
        cycling = input(f"please enter {name}'s cycling time in minutes: ")
        cycling = int(cycling)
        cycle_valid = True
    except:
        print(f"Please enter {name}'s cycling time as an integer: ")

# store racer's running time as "running" variable and convert to int
# use while loop and try-except to catch errors
run_valid = False
while run_valid == False:
    try:
        running = input(f"please enter {name}'s running time in minutes: ")
        running = int(running)
        run_valid = True
    except:
        print(f"Please enter {name}'s running time as an integer: ")

# store combined time for all three parts as "total" variable
total = swimming + cycling + running 
print(f"{name}'s total time to complete the triathalon was: {total} minutes.")

#output correct award using operators and if elif else statement
if total <= 100:
    print(f"{name} is awarded Provincial Colours.")
elif total <= 105 and total >= 101:
     print(f"{name} is awarded Provincial Half Colours.")
elif total <= 110 and total >= 106:
     print(f"{name} is awarded a Provincial Scroll.")
else:
    print(f"{name} recieves no award.")
