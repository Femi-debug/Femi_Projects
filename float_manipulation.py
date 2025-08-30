import math
from statistics import mean 
from statistics import median
list_a = []
# Loop 10 times to get user input
for i in range(10):
    # Prompt user and convert input to float
    num = float(input(f"Enter float number {i+1}: "))
    # Add the number to the list
    list_a.append(num)
# Print the collected list of floats
print("The list of entered numbers is:", list_a)
print(sum(list_a))
print(min(list_a))
print(max(list_a))
print(mean(list_a))
print(median(list_a))
