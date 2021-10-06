#!/usr/bin/python3
import os
import argparse


from modules.Ashok.core.nmap import nmap
from modules.Ashok.core.gitbot import gitusers,gitemails
from modules.Ashok.core.linkextractor import extract
from modules.Ashok.core.bannergrab import banner
from modules.Ashok.core.subdomains import sub
from modules.Ashok.core.geoip import geo
from modules.Ashok.core.wayback import waybackurl,waybackrobots,waybackjson
from modules.Ashok.core.gdork import dork
from modules.Ashok.plugins.dnslookup import dnslookup
from modules.Ashok.plugins.subnetlookup import subnetlookup
from modules.Ashok.plugins.httpheaders import httpheader
from modules.Ashok.plugins.techanalyzer import techno
import sys

dorknumber = 10
ascii = """


    ▄▄▄        ██████  ██░ ██  ▒█████   ██ ▄█▀
    ▒████▄    ▒██    ▒ ▓██░ ██▒▒██▒  ██▒ ██▄█▒ 
    ▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓███▄░ 
    ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒██   ██░▓██ █▄ 
    ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░ ████▓▒░▒██▒ █▄
    ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▒ ▓▒
    ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒ ▒░
    ░   ▒   ░  ░  ░   ░  ░░ ░░ ░ ░ ▒  ░ ░░ ░  > Recon Swiss Army Knife
        ░  ░      ░   ░  ░  ░    ░ ░  ░  ░      v1.1   
    """

def print_logo():
    print(ascii)
    print("""
    Author  : Ankit Dobhal | Break||The||Code
    Github  : https://github.com/ankitdobhal
    Website : http://ankitdobhal.github.io/ 
    =========================================
        """)
    

def ashok(url):
    """ Function to call ashok library

    Args:
        url ([type]): URL (https://www.example.com)
        
    """
    ashok_result = {}
    ashok_result['ascii'] = ascii
    # TODO nutzen von Domains wie http://example.com etc. ermöglichen 
    print(url)
    protocol = url.split('/')[0]
    third_level_domain = url.split('/')[2].split('.')[0]
    first_level_domain = url.split('/')[2].split('.')[1]
    top_level_domain = url.split('/')[2].split('.')[2]

    url = protocol + '//' + third_level_domain + '.' + first_level_domain + '.' + top_level_domain

    domain = first_level_domain + '.' + top_level_domain
    print_logo()
    
    # Extract Http Headers from single url
    print("[+] Extracing http headers of target url")
    result = httpheader(url)
    ashok_result['headers'] = result
    print()

    # Dns Lookup of single target domain
    print("[+] DNS lookup of target domain")
    result = dnslookup(domain)
    ashok_result['dns'] = result
    print()
    print(ashok_result['dns'])
    print(ashok_result['dns']['A'])
    ip = ashok_result['dns']['A']
    port = None

    # Subdomain Lookup of single target domain
    print("[+] Subdomain lookup from target domain")
    result = sub(domain)
    ashok_result['subdomain'] = result
    print()

    # Port Scan using nmap of single target domain 
    # Outdated. Key required. Use nmap instead
    # print("[+] Port scanning of target domain")
    # result = nmap(domain)
    # ashok_result['nmap'] = result
    # print()

    # TODO if needed
    # Extract data using Github username of target
    # print("[+] Extract data using Github username of target")
    # result_users = gitusers(username)
    # result_emails = gitemails(username)
    # ashok_result['username'] = {
    #     'users': result_users,
    #     'emails': result_emails
    # }
    # print()

    # Detect Cms of target url
    # Replaced with wappalyzer
    # print("[+] Detecting CMS with Identified Technologies and Custom Headers from target url")
    # result = techno(url)
    # ashok_result['cms'] = result
    # print()

    # Extract links from target domain
    print("[+] Extracting all hidden and visiable links from target url")
    result = extract(domain)
    ashok_result['extract'] = result
    print()

    # Subnetlookup of target CIDR
    # result = subnetlookup(ip + '/' + port)
    # ashok_result['cidr'] = result
    # print()

    # Banner grabbing of target ip address
    print("[+] Banner Grabing from target ip address")
    print(ip)
    result = banner(ip)
    ashok_result['banner'] = result
    print()

    # GeoIP lookup of target ip address
    print("[+] Geoip lookup of target Ip address")
    result = geo(ip)
    ashok_result['geoip'] = result
    print()

    # Dump internet-archive machine with json output for single url
    # print("[+] Dumping and Crawling Internet Archive Machine With Ashok")
    # result_url = waybackurl(url)
    # result_robots = waybackrobots(url)
    # result_json = waybackjson(url)
    # ashok_result['wayback'] = {
    #     'url': result_url,
    #     'robots': result_robots,
    #     'json': result_json
    # }
    print()

    # Google dorking using number of results as dorknumber
    # Not needed ?
    # result = dork(dorknumber)
    # ashok_result['dorknumber'] = result
    # print()

    return ashok_result
