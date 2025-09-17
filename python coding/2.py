 #Password Strength Validator
# Validate a password based on:
# •At least one uppercase, one lowercase, one digit, one special character
# • Length between 8 and 16
# •No spaces
import string

password = input("enter password : ")

hasupper = haslower = hasspecial = hasdigit = hasspace = False


if(8 < len(password) < 16):
    flag = 0
else:
    flag = 1



for i in password:
    if(i.isupper() == 1):
        hasupper = True
        
    if(i.islower() == 1):
       haslower  = True

    if(i == ' '):
        hasspace = True
    
    if(i.isdigit() == 1):
        hasdigit = True
    
    for char in string.punctuation:
        if(i == char):
            hasspecial = True

if (flag == 0 and hasspecial and hasdigit and haslower and hasupper and hasspace == False):
    print("valid")

else:
    print("invalid")

