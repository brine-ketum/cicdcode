from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Yeyyyy, i have successfully build a fully automated CICD pipeline!!!'
