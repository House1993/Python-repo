__author__ = 'Fang'

import json
import unicodecsv


def read_json(file_name):
    with open(file_name, "rb") as inFile:
        data = json.load(inFile)
    return data


def write_json(file_name, data):
    with open(file_name, "wb") as outFile:
        json.dump(data, outFile)


def read_csv(file_name):
    with open(file_name, "r") as inFile:
        reader = unicodecsv.reader(inFile)
        data = []
        for cols in reader:
            data.append(cols)
    return data


def write_csv(file_name, data):
    with open(file_name, "w") as outFile:
        writer = unicodecsv.writer(outFile)
        writer.writerows(data)


def read_str_file(file_name):
    with open(file_name, "r") as inFile:
        data = inFile.read()
    return data


def write_str_file(file_name, data):
    with open(file_name, "w") as outFile:
        outFile.write(data)


def write_log(log_file_name, log_info):
    with open(log_file_name, "a") as log:
        log.write(log_info)
