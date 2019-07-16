#!/usr/bin/env python3

import json
import requests
from requests.auth import HTTPBasicAuth

# DevNet Sandbox details
URI = "https://sandboxdnac.cisco.com"
TOKEN_PATH = "/dna/system/api/v1/auth/token"
USER = "devnetuser"
PASS = "Cisco123!"

INPUT_FILE = "./api_json/dnac_intent_v1_3_template.json"
OUTPUT_FILE_DIR = "./api_json_result/"

def get_token(uri, token_path, user, pwd):
    headers = {
        "Content-Type": "application/json",
    }

    r = requests.post(
        uri + token_path,
        auth=HTTPBasicAuth(username=user, password=pwd),
        headers=headers,
    )
    return r.json()["Token"]

# CRUD Methods
# post, get, put, delete
def request(method, uri, body, token):

    r = getattr(requests, method)(
        uri + body,
        headers = {
            "X-Auth-Token" : token,
            "Content-type" : "application/json"
        },
    )

    return r.json()


# Read file and assign variable to a dict object
with open(INPUT_FILE) as file_handle:
    resource_dict = json.load(file_handle)

# Connect to Cisco DNA Center Sandbox and make a REST request
token = get_token(URI, TOKEN_PATH, USER, PASS)
result = request(resource_dict["request"], URI, resource_dict["resource_path"], token)

# Writing result to file.
for json_kv_pair in result:
    with open(OUTPUT_FILE_DIR + json_kv_pair["name"] + ".json", "w") as file_handle:
        json.dump(json_kv_pair, file_handle, indent=4)
