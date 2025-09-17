#Print a triangle of numbers where each row skips even numbers:
number = 1
row = int(input("enter the number of rows : "))
for i in range(1, row + 1):  # to detrmine how many rows
    for j in range(0, i*2): #skip the number of numbersin each row
        if(number % 2 != 0 ):
            print(number, end = ' ') #in python normly print in next line without /n thaty end 
        number = number + 1

    print("")