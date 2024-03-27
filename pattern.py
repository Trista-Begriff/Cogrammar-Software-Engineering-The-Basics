

asterisks_list = []
# The empty list we shall add the asterisks to.  


for i in range(0,9):
    if i <= 4:
        asterisks_list.append("*")
        print("".join(asterisks_list))
        # This joins the contents of asterisks_list into a string and prints.
    else:
        asterisks_list.remove("*")
        print("".join(asterisks_list))