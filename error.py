# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")
print ("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = 24 
age = int(age_Str) 
print(f"I'm {age} years old.")

    # Variables declaring additional years and printing the total years of age
    #logical error: 3 was in parenthese
years_from_now = 3
total_years = age + years_from_now
#logical error: "answer_years is not defined"
print ("The total number of years:" + "answer_years")

# Variable to calculate the total number of months from the given number of years and printing the result
total = 27.5
total_months = total * 12
print (f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer