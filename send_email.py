import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email, subject, body):
    sender_email = "javed0786alam@gmail.com"
    password = "Qwerty@1225"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email + "@gmail.com"
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email + "@gmail.com", text)
    server.quit()

    print("Email sent successfully!")

