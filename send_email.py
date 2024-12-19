import smtplib # standard lib
import ssl
import http.server

host = "smtp.gmail.com"
port = 465

password = "evne zhzd dong rchw"
username = "bchisu@gmail.com"

receiver = "bchisu@gmail.com"
my_context = ssl.create_default_context()

message = """\
subject: Hi!
How are you?
By!
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, message)