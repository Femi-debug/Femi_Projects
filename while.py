my_num = 0
while my_num > 0:
    print("Please enter a new number")
    if my_num <= 0:
        break
    for numbers in my_num:
        average = sum(my_num)/ len(my_num)
        print(average)

