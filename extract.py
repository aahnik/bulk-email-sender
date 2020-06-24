import csv
import yaml


def extract_configs():

    with open('config.yaml', 'r') as file:
        configs = yaml.full_load(file)
    return configs


configs = extract_configs()

sender_name = configs['sender_name']
auth_file = configs['auth']
data_file = configs['pull_data_from']
compose = configs['compose']



file = open(compose, 'r')

template = f"""\
from: {sender_name}
to: receiver
subject: {file.readline()}

{file.read()} """


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

# AAHNIK 2020
