#!/usr/bin/python3
from requests import get
def sub(domain):
	response = get('https://api.hackertarget.com/hostsearch/?q=' + domain).text
	print(response,"\n")

	return convert_response_to_list(response)

def convert_response_to_list(response) -> list:
	"""Converts a response sting that contains a single level
	
	Args:
		response (string): the response.text

	Returns:
		list: list containing response objects
	"""
	dict = {}
	temp = response.splitlines()
	for t in temp:
		items = t.split(',')
		dict[items[0]] = items[1]

	return dict

