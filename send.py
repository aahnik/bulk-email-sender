import setup    # module written by AAHNIK 2020
import extract    # module written by AAHNIK 2020
import smtplib
import ssl
import markdown
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

        mime_msg_send = MIMEMultipart("alternative")

        mime_msg_send["Subject"] = "Testing mime"
        mime_msg_send["From"] = extract.sender_name
        mime_msg_send["To"] = receiver_address

        # print("mime subject  from to  lines executed")

        text = message
        html = markdown.markdown(text)
        # print(html)

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        mime_msg_send.attach(part1)
        mime_msg_send.attach(part2)

        # print("part 1 and 2 attached")

        # print(message)
        input("PRESS ENTER TO SEND THIS MESSAGE ")
        try:
            server.sendmail(sender_address, receiver_address,
                            mime_msg_send.as_string())
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
