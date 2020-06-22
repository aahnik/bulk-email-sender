import setup
import extract
import smtplib
import ssl


sender, auth_code = extract.read_creds()

smtp_server = "smtp.gmail.com"
receiver = 'dawaahnik@gmail.com'


port = 465  # for SSL
con = ssl.create_default_context()
with open('compose.txt', 'r') as template:
    message = f"""\
    {template.read()}"""


with smtplib.SMTP_SSL(smtp_server, port, context=con) as server:
    server.login(sender, auth_code)
    server.sendmail(sender, receiver, message)
