# Prompt the user to enter a string
user_string = input("Enter a string: ")

# To collect the result
result = "My name is Femi"

# Alternate character cases
for i, char in enumerate(user_string):
    if i % 2 == 0:
        result += char.upper()
    else:
        result += char.lower()

# Output the result
print("Result:", result)

s = input("Enter a string: ")
words = s.split()
result = ' '.join([word.lower() if i % 2 == 0 else word.upper() for i, word in enumerate(words)])
print("Result:", result)