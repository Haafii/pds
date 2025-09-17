#to print 1 to 100 replace 3 with buzz 5 with fizz and both multiple with fizzbuzz

for i in range(1,101):
    if (i%15==0):
        print("fizzbuzz")
    elif(i%5==0):
        print("fizz")
    elif(i%3==0):
        print("buzz")
    else:
        print(i)


