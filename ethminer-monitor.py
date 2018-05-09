#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import subprocess
from time import sleep

result = []

def get_miner_info():

	global version
	global uptime
	global hashrate
	global hardware
	global temperature_gpu
	global fanspeed_gpu
	global pool

	cmd = '''echo '{"method": "miner_getstat1", "jsonrpc": "2.0", "id": 5 }' | timeout 2 nc 127.0.0.1 8085'''
	s = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	rsp = s.communicate()[0]
	data = json.loads(rsp)
	version = data['result'][0]
	uptime = data['result'][1]
	hashrate = data['result'][3]
	hashrate = hashrate.split(";")
	hardware = data['result'][6]
	hardware = hardware.split(";")
	temperature_gpu = hardware[::2]
	fanspeed_gpu = hardware[1::2]
	pool = data['result'][7]
	pool = pool.split(";")

def print_result():

	problem = False

	gpu = 0
	for item in hashrate:
		if int(item) < 20000:
			problem = True
		tmp = "hashrate_gpu" + str(gpu) + "=" + str(item)
		result.append(tmp)
		gpu = gpu + 1

	gpu = 0
	for item in temperature_gpu:
		if int(item) > 70:
			problem = True
		tmp = "temperature_gpu" + str(gpu) + "=" + str(item.lstrip())
		result.append(tmp)
		gpu = gpu + 1

	gpu = 0
	for item in fanspeed_gpu:
		tmp = "fanspeed_gpu" + str(gpu) + "=" + str(item)
		result.append(tmp)
		gpu = gpu + 1

	for item in pool:
		tmp = "pool=" + str(item)
		result.append(tmp)

	if problem == True:
		print("Something is wrong with this rig |"),
		print("version=" + str(version) + " uptime=" + str(uptime)),
		for item in result:
	    		print item,
		sys.exit(1)
	else:
		print("This mining rig is operating in its specified parameters |"),
		print("version=" + str(version) + " uptime=" + str(uptime)),
		for item in result:
	    		print item,
    	sys.exit(0)

get_miner_info()
print_result()
