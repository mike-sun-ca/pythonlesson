import requests
import json

headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
urlAddress = "http://api.weatherstack.com/current" \
"?access_key=e456ff10006f8eeec0f7d944692696b0" \
"&query=Langley" \
"&units=m" \
"& language = en" \
"& callback = MY_CALLBACK"
response= requests.get(urlAddress,headers)
print (urlAddress)
print(response.text)
print("*******************")
jsonStr = json.loads(response.text)
print("Current Temperature: " , jsonStr['current']["temperature"] , "Celsius degree")