import json
import re
import os
import sys
import urllib.request
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def firewallrule(id):
    payload={}
    headers = { "Content-Type": "application/json" }
    credentials = ('trainee','VMware1!VMware1!')

    URL = "https://10.0.0.94/policy/api/v1/infra/domains/default/security-policies/Test_Policy_" + str(id)

    name = "Test Policy " + str(id)
    payload = {
        "description": "comm map",
        "display_name": name,
        "category": "Application",
        "rules": [
          {
            "description": "Allow Apps 01 to access AD",
            "display_name": "Test_Rule_001",
            "sequence_number": 20,
            "source_groups": [
              "ANY"
            ],
            "destination_groups": [
              "/infra/domains/default/groups/MGMT"
            ],
            "services": [
              "/infra/services/AD_Server"
            ],
            "action": "DROP"
          }

        ]
    }


    response = requests.put(url=URL, data=json.dumps(payload), headers=headers, auth=credentials, verify=False)
    #dict_response = response.json()
    #print (json.dumps(dict_response, indent=2))

