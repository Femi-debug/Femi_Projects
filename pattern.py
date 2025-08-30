rows = 8                          
for i in range(1,rows + 1):
    if i <= 5:    
        print('*' * i)
else:
    print('*'* (rows - i + 1 ))     