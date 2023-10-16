import smtplib, ssl

def send_email(message) :
    port = 465  # For SSL
    password = "wcmk ufpe oscq fdat"

    # Create a secure SSL context
    context = ssl.create_default_context()

    sender_email = "hire.muhlis@gmail.com"
    receiver_email = "muhlis.asri@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("hire.muhlis@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
