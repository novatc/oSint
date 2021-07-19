import json

from ipwhois import IPWhois

f = open('output.txt')
content = f.readlines()
result = {}
for line in content:
    res_json = {}
    line = line.strip()
    x = line.split(',')
    name = x[0]
    res_json['ip'] = name
    obj = IPWhois(x[1])
    res = obj.lookup_whois()
    address = res['nets'][0]['address'].strip()
    res_json['address'] = address
    result[res_json['ip']] = res_json


print(json.dumps(result, indent=4))
f = open('result.json', "x")
f.write(json.dumps(result, indent=4))
