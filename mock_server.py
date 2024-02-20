from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Mock API Gateway Running'


@app.route('/disable', methods=['POST'])
def disable():
    return 'API Gateway Disabled', 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
