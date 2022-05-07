import re
from PassManager import *

def checkSecPass(passInput):
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    
    if len(passInput) < 8:
        print("Your Password Must be More Than 8 Characters, Please Try Again!")
        return False
    elif (string_check.search(passInput) == None):
        print("Password must contain at least one special character, Please try again!")
        return False
    elif not (bool(re.search(r'\d', passInput))):
        print("Password must contain at least a number, Please try again!")
        return False
    else:
        return True


passInput = input("Enter the password!:")
print(checkSecPass(passInput))
