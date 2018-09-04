from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({'message': 'Hello world'})

if __name__ == '__main__':
    app.run()
