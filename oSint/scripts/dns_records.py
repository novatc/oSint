import json
import socket
from urllib.parse import urlparse
import dns.resolver
import whois


def transform_url(url: str):
    parse_object = urlparse(url)
    return str(parse_object.netloc)


def find_ip(url: str) -> str:
    url = transform_url(url)

    return socket.gethostbyname(url)


def get_dns_record(url: str):
    record = {}
    url = transform_url(url)
    list_of_nameservers = []
    list_of_mailservers = []
    list_of_txt = []

    ns = dns.resolver.resolve(url, 'NS')
    mx = dns.resolver.resolve(url, 'MX')
    soa = dns.resolver.resolve(url, 'SOA')
    txt = dns.resolver.resolve(url, 'TXT')
    for data in ns:
        list_of_nameservers.append(str(data))
    for data in mx:
        list_of_mailservers.append(str(data))

    for data in txt:
        list_of_txt.append(data)

    #record['NS'] = list_of_nameservers
    #record['MX'] = list_of_mailservers
    record['SOA'] = soa
    record['TXT'] = list_of_txt
    return record


def dns_whois(url: str):
    url = transform_url(url)
    w = whois.whois(url)



