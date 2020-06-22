import setup

server = setup.server
from_email = 'AAHNIK'


def send_mail():
    input("PRESS ENTER TO SEND MAIL: ")
    try:
        server.sendmail(from_email, 'dawaahnik@gmail.com', "new")
        print("sent")
    except:
        print("error")


send_mail()
