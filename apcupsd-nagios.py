#!/usr/bin/env python
import subprocess
import sys

warning = False
critical = False

load = subprocess.check_output("/usr/sbin/apcaccess -p LOADPCT -u", shell=True).rstrip()
bcharge = subprocess.check_output("/usr/sbin/apcaccess -p BCHARGE -u", shell=True).rstrip()
timeleft = subprocess.check_output("/usr/sbin/apcaccess -p TIMELEFT -u", shell=True).rstrip()
linev = subprocess.check_output("/usr/sbin/apcaccess -p LINEV -u", shell=True).rstrip()
battv = subprocess.check_output("/usr/sbin/apcaccess -p BATTV -u", shell=True).rstrip()

if float(load) > 70.0:
	warning = True
elif float(load) > 90.0:
	citical = True

if float(linev) > 240.0:
	warning = True
elif float(linev) > 250.0:
	critical = True

if float(linev) < 210.0:
	warning = True
elif float(linev) < 200.0:
	critical = True

if float(battv) > 28.0:
	warning = True
elif float(battv) > 29.0:
	critical = True

if float(battv) < 11.0:
	warning = True
elif float(battv) < 10.0:
	critical = True

if float(timeleft) < 10.0:
	warning = True
elif float(timeleft) < 5.0:
	critical = True

if float(bcharge) < 50.0:
	warning = True
elif float(bcharge) < 20.0:
	critical = True

if warning == True:
	print "WARNING - check ups values! |",
elif critical == True:
	print "CRITICAL - check ups values! |",
else:
	print "Ok - ups looks good |",

print "battery-load=" + str(load) + ";" , "battery-charge=" + str(bcharge) + ";" , "timeleft=" + str(timeleft) + ";" , "linevolt=" + str(linev) + ";" , "batteryvolt=" + str(battv) + ";"

if warning == True:
	sys.exit(1)
elif critical == True:
	sys.exit(2)
else:
	sys.exit(0)
