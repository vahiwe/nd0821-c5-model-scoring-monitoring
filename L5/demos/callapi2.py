import requests 

response3=requests.get('http://127.0.0.1:8000?user=Bradford').content 
print(response3) 

response4=requests.get('http://127.0.0.1:8000/medians?filename=demodata.csv').content 
print(response4)