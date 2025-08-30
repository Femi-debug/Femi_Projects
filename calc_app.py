file = None
def calculator():
   print ("\n")

   try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        opp = input("Enter an operation [+, -, *, /]" )
   except ValueError:
        print("Oops! That was not a valid entry. Try again...")
        return


   if (opp == "+"):
       result = num1 + num2
   elif (opp == "-"):
       result = num1 - num2
   elif (opp == "*"):
       result = num1 * num2
   elif (opp == "/"):
       try:
        result = num1 // num2 
       except ZeroDivisionError:
          print("Invalid Equation\n") 
          print("Try Again")       

   else:
    result = ("invalid operation entered")
print (f"The result of operation is: {result}")


try:
 file = open('equations', 'r')
 # Do stuff with the file here
except FileNotFoundError as error:
 print("The file that you are trying to open does not exist")
 print(error)
finally:
 if file is not None:
    file.close()   

 while True:
   calculator()