import pandas as pd
import requests
import json
import ast
import pprint


def get_API_Key() -> str:
    with open("./apikey", "r") as apikey_file:
        api_key = apikey_file.readlines()[0].strip()
    return api_key


api_endpoint = "https://api.core.ac.uk/v3/"


def query_api(url_fragment, query, limit=300):
    headers = {"Authorization": "Bearer " + get_API_Key()}
    query = {"q": query, "limit": limit}
    response = requests.post(f"{api_endpoint}{url_fragment}", data=json.dumps(query), headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error code {response.status_code}, {response.content}")

def get_entity(url_fragment):

    headers = {"Authorization": "Bearer " + get_API_Key()}
    response = requests.get(api_endpoint + url_fragment, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error code {response.status_code}, {response.content}")


def main():
    # get all data providers in uk
    #results = query_api("search/data-providers", "location.countryCode:gb")
    # print(provider['oaiPmhUrl'] for provider in results['results'])
    #get_all_oaiPmhUrls(results)

    get_known_software_from_core()


def get_known_software_from_core():
    frags = ["works/42882199", "works/77266753", "works/78543945", "/works/8249065", "works/8221449"]
    for frag in frags:
        pprint.pprint(get_entity(frag))
def get_all_oaiPmhUrls(results):
    all_oaiPmhUrls = []
    for provider in results['results']:
        oaiPmhUrl = provider['oaiPmhUrl']
        print(oaiPmhUrl)
        all_oaiPmhUrls.append(oaiPmhUrl)

    return all_oaiPmhUrls

main()
