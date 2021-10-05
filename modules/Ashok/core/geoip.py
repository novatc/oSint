#!/usr/bin/python3
from requests import get
def geo(ip):
	response = get('https://api.hackertarget.com/geoip/?q=' + ip).text
	print(response,"\n")

	return convert_response_to_dict(response)

def convert_response_to_dict(response) -> dict:
	"""Converts a response sting that contains a single layer
	
	Args:
		response (string): the response.text

	Returns:
		dict: dict containing response objects
	"""
	dict = {}
	temp = response.splitlines()
	for t in temp:
		items = t.split(': ')
		if len(items)==1:
			dict[items[0]] = ''
		else:
			dict[items[0]] = items[1]
	return dict