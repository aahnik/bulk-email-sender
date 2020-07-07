import csv
import os
import creds

sender_name = creds.DISPLAY_NAME


with open('compose.md', 'r') as file:
    template = file.read()


def read_creds():
    return creds.SENDER_EMAIL, creds.PASSWORD


def get_dynamic_from_template(csv_file_path, template):
    with open(csv_file_path, 'r') as file:
        headers = file.readline().split(',')
        headers[len(headers) - 1] = headers[len(headers) - 1][:-1]
    # i am opening the csv file two times above and below INTENTIONALLY, changing will cause error
    with open(csv_file_path, 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            required_string = template
            for header in headers:
                value = row[header]
                required_string = required_string.replace(f'${header}', value)
            yield row['EMAIL'],required_string



def confirm_attachments():
    attachments = []
    filenames = []
    for filename in os.listdir('ATTACH'):

        entry = input(f"""TYPE IN 'Y' AND PRESS ENTER IF YOU CONFIRM T0 ATTACH {filename} 
                                TO SKIP PRESS ENTER: """)
        confirmed = True if entry == 'Y' else False
        if confirmed:
            filenames.append(filename)
            attachment = open(f'{os.getcwd()}/ATTACH/{filename}', "rb")
            attachments.append(attachment)

    return filenames, attachments


# AAHNIK 2020
