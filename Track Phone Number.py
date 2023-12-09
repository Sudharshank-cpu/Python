import phonenumbers
from phonenumbers import geocoder
phNo=input("Enter your Phone Number: ")
phno1=phonenumbers.parse(phNo)
#To check it
#phno2=phonenumbers.parse("+12136574429")
#It gets only at International Phone Numbers.Can't track all Numbers
print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phno1,"en"))
#print(geocoder.description_for_number(phno2,"en"))
#To install "pip install phonenumbers"
