from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Your Flask app is running globally."

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) to make it accessible globally
    app.run(host='0.0.0.0', port=5001)
