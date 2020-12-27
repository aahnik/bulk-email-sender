import setup    # module written by AAHNIK 2020
import extract    # module written by AAHNIK 2020
import smtplib
import ssl
import markdown
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email import encoders
import os

sender_address, auth_code = extract.read_creds()
smtp_server = "smtp.gmail.com"
port = 587  # TLS replaced SSL in 1999.
con = ssl.create_default_context()
template = extract.template
filenames, attachments = extract.confirm_attachments()

sent_count = 0
try_count = 0
with smtplib.SMTP_SSL(smtp_server, port, context=con) as server:

    for receiver_address, message in extract.get_dynamic_from_template('data.csv', template):

        if try_count % 40 == 0:
            # Login agian after sending every 40 tries
            # Prevent timeout
            server.login(sender_address, auth_code)

        sent = True
        multipart_msg = MIMEMultipart("alternative")

        multipart_msg["Subject"] = message.splitlines()[0]
        multipart_msg["From"] = extract.sender_name
        multipart_msg["To"] = receiver_address

        text = message
        html = markdown.markdown(text)
        # with open('compose.html', 'w+') as html_file:
        #     html_file.write(html)

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        multipart_msg.attach(part1)
        multipart_msg.attach(part2)

        for attachment, filename in zip(attachments, filenames):
            attach_part = MIMEBase('application', 'octet-stream')
            attach_part.set_payload((attachment).read())
            encoders.encode_base64(attach_part)
            attach_part.add_header('Content-Disposition',
                                   f"attachment; filename= {filename}")
            multipart_msg.attach(attach_part)

        # input("PRESS ENTER TO SEND THIS MESSAGE ")
        try:
            try_count += 1
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
                sent_count += 1
            else:
                print(f"Failed to  send email to {receiver_address}")

    print(f" sent {sent_count} emails")


# AAHNIK 2020
