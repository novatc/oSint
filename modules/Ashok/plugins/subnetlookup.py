#!/usr/bin/python3
from requests import get


def subnetlookup(cidr):
	response = get('https://api.hackertarget.com/subnetcalc/?q='+ cidr).text
	print(response)

	return convert_response_to_list(response)

def convert_response_to_list(response) -> list:
	"""Converts a response sting that contains a single level
	
	Args:
		response (string): the response.text

	Returns:
		list: list containing response objects
	"""
	return response.splitlines()