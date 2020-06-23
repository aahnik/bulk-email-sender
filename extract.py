import csv
import yaml


def extract_configs():

    with open('config.yaml', 'r') as file:
        configs = yaml.full_load(file)
    return configs


def read_creds():

    with open('~auth.txt', 'r') as file:
        sender = file.readline()
        auth_code = file.readline()
    return sender, auth_code


def data():

    with open('data.csv', 'r') as csv_file:
        data_dict = csv.DictReader(csv_file)
        for row in data_dict:
            yield row['EMAIL'], row['NAME']


configs = extract_configs()

file = open('compose.txt', 'r')

template = f"""\
from: {configs['sender_name']}
to: receiver
subject: {file.readline()}

{file.read()} """


# AAHNIK 2020
