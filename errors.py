# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  # Syntax Error encountered due to lack of brackets enclosing the print statement.
print ("\n")  # Syntax error encountered due to incorrect indentation. Another due to unbracketed print statement.

# Variables declaring the user's age, casting the str to an int, and printing the result.
age_str = "24"  # Syntax error (indentation error) due to unnecessary indent fixed for lines 8-15)
# Second syntax error due to identity operator '==' used instead of assignment operator '='.
# Snake casing also has not been used correctly in 'age_Str'
age = int(age_str)  # Syntax error as age_Str cannot be converted to an int whilst it contains letters.
print("I'm " + str(age) + " years old.")  # Syntax error (type error) as cannot concatenate age with the strings whilst it's an int.
# Small logical error too as the strings would not have spacing between them as originally written.
# Variables declaring additional years and printing the total years of age.
years_from_now = "3"
total_years = age + int(years_from_now)  # Syntax error (type error) as a string and an int cannot be concatenated.

print ("The total number of years: " + str(total_years))  # Syntax error: unbracketed print statement.
# Second syntax error: used undefined variable "answer_years" instead of "total_years"
# Logical error. printed the string "total years" instead of a string of the variable total_years.
# Small logical error, as a space was pronbably intended after the colon in the printed statement.
# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12  #  Syntax error. undefined variable 'total' was called instead of total_years.
print ("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")  # Syntax error: unbracketed print statement.
# Second syntax error (a type error). total_months is an int and myst be converted to a str to concatenate here. 
# Logical error. The original code has ommitted to add the extra six months to the final print statement value.
#HINT, 330 months is the correct answer

