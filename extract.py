import smtplib
import ssl
import yaml


configs = {}
smtp_server = "smtp.gmail.com"


def extract():

    with open('config.yaml', 'r') as file:
        global configs
        configs = yaml.full_load(file)


def read_creds():
    with open('~auth.txt', 'r') as file:
        sender = file.readline()
        auth_code = file.readline()
    return sender, auth_code


def checkConnection():

    flag = True
    print("\n\nCHECKING CONNECTION...\n")
    sender, auth_code = read_creds()
    try:
        port = 465  # for SSL
        con = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=con) as server:
            server.login(sender, auth_code)

    except Exception as e:
        flag = False
        error = str(e)
        if ("Username and Password not accepted" in error):
            print("\n   Incorrect Login Credentials :-( \n")
        else:
            print("\nSOME UNKNOWN ERROR OCCURED :-( SEE DETAILS BELOW \n\n", e)

    finally:
        return flag


if __name__ == "__main__":

    print('\n\n\n')
    extract()
    print(configs)
    print("CONNECTION:", "\tSUCCESS" if checkConnection() == True else "\tFAILED")
    print('\n\n\n')


# AAHNIK 2020
