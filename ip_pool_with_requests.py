#!/usr/bin/env python3

from intersight_auth import IntersightAuth
from pathlib import Path
import cli_arguments
import requests

args = cli_arguments.cli_arguments_function()
home = Path.home()

api_auth = IntersightAuth(api_key_id=args.api_key_id, secret_key_filename=args.api_key_file)

orgs = requests.get(f"https://{args.endpoint}/api/v1/organization/Organizations", auth=api_auth)
orgs_json = orgs.json()
for i in orgs_json['Results']:
    if i['Name'] == 'default':
        default_org_moid = i['Moid']

print(f'default org moid is: {default_org_moid}')
payload = {
    'AssignmentOrder': 'default',
    'Description': 'Demo Pool Creation',
      "IpV4Blocks": [
        {
          "From": "198.18.24.101",
          "ObjectType": "ippool.IpV4Block",
          "Size": 27
        }
      ],
      "IpV4Config": {
        "Gateway": "198.18.24.1",
        "Netmask": "255.255.255.0",
        "ObjectType": "ippool.IpV4Config",
        "PrimaryDns": "10.101.128.15",
        "SecondaryDns": "10.101.128.16"
      },
      "Name": "demo-198-18-24-0",
      "ObjectType": "ippool.Pool",
      "Organization": {
        "Moid": default_org_moid,
        "ObjectType": "organization.Organization"
      }
}

pool = requests.post(f"https://{args.endpoint}/api/v1/ippool/Pools", auth=api_auth, json=payload)

print(f'pool status is {pool}')
if pool.json():
    pool_json = pool.json()
    pool_moid = pool_json['Moid']
    print(f'pool demo-198-18-24-0 moid is:{pool_moid}')
exit()