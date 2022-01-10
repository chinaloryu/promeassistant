#!/bin/env python3
# -*- coding: UTF-8 -*-

import requests,json
import sys,getopt

def pro_query(auth_key = '', url = ''):
	url = url
	auth_key = auth_key
	headers = {}
	headers['Authorization'] = "Bearer "+auth_key
	headers['content-type'] = 'application/json'
	result = requests.get(url, headers = headers)
	return result

def pro_add(auth_key = '', url = '', name = '', type = 'prometheus',jsonData = {'httpMethod':'GET'}, readOnly = False, access = 'proxy'):
	url = url
	auth_key = auth_key
	headers = {}
	data = {}
	headers['Authorization'] = "Bearer "+auth_key
	headers['content-type'] = 'application/json'
	data['name'] = name
	data['type'] = type
	data['jsonData'] = jsonData
	data['readOnly'] = readOnly
	data['access'] = access
	result = requests.post(url, headers = headers, data = json.dumps(data))
	return result
	print(result)


if __name__ == '__main__':
	url = ''
	auth_key = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"-h-m:-k:-n:-u:",["help","method=","key=","name=", "url="])
	except getopt.GetoptError:
		print('test.py -q')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ['-k','--key']:
			auth_key = arg
			print(auth_key)
		if opt in ['-m','--method']:
			print(f"auth_key is: {auth_key}")
			method = arg
		if opt in ['-n', '--name']:
			name = arg
		if opt in ['-u', '--url']:
			url = arg
	print(f"method is: {method},auth_key is: {auth_key}")
	match method:
		case 'query':
			r = pro_query(auth_key = auth_key, url = url)
			print(r.json())
		case 'create':
			pass
		case 'add':
			r = pro_add(auth_key = auth_key, url = url, name = name)
			print(r.json())
		case 'delete':
			pass

	# if method == 'query':
	# 	r = pro_query(auth_key = auth_key)
	# 	print(r.json())