import extract as e
info = """# AAHNIK 2020
    RECOMMENDATIONS:
        do not use original password for running this program
        use a DEVICE AUTHENTICATION CODE generated from GMAIL"""


def run_setup():
    print("\nRUNNING SETUP ....\n")
    e.extract()
    connected = e.checkConnection()
    if connected:
        print("\nCONNECTED\n")

    else:
        global sender
        sender = input("ENTER SENDER'S (your) GMAIL ID : ")
        auth_code = input("ENTER THE AUTHENTICATION CODE: ")
        with open('~auth.txt', 'w') as file:
            file.write(f"{sender}\n{auth_code}\n{info}")
        run_setup()


run_setup()


# AAHNIK 2020
