#Inbuilt modules
import string
import random
#Characters Declaration
le=int(input("Enter Length of Password: "))
#If You want to get Whole Punctuations,type "string.punctuation" as replacement of 'punctuaton' variable name
punctuaton=",./?!@#%^&()~"
allcharacters=string.ascii_letters+string.digits+punctuaton
passw=''.join(random.choice(allcharacters) for i in range(le))
print("Now,You Can Copy and Paste this code or Open passw.txt file to Destination")
print(passw)
#Save in Progress & Overwrite file
with open("Password.txt","w") as file:
    file.write(passw)
print("Password Saved as Password.txt")