import requests
from . import constants
import pandas as pd


def get_process_by_name(process_name):
    response = requests.post(f"{constants.GEOWEAVER_DEFAULT_ENDPOINT_URL}/web/list", data={'type': 'process'})
    process_list = response.json()

    matching_processes = []

    for process in process_list:
        if process['name'] == process_name:
            matching_processes.append(process)
    pd.DataFrame(matching_processes)


def get_process_by_id(process_id):
    response = requests.post(f"{constants.GEOWEAVER_DEFAULT_ENDPOINT_URL}/web/list", data={'type': 'process'})
    process_list = response.json()

    matching_processes = []

    for process in process_list:
        if process['id'] == process_id:
            matching_processes.append(process)
    pd.DataFrame(matching_processes)


def get_process_by_language(language):
    response = requests.post(f"{constants.GEOWEAVER_DEFAULT_ENDPOINT_URL}/web/list", data={'type': 'process'})
    process_list = response.json()

    matching_processes = []

    for process in process_list:
        if process['lang'] == language:
            matching_processes.append(process)
    pd.DataFrame(matching_processes)

