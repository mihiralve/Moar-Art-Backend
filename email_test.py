from gmail_api import authenticate, CreateMessage, SendMessage

SCOPES = ['https://mail.google.com/']

service = authenticate()

with open("email_template.txt") as email_template:
    email_text = email_template.read()
    message = CreateMessage("contact.moarart@gmail.com", "mihiralvedev@gmail.com", "Moar Art Purchase Inquiry for {Piece}", email_text)
    print(message)        

status = SendMessage(service, "me", message)

print(status)