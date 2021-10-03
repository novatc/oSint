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
    url = transform_url(url)
    list_of_nameserver = []
    list_of_mailservers =[]
    soa = ""
    list_of_txt = []
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [socket.gethostbyname('8.8.8.8')]

    answers = dns.resolver.resolve(url, 'MX')
    for rdata in answers:
        list_of_mailservers.append(rdata.exchange)
        print('Mail', rdata.exchange)

    answers = dns.resolver.resolve(url, 'NS')
    for rdata in answers.response.answer[0].items:
        list_of_nameserver.append(rdata)
        print('Nameserver', rdata)

    answers = dns.resolver.resolve(url, 'SOA')
    for rdata in answers.response.answer[0].items:
        soa = rdata
        print('SOA', rdata)

    answers = dns.resolver.resolve(url, 'TXT')
    for rdata in answers.response.answer[0].items:
        list_of_txt.append(rdata)
        print('TXT', rdata)
    return [list_of_mailservers, list_of_nameserver, soa, list_of_txt]

def dns_whois(url: str):
    url = transform_url(url)
    w = whois.whois(url)
    print(w)
    

# ip = find_ip("https://deananddavid.com/")
# dns_whois("https://deananddavid.com/")
