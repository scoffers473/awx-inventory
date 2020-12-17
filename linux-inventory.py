#!/usr/bin/env python3
import os
import requests
import json, yaml
from argparse import ArgumentParser
import urllib3


def getInventoryData(hostname=""):
    #results = {'_meta': { 'hostvars': {}}}
    results = { }

    groupname='Development'
    if groupname not in results:
        results[groupname]={
            'name': groupname,
            'hosts': [],
            'vars': {}
        }
    results[groupname]['hosts'].append(['centos'])
    #results["alll"] = {"vars":{"url":"http://www.test.com"}}
    return results


def list_groups():
    """Returns a dict of all the available apps

    {
        name: 'foo',
        hosts: ['bar.example.com', 'baz.example.com'],
        vars: {
            foo: 42,
            bar: 'baz'
        },
        children: ['bar']
    }
    """
    results = getInventoryData()

    return json.dumps(results)

def show_host(hostname):
    """Returns a dict containing the variables for a specific host
    {
        hostname: 'foo.example.com',
        vars: {
            foo: 42,
            bar: 'baz'
        }
    }
    """
    result = getInventoryData(hostname)
    return json.dumps(result)

# Main Entry
def main():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', dest='list', action='store_true')
    group.add_argument('--host', dest='host', metavar='<hostname>')

    args = parser.parse_args()
    if args.list:
        result = list_groups()
    elif args.host:
        result = show_host(args.host)

    print(result)

if __name__ == '__main__':
    main()
