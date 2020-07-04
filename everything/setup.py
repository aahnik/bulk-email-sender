import extract   # module written by AAHNIK 2020
import smtplib
import ssl

info = """# AAHNIK 2020
    RECOMMENDATIONS:
        do not use original password for running this program
        use a DEVICE AUTHENTICATION CODE generated from GMAIL"""
auth_warning = """ ** DO NOT TAMPER WITH THIS FILE ~auth.txt
    # MEANT TO BE READ AND WRITTEN ONLY BY PROGRAM
    # CORRUPTION IN THIS FILE MAY LEAD TO UNINTENDED AND DANGEROUS ERRORS"""


def checkConnection():

    flag = True
    print("\n\nCHECKING CONNECTION...\n")
    sender, auth_code = extract.read_creds()
    smtp_server = "smtp.gmail.com"
    port = 465  # for SSL
    con = ssl.create_default_context()
    try:
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


def run_setup():

    print("\nRUNNING SETUP ....\n")
    connected = checkConnection()
    if connected:
        print("\nCONNECTED\n")

    else:
        print("GO AND EDIT THE creds.py FILE PLEASE     oops!  your login credentials are incorrect ")


run_setup()


# AAHNIK 2020
