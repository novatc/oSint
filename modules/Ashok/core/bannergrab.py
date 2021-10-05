#!/usr/bin/python3
from requests import get
import json
def banner(ip):
	response = get('https://api.hackertarget.com/bannerlookup/?q=' + ip)
	print(response.text)
	try:
		return response.json()
	except Exception:
		return {}