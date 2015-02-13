#!/usr/bin/env python
import subprocess
load = subprocess.check_output("apcaccess.exe -u -p LOADPCT", shell=True).rstrip()
bcharge = subprocess.check_output("apcaccess.exe -u -p BCHARGE", shell=True).rstrip()
timeleft = subprocess.check_output("apcaccess.exe -u -p TIMELEFT", shell=True).rstrip()
linev = subprocess.check_output("apcaccess.exe -u -p LINEV", shell=True).rstrip()
battv = subprocess.check_output("apcaccess.exe -u -p BATTV", shell=True).rstrip()

print "Ok |" , "battery-load=" + str(load) + ";" , "battery-charge=" + str(bcharge) + ";" , "timeleft=" + str(timeleft) + ";" , "linevolt=" + str(linev) + ";" , "batteryvolt=" + str(battv) + ";"