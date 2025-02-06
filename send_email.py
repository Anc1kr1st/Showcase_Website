import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "riso.bajan@gmail.com"
password = "htaj qynd lzuh tcbk"

receiver = "riso.bajan@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)