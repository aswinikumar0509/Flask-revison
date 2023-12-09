from flask import Flask



app = Flask(__name__)

@app.route('/')

def first():
    return "Hello Flask"

@app.route('/name')

def second():
    return "aswini kumar"

if __name__ == '__main__':
    app.run()