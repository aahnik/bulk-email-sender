# this function extracts data from config.yaml
import yaml
import smtplib


configs = {}


def extract():

    with open('config.yaml', 'r') as file:
        global configs
        configs = yaml.full_load(file)


def checkConnection():

    flag = True
    print("\n\nCHECKING CONNECTION...")

    with open('~auth.txt', 'r') as file:
        sender = file.readline()
        auth_code = file.readline()

    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
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