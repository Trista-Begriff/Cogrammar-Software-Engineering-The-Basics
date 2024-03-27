# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "lion"  # Syntax error. 'Lion' needs to be a string. 
# Also a small logical error, as capitalising the L in 'lion yields an ungrammatical sentence at line 12.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  # Logical error: number_of_teeth and animal_type have to be transposed.
# Also, Logical error. the string above needs to be a formatted string to outpit the values assigned in lines 5-7
print(full_spec)  # Syntax error. Print statement was unbracketed.

