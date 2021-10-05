#!/usr/bin/python3
from requests import get


def httpheader(url):
	response = get('https://api.hackertarget.com/httpheaders/?q=' + url).text
	print(response)

	return convert_response_to_dict(response)

def convert_response_to_dict(response):
	"""Converts a response sting that contains multiple layers
	
	Args:
		response (string): the response.text

	Returns:
		dict: dict containing response objects
	"""
	dict = {}
	temp = response.splitlines()
	index = 0
	for t in temp:
		if t == '':
			continue
		if ':' in t:
			items = t.split(': ')
			dict[index][items[0]] = items[1]
		else:
			index = t
			dict[index] = {}
	return dict