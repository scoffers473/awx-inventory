#!/usr/bin/env python3
import os
import requests
import json, yaml
from argparse import ArgumentParser
import urllib3


def getInventoryData(hostname=""):
    results = {'_meta': { 'hostvars': {}}}

    groupname='vagrant'
    if groupname not in results:
        results[groupname]={
            'name': groupname,
            'hosts': [],
            'vars': {}
        }
    results[groupname]['hosts'].append('192.168.100.2')


    groupname='vbox'
    if groupname not in results:
        results[groupname]={
            'name': groupname,
            'hosts': [],
            'vars': {}
        }
    results[groupname]['hosts'].append('192.168.0.47')
    results[groupname]['hosts'].append('192.168.0.65')
    results[groupname]['hosts'].append('192.168.0.66')

    groupname='rhel'
    if groupname not in results:
        results[groupname]={
            'name': groupname,
            'hosts': [],
            'vars': {}
        }
    results[groupname]['hosts'].append('192.168.0.65')

    groupname='centos'
    if groupname not in results:
        results[groupname]={
            'name': groupname,
            'hosts': [],
            'vars': {}
        }
    results[groupname]['hosts'].append('192.168.0.66')

    results['all'] = {'hosts': [],'vars':{'url':'http://www.test.com'}}
    results['all']['hosts'].append('192.168.100.2')
    results['all']['hosts'].append('192.168.0.47')
    results['all']['hosts'].append('192.168.0.65')
    results['all']['hosts'].append('192.168.0.66')
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
