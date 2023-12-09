import qrcode
#"pip install pyqrcode" to install 'qrcode' for importation in Python
#Generate QR Code using "make()" function
value=str(input("Enter a String: "))
qrimg=qrcode.make(value)
#Saving Image File
qrimg.save("qr-img.jpg")
