#!/usr/bin/env python3

from intersight_auth import IntersightAuth
from pathlib import Path
import cli_arguments
import logging
import requests

args    = cli_arguments.cli_arguments_function()
api_auth= IntersightAuth(api_key_id=args.api_key_id, secret_key_filename=args.api_key_file)

def get_organization(logger, org_name):
    orgs = requests.get(f"https://{args.endpoint}/api/v1/organization/Organizations", auth=api_auth)
    orgs_json = orgs.json()
    for i in orgs_json['Results']:
        if i['Name'] == org_name:
            org_moid = i['Moid']
    logger.info(f"Organization {org_name} moid is: {org_moid}")
    return org_moid

def create_ip_payload(org_moid):
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
            "Moid": org_moid,
            "ObjectType": "organization.Organization"
        }
    }
    return payload

def create_ip_pool(args, payload):
    pool = requests.post(f"https://{args.endpoint}/api/v1/ippool/Pools", auth=api_auth, json=payload)
    return pool


def main():
    FORMAT = '%(asctime)-15s [%(levelname)s] [%(filename)s:%(lineno)s] %(message)s'
    LOGGING_LEVEL = logging.INFO
    logging.basicConfig(format=FORMAT, level=LOGGING_LEVEL)
    logger = logging.getLogger()

    # Creating ippool_pool
    org_moid = get_organization('default')
    payload  = create_ip_payload(logger, org_moid=org_moid)
    logger.info("Creating the ippool_pool.")
    pool_results = create_ip_pool(args, payload)
    logger.info("ippool_pool is created successfully.")
    if pool_results.json():
        pool_json = pool_results.json()
        pool_moid = pool_json['Moid']
        logger.info(f"pool demo-198-18-24-0 moid is:{pool_moid}")

    exit()

if __name__ == '__main__':
    main()
