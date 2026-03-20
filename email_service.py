from flask_mail import Message

def send_email(mail, to, pdf_bytes, password):
    msg = Message("Your Resume", recipients=[to])
    msg.body = f"Your PDF password is: {password}"

    msg.attach("resume.pdf", "application/pdf", pdf_bytes)

    mail.send(msg)