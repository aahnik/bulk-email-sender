import setup    # module written by AAHNIK 2020
import extract    # module written by AAHNIK 2020
import smtplib
import ssl


sender, auth_code = extract.read_creds()
smtp_server = "smtp.gmail.com"
port = 465  # for SSL
con = ssl.create_default_context()

template = extract.template

with smtplib.SMTP_SSL(smtp_server, port, context=con) as server:
    server.login(sender, auth_code)
    for receiver, name in extract.data():
        message = template.replace('receiver', receiver)
        server.sendmail(sender, receiver, message)
setup.make_original()