from flask import Flask
app = Flask(__name__)
from flask_cors import CORS

if __name__ == '__main__':
    app.run(debug=True)

CORS(app, origins=[
    'http://localhost:5173',
], methods=['GET', 'POST'], supports_credentials=True)

@app.route("/")
def firstview():
    return("HELLO WORLD !!!")
from controller import * 

