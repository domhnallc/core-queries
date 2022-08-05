import pandas as pd
import requests
import json
import pprint

def get_API_Key() -> str:
    with open ("./apikey", "r") as apikey_file:
        api_key=apikey_file.readlines()[0].strip()
    return api_key

api_endpoint = "https://api.core.ac.uk/v3/"

def query_api(url_fragment, query,limit=100):
    headers={"Authorization":"Bearer "+get_API_Key()}
    query = {"q":query, "limit":limit}
    response = requests.post(f"{api_endpoint}{url_fragment}",data = json.dumps(query), headers=headers)
    if response.status_code ==200:
        return response.json(), response.elapsed.total_seconds()
    else:
        print(f"Error code {response.status_code}, {response.content}")




def main():
    #results , elapsed = query_api("search/data-providers", "location.countryCode:gb")
    query = f"type:article"
    results = query_api("search/works", query, limit=1)


    pprint.pprint(results)


main()