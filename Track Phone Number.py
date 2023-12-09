import phonenumbers
from phonenumbers import geocoder
#                        "             "-Enter your Phone Number from Here
phno1=phonenumbers.parse("+917092732950")
phno2=phonenumbers.parse("+919344123335")
phno3=phonenumbers.parse("+12136574429")
phno4=phonenumbers.parse("+911234567890")
print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phno1,"en"))
print(geocoder.description_for_number(phno2,"en"))
print(geocoder.description_for_number(phno3,"en"))
print(geocoder.description_for_number(phno4,"en"))
