from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user = request.args.get('user')
    return "Hello " + user

app.run(host='0.0.0.0', port=8000)