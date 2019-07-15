#!/usr/bin/env python3

import json

# Read file and assign to a dict
with open("./api_json/dnac_intent_v1_3.json") as file_handle:
    rest_resource_dict = json.load(file_handle)

# Checking if its a dict
print("REST RESOURCE")
print(type(rest_resource_dict))

# Printing Depth 1 Keys.
# To be continued
for i in rest_resource_dict:
    print(i)
    print("-" * 10)
