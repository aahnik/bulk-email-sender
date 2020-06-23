import setup    # module written by AAHNIK 2020
import extract    # module written by AAHNIK 2020
import smtplib
import ssl


sender_address, auth_code = extract.read_creds()
smtp_server = "smtp.gmail.com"
port = 465  # for SSL
con = ssl.create_default_context()

template = extract.template

with smtplib.SMTP_SSL(smtp_server, port, context=con) as server:
    server.login(sender_address, auth_code)
    for receiver_address, receiver_name in extract.data():
        message = template.replace('receiver', receiver_address)
        message = message.replace('$name', receiver_name)
        # print(message)
        # input("PRESS ENTER TO SEND THIS MESSAGE ")
        server.sendmail(sender_address, receiver_address, message)
