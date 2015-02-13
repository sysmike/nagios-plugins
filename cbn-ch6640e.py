#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup

a = str(0)
b = str(0)
c = str(0)

page_downstream = urllib2.urlopen('http://192.168.100.1/xml/DocsisDownstream.xml').read()
downstream = BeautifulSoup(page_downstream)
downstream.prettify()

page_upstream = urllib2.urlopen('http://192.168.100.1/xml/DocsisUpstream.xml').read()
upstream = BeautifulSoup(page_upstream)
upstream.prettify()

print "Ok |",
#Downstream
for snr in downstream.find_all("snr"):
	result1 = downstream.snr.extract()
	a = int(a) + 1
	print "snr" + str(a) + "=" + str(result1.renderContents()) + ";" ,

for power_level in downstream.find_all("power_level"):
	result2 = downstream.power_level.extract()
	b = int(b) + 1
	result22 = int(result2.renderContents()) + 60
	print "power_level_down" + str(b) + "=" + str(result22) + ";" ,

#Upstream
for power_level in upstream.find_all("power_level"):
	result3 = upstream.power_level.extract()
	c = int(c) + 1
	result33 = int(result3.renderContents()) + 60
	print "power_level_up" + str(c) + "=" + str(result33) + ";" ,
