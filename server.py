from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/form')
def form_submitted():
    return "Form submitted!"