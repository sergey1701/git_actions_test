from flask import *

app = Flask(__name__)

@app.route('/')

def main_page():
    return "<html><body><h1>Hi, Git Actions Test</h1></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)    