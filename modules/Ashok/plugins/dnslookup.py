#!/usr/bin/python3
from requests import get


def dnslookup(url):
	response = get('https://api.hackertarget.com/dnslookup/?q=' + url).text
	print(response)

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
		items = t.split(' : ')
		dict[items[0]] = items[1]

	return dict