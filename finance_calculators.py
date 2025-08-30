import math
# Giving the user the choice between which calculation they want to run
choice = input(
    "Investment - to calculate the amount of interest you'll earn on your investment.\n"    
    "Bond - to calculate the amount you'll have to pay on a home loan.\n" 
    "Enter either investment or bond from the menu above to proceed:"
).lower()
# Print the results
print(choice)
# If user inputs investments
if choice == "investment":
# Prompt the user to enter numbers for interest calculation
    P = float(input("Enter the amount of money you would like to deposit: "))
    r = float(input("Enter the annual interest rate: ")) / 100
    t = int(input("Enter the number of years you would like to invest: "))
# Asking user to input if they want "simple" or "compound" interest
    interest_type = input("Please enter if you want simple or compound interest: ").lower()
# Simple interest formula
    if interest_type == "simple":
        A = P * (1 + r*t)
        print(A)
# Compound interest formula
    elif interest_type == "compound":
        A = P * math.pow((1+r),t)
        print(A)
# If user inputs an invalid response
    else:
        print("input invalid, please select simple or compound interest")
# If the user chooses bond calculation
elif choice == "bond":
# Prompt the user to enter numbers for bond payment
    P = float(input("Enter the present value of the house: "))
    i = float(input("Enter the annual interest rate: "))
    n = int(input("Enter the number of months over which the bond will be repaid: "))
# Final monthly interest rate after converting from annual rate 
    monthly_i = (i / 100) / 12 
# Bond payment formula    
    repayment = (monthly_i* P)/(1 - (1 + monthly_i)**(-n))
    print(f" monthly repayment: {repayment}")
# If user inputs an invalid response
else:
    print("Invalid selection. Please choose either 'investment' or 'bond'.")