#!/usr/bin/python3
import os
import requests as res
import json
def gitusers(username):
	response = res.get("https://api.github.com/users/" + username).text
	data = json.loads(response)
	print("[+] Dumping Sensitive information from github")
	os.system('tput setaf 9')
	print("[+] Name : ", str(data['name']))
	print("[+] Location : ", str(data['location']))
	print("[+] Website : ", str(data['blog']))
	print("[+] Number of public github Repository : " ,str(data['public_repos']))
	print("[+] Number of public gist Repository : ",str(data['public_gists']))

	result = {
		'name': data['name'],
		'location': data['location'],
		'website': data['Website'],
		'public_repos': data['public_repos'],
		'public_gists': data['public_gists']
	}
	return result

def gitemails(username):
	try:
		response = res.get("https://api.github.com/users/%s/events/public" %(username))
		jsn = response.json()
		data = jsn[0]
		dump = data["payload"]["commits"][0]["author"]["email"]
		print("[+] Email data : ", dump)	

		return dump
		
	except KeyError:
		os.system('tput setaf 12')
		print("[+] Aww Snap Unable to find out the email address!")

	