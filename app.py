from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins!<br>This is task 7 of Jenkins CI <br> New LINE ADDED"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
