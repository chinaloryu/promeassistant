#!/bin/env python3
# -*- coding: UTF-8 -*-

import requests,json
import sys,getopt

def pro_query(auth_key = '', url = '' ,name = name ):
	url = url
	auth_key = auth_key
	headers = {}
	headers['Authorization'] = "Bearer "+auth_key
	headers['content-type'] = 'application/json'
	result = requests.get(url, headers = headers)
	return result

def pro_add(auth_key = '', url = '', ds_url = 'http://localhost:9090', name = '', type = 'prometheus',jsonData = {'httpMethod':'GET'}, readOnly = False, access = 'proxy'):
	url = url
	auth_key = auth_key
	headers = {}
	data = {}
	headers['Authorization'] = "Bearer "+auth_key
	headers['content-type'] = 'application/json'
	data['name'] = name
	data['type'] = type
	data['jsonData'] = jsonData
	data['url'] = ds_url
	data['readOnly'] = readOnly
	data['access'] = access
	result = requests.post(url, headers = headers, data = json.dumps(data))
	return result
	print(result)

def pro_modify(url = '', name = name ):
	url = url
	headers = {}
	headers['Authorization'] = "Bearer "+auth_key
	headers['content-type'] = 'application/json'


if __name__ == '__main__':
	url = ''
	auth_key = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"-h-m:-k:-n:-u:-s:",["help","method=","key=","name=", "url=", "ds_url="])
	except getopt.GetoptError:
		print('usage:\ntest.py -h')
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
		if opt in ['-s', '--ds_url']:
			ds_url = arg
	print(f"method is: {method},auth_key is: {auth_key}")
	match method:
		case 'query':
			r = pro_query(auth_key = auth_key, url = url)
			print(r.json())
		case 'modify':
			pass
		case 'add':
			d = {}
			r = pro_query(auth_key = auth_key, url = url, name = name )
			# r = pro_add(auth_key = auth_key, url = url, name = name, ds_url = ds_url)
			d = r.json()
			if name in d['name']:
				print(f"{name} already in datasource")
			else:
				r = pro_add(auth_key = auth_key, url = url, name = name, ds_url = ds_url)
				print(r.json())
		case 'delete':
			pass

	# if method == 'query':
	# 	r = pro_query(auth_key = auth_key)
	# 	print(r.json())
