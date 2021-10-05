from ipwhois import IPWhois
from pprint import pprint
obj = IPWhois('195.60.121.167')
res=obj.lookup_whois()
pprint(res)
