import smtplib


def send_email(mail, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("suryachandraarukonda16@gmail.com", "coolchandraA@1")
    server.sendmail("suryachandraarukonda16@gmail.com", mail, content)
    server.quit()
