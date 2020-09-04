import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import vision

# Create dictionary so that you have not enter manually email address
mail_address = {'Friends name': 'Friends Email Address'}


def mail():
    # Write here sender email address and password
    sender_email = "sender email address"
    password = "sender email password"

    vision.speak("Who do you want to email? ")
    receiver = vision.command()

    if receiver in mail_address:
        receiver_email = mail_address[receiver]

        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["To"] = receiver_email

        # This is for email subject
        vision.speak(f"Got it, you want to email {receiver}.\n"
                     f"What's the Subject?")
        subject = vision.command()

        # Create the plain-text version of your message
        vision.speak(f"Got it, What's the message?")
        text = vision.command()

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message["Subject"] = subject

        try:
            # Create secure connection with server and send email
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                vision.speak("Sir I have successfully send mail..")

        except smtplib.SMTPException:
            vision.speak("Error: unable to send email")
