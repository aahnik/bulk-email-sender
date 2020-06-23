import extract   # module written by AAHNIK 2020
import smtplib
import ssl
info = """# AAHNIK 2020
    RECOMMENDATIONS:
        do not use original password for running this program
        use a DEVICE AUTHENTICATION CODE generated from GMAIL"""


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
        global sender
        sender = input("ENTER SENDER'S (your) GMAIL ID : ")
        auth_code = input("ENTER THE AUTHENTICATION CODE: ")
        with open('~auth.txt', 'w') as file:
            file.write(f"{sender}\n{auth_code}\n{info}")
        run_setup()


def make_original():
    with open('data.csv', 'w') as file:
        file.write('EMAIL,NAME')
    with open('compose.txt', 'w') as file:
        file.write("""The first line is treated as SUBJECT automatically and is highlighted 

                    Hey this is the body of the mail , above line must be EMPTY
                    
                    SEE screenshot OF HOW THE EMAIL LOOKS TO THE RECIEVER

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero in, suscipit maxime quod 
                dolor cupiditate porro consequuntur, minima ipsa perferendis odit nemo sed expedita consequatu
                placeat! Aspernatur blanditiis illum accusamus?
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero in, suscipit maxime quod 
                dolor cupiditate porro consequuntur, minima ipsa perferendis odit nemo sed expedita consequatu
                placeat! Aspernatur blanditiis illum accusamus?
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero in, suscipit maxime quod 
                dolor cupiditate porro consequuntur, minima ipsa perferendis odit nemo sed expedita consequatu
                placeat! Aspernatur blanditiis illum accusamus?



                yours lovely
                Aahnik 2020""")


run_setup()


# AAHNIK 2020
