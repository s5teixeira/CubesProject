import sys
import requests
import json
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth

subdomain = 'https://stepht15.wufoo.com/api/v3/'
format = 'forms/cubes-project-proposal-submission/entries/json'
url = subdomain + format
username = wufoo_key
password = 'helloworld'
wufoo_file = open('txtfile.txt', 'w')


def message():
    response = requests.get(url, auth=(username, password))
    if response.status_code != 200:
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        print(response.raise_for_status())
        sys.exit(-1)


def get_wufoo_data1():
    response = requests.get(url, auth=(username, password))
    data = json.loads(response.text)
    print(json.dumps(data, indent=4, sort_keys=True))


def get_wufoo_data2():
    response = requests.get(url, auth=(username, password))
    data = json.loads(response.text)
    print(json.dumps(data, indent=4, sort_keys=True))


def get_wufoo_data3():
    response = requests.get(url, auth=(username, password))
    data = json.loads(response.text)
    wufoo_file.write(str(data))
    print(json.dumps(data, indent=4, sort_keys=True))


def get_wufoo_data4():
    response = requests.get(url, auth=(username, password))
    data = json.loads(response.text)
    wufoo_file.write(str(data))
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    message()
    get_wufoo_data1()
    get_wufoo_data2()
    get_wufoo_data3()
    get_wufoo_data4()
