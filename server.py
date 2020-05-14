import re
import json
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from gmail_api import authenticate, CreateMessage, SendMessage

SCOPES = ['https://mail.google.com/']

app = Flask(__name__)
keyFile = open('secret_key.txt', 'r') 
app.config['SECRET_KEY'] = keyFile.readline()
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/form": {"origins": "https://moarart.net"}})

@app.route('/form', methods=['GET','POST'])
@cross_origin(origin='moarart.net',headers=['Content- Type','Authorization'])
def form_submitted():
    data = request.data
    data = json.loads(data)
    print(data)
    send_mail(data)
    return "success"

def send_mail(data):
    service = authenticate()
    with open("email_template.txt") as email_template:
        email_text = email_template.read()
        email_text = fill_email(email_text, data)
        message = CreateMessage("contact.moarart@gmail.com", "contact@moarart.net", "Moar Art Purchase Inquiry for " + data['piece_name'], email_text)
        message_copy = CreateMessage("contact.moarart@gmail.com", "mihiralvedev@gmail.com", "Moar Art Purchase Inquiry for " + data['piece_name'], email_text)

    status = SendMessage(service, "me", message)

    status_copy = SendMessage(service, "me", message_copy)


def fill_email(email_text, data):
    email_text = re.sub("%piece_name%", data['piece_name'], email_text)
    email_text = re.sub("%name%", data['name'], email_text)
    email_text = re.sub("%email%", data['email'], email_text)
    email_text = re.sub("%zip%", data['zip_code'], email_text)
    email_text = re.sub("%message%", data['message'], email_text)

    return email_text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')