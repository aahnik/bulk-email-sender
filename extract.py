import csv
import yaml
import os


def extract_configs():

    with open('config.yaml', 'r') as file:
        configs = yaml.full_load(file)
    return configs


configs = extract_configs()

sender_name = configs['sender_name']
auth_file = configs['auth']
data_file = configs['pull_data_from']
# compose = configs['compose']


with open('compose.md', 'r') as file:
    template = file.read()


def read_creds():

    with open(auth_file, 'r') as file:
        sender = file.readline()
        auth_code = file.readline()
    return sender, auth_code


def data():

    with open(data_file, 'r') as csv_file:
        data_dict = csv.DictReader(csv_file)
        for row in data_dict:
            yield row['EMAIL'], row['NAME']


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
