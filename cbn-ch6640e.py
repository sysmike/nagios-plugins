#!/usr/bin/env python
import urllib2
import sys
from bs4 import BeautifulSoup

counter_downstream_snr = 0
counter_downstream_power_level = 0
counter_upstream_power_level = 0
counter2_downstream_snr = 0
counter2_downstream_power_level = 0
counter2_upstream_power_level = 0
warning = False
downstream_snr = []
downstream_power_level = []
upstream_power_level = []

# Fetch that shit
page_downstream = urllib2.urlopen('http://192.168.100.1/xml/DocsisDownstream.xml').read()
downstream = BeautifulSoup(page_downstream)
downstream.prettify()

page_upstream = urllib2.urlopen('http://192.168.100.1/xml/DocsisUpstream.xml').read()
upstream = BeautifulSoup(page_upstream)
upstream.prettify()

for snr in downstream.find_all("snr"):
	snr_tmp = downstream.snr.extract()
	snr_tmp = int(snr_tmp.renderContents())
	counter_downstream_snr += 1
	if downstream_snr < 35:
		warning = True
	downstream_snr.append(snr_tmp)

for power_level in downstream.find_all("power_level"):
	downstream_power_level_tmp = downstream.power_level.extract()
	downstream_power_level_tmp = int(downstream_power_level_tmp.renderContents()) + 60
	counter_downstream_power_level += 1
	if downstream_power_level < 50:
		warning = True
	downstream_power_level.append(downstream_power_level_tmp)

for power_level in upstream.find_all("power_level"):
	upstream_power_level_tmp = upstream.power_level.extract()
	upstream_power_level_tmp = int(upstream_power_level_tmp.renderContents()) + 60
	counter_upstream_power_level += 1
	if upstream_power_level < 100:
		warning = True
	upstream_power_level.append(upstream_power_level_tmp)

if warning == True:
	print "CRITICAL - check modem values! |",
else:
	print "OK - modem has " + str(counter_downstream_snr) + " downstream-channels and " + str(counter_upstream_power_level) + " upstream-channels |",

for item in downstream_snr:
	counter2_downstream_snr += 1
	print "snr" + str(counter2_downstream_snr) + "=" + str(item) + ";" ,

for item in downstream_power_level:
	counter2_downstream_power_level += 1
	print "power_level_down" + str(counter2_downstream_power_level) + "=" + str(item) + ";" ,

for item in upstream_power_level:
	counter2_upstream_power_level += 1
	print "power_level_up" + str(counter2_upstream_power_level) + "=" + str(item) + ";" ,

if warning == True:
	sys.exit(2)
else:
	sys.exit(0)
