import os
from flask import Flask


# Flask APP
app = Flask(__name__, template_folder="templetes")


@app.route('/', methods=['GET'])
def index():
    # Main page
    return "TEST SERVER"


if __name__ == '__main__':
    app.run(debug=True) 