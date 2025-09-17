#Write a Python program that handles discount of 500rs for every 100 litres of petrol 
# filled by a customer,
#  and carries forward extra litres to the next billing cycle. 
# (note: enter 0 to come out of loop)

#print("enter the liter of petrol to be filled: ")

totalliter = 0

while True :
    liter = int(input("enter the liter of petrol to be filled: "))
    totalliter += liter
    if(totalliter >= 100):
        discount = ( totalliter // 100 ) * 500
        print("here is", discount, "rupees")
        
        totalliter = totalliter % 100
        
        print("the balence liter is ", totalliter)


    if(liter == 0):
        break
    




