from flask import Flask
app = Flask(__name__)

if__name__ == '__main__':
#Fire up the Flask test server
app.run(debug=True, use_reloader=True)
