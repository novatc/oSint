from ipwhois import IPWhois
from pprint import pprint
import requests
import json


def get_ripe_info(ip):
    obj = IPWhois(ip)
    res = obj.lookup_whois()
    ripe_handle = res['nets'][0]['handle']

    url = f'http://rest.db.ripe.net/ripe/role/{ripe_handle}'
    header = {'Accept': 'application/json'}

    response = requests.get(url, headers=header)
    x = response.content
    data = x.decode('utf-8').replace("'", '"')
    data = json.loads(data)
    role = data['objects']['object'][0]['attributes']['attribute'][0]['value']
    name = data['objects']['object'][0]['attributes']['attribute'][1]['value']
    address = data['objects']['object'][0]['attributes']['attribute'][2]['value']
    address2 = data['objects']['object'][0]['attributes']['attribute'][3]['value']
    phone = data['objects']['object'][0]['attributes']['attribute'][5]['value']
    fax = data['objects']['object'][0]['attributes']['attribute'][6]['value']
    modified = data['objects']['object'][0]['attributes']['attribute'][12]['value']
    mail = data['objects']['object'][0]['attributes']['attribute'][14]['value']

    ripe_object = {
        'role': role,
        'name': name,
        'address': [address, address2],
        'phone': phone,
        'fax': fax,
        'mail': mail,
        'last_modified': modified
    }
    print(ripe_object)
    return ripe_object
