#It requires Internet to fetch data from 'request_url'
import requests
import json5
print("Format of IP Address be in 'xxx.xxx.xxx.xxx' \r\n")
ip_address=input("Enter IP Address: ")
request_url='https://geolocation-db.com/jsonp/'+ip_address
response=requests.get(request_url)
result=response.content.decode()
result=result.split("(")[1].strip(")")
result=json5.loads(result)
#Shows the Output
print(result)