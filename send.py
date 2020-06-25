import setup    # module written by AAHNIK 2020
import extract    # module written by AAHNIK 2020
import smtplib
import ssl
import markdown
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_address, auth_code = extract.read_creds()
smtp_server = "smtp.gmail.com"
port = 465  # for SSL
con = ssl.create_default_context()
template = extract.template

count = 0
with smtplib.SMTP_SSL(smtp_server, port, context=con) as server:
    server.login(sender_address, auth_code)
    for receiver_address, receiver_name in extract.data():

        sent = True
        message = template.replace('receiver', receiver_address)
        # print(message)
        message = message.replace('$name', receiver_name)
        # print(message)

        multipart_msg = MIMEMultipart("alternative")

        multipart_msg["Subject"] = "Testing mime"
        multipart_msg["From"] = extract.sender_name
        multipart_msg["To"] = receiver_address

        # print("mime subject  from to  lines executed")

        text = message
        html = markdown.markdown(text)
        # print(html)

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        multipart_msg.attach(part1)
        multipart_msg.attach(part2)


       

        # filename = 'screenshot1.png'
        # attachment = open(filename, "rb")
        # attach_part = MIMEBase('application', 'octet-stream')
        # attach_part.set_payload((attachment).read())
        # encoders.encode_base64(attach_part)
        # attach_part.add_header('Content-Disposition',
        #                        f"attachment; filename= {filename}")

        # multipart_msg.attach(attach_part)

        input("PRESS ENTER TO SEND THIS MESSAGE ")
        try:
            server.sendmail(sender_address, receiver_address,
                            multipart_msg.as_string())
        except Exception as e:
            sent = False
            # print(
            #     f"some error occured while sending email to {receiver_address} ")
            print(e)
            input("PRESS ENTER TO CONTINUE")
        finally:
            if sent:
                print(f"Successfully sent email to {receiver_address}")
                count += 1
            else:
                print(f"Failed to  send email to {receiver_address}")

    print(f" sent {count} emails")
