#!/usr/bin/python3
import sys
from requests import get
# Outdated. Key required
def nmap(domain):
	response = get('http://api.hackertarget.com/nmap/?q=' + domain).text
	print(response)

	return response