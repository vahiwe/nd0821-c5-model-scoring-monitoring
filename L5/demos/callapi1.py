import subprocess

response1=subprocess.run(['curl', '127.0.0.1:8000?user=Bradford'],capture_output=True).stdout
print(response1)

response2=subprocess.run(['curl', '127.0.0.1:8000/medians?filename=demodata.csv'],capture_output=True).stdout
print(response2)