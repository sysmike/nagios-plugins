#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import subprocess
from time import sleep
from argparse import ArgumentParser

result = []

parser = ArgumentParser(add_help=False)
parser.add_argument('-H', '--hostname', dest='hostname', metavar='ADDRESS', required=True, help="host name or IP address")
args = parser.parse_args()

def get_miner_info():

	global version
	global uptime
	global hashrate
	global hardware
	global temperature_gpu
	global power_usage
	global fanspeed_gpu
	global pool

	cmd = '''echo '{"method": "miner_getstathr", "jsonrpc": "2.0", "id": 5 }' | timeout 2 nc ''' + str(args.hostname) + ' 8085'
	s = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	rsp = s.communicate()[0]
	data = json.loads(rsp)
	version = data['result']['version']
	uptime = data['result']['runtime']
	hashrate = data['result']['ethhashrates']
	power_usage = data['result']['powerusages']
	temperature_gpu = data['result']['temperatures']
	fanspeed_gpu = data['result']['fanpercentages']
	pool = data['result']['pooladdrs']

def print_result():

	problem = False

	gpu = 0
	for item in hashrate:
		if int(item) < 20000:
			problem = True
		item = int(item) / 1000
		tmp = "hashrate_gpu" + str(gpu) + "=" + str(item)
		result.append(tmp)
		gpu = gpu + 1

	gpu = 0
	for item in temperature_gpu:
		if int(item) > 70:
			problem = True
		tmp = "temperature_gpu" + str(gpu) + "=" + str(item)
		result.append(tmp)
		gpu = gpu + 1

	gpu = 0
	for item in power_usage:
		if int(item) > 120:
			problem = True
		if int(item) < 60:
			problem = True
		tmp = "powerusage_gpu" + str(gpu) + "=" + str(item)
		result.append(tmp)
		gpu = gpu + 1

	gpu = 0
	for item in fanspeed_gpu:
		tmp = "fanspeed_gpu" + str(gpu) + "=" + str(item)
		result.append(tmp)
		gpu = gpu + 1

	item = pool
	tmp = "pool=" + str(item)
	result.append(tmp)

	if problem == True:
		print("Something is wrong with this rig |"),
		print("version=" + str(version) + " uptime=" + str(uptime)),
		for item in result:
	    		print item,
		sys.exit(1)
	else:
		print("This mining rig is operating in its specified parameters on " + str(pool) + " |"),
		print("version=" + str(version) + " uptime=" + str(uptime)),
		for item in result:
	    		print item,
    	sys.exit(0)

get_miner_info()
print_result()
