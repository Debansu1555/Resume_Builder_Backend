from twilio.rest import Client

def send_whatsapp(account_sid, auth_token, from_no, to_no, message):
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_=from_no,
        to=to_no
    )