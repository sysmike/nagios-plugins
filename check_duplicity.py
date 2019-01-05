#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re

filepath = '/var/log/duplicity.txt'

with open(filepath, 'r') as f:
     for line in f:
        if "ElapsedTime" in line:
             elapsedtime = line
             elapsedtime = elapsedtime.split()
        if "SourceFiles" in line:
             sourcefiles = line
             sourcefiles = int("".join(filter(str.isdigit, sourcefiles)))
        if "DeletedFiles" in line:
             deletefiles = line
             deletefiles = int("".join(filter(str.isdigit, deletefiles)))
        if "ChangedFiles" in line:
             changedfiles = line
             changedfiles = int("".join(filter(str.isdigit, changedfiles)))
        if "DeltaEntries" in line:
             deltaentries = line
             deltaentries = int("".join(filter(str.isdigit, deltaentries)))
        if "RawDeltaSize" in line:
             rawdeltasize = line
             rawdeltasize = rawdeltasize.split()
        if "TotalDestinationSizeChange" in line:
             totaldestinationsizechange = line
             totaldestinationsizechange = totaldestinationsizechange.split()
        if "StartTime" in line:
             starttime = line
             starttime = starttime.split()
             starttime = ' '.join(starttime[2:7])
             starttime = starttime.replace('(', '')
             starttime = starttime.replace(')', '')
        if "Errors" in line:
             errors = line
             errors = int("".join(filter(str.isdigit, errors)))

if errors > 0:
    print('CRITICAL - error(s) on last run. The last backup ran on ' + starttime + ' and took ' + elapsedtime[1] + 's. | elapsedtime=' + elapsedtime[1]
 + ' sourcefiles=' + str(sourcefiles) + ' deletefiles=' + str(deletefiles) + ' changedfiles=' + str(changedfiles)
 + ' deltaentries=' + str(deltaentries) + ' rawdeltasize=' + rawdeltasize[1] + ' totaldestinationsizechange='
 + totaldestinationsizechange[1] + ' errors=' + str(errors))
    sys.exit(2)
else:
    print('OK - The last backup ran on ' + starttime + ' and took ' + elapsedtime[1] + 's. | elapsedtime=' + elapsedtime[1]
 + ' sourcefiles=' + str(sourcefiles) + ' deletefiles=' + str(deletefiles) + ' changedfiles=' + str(changedfiles)
 + ' deltaentries=' + str(deltaentries) + ' rawdeltasize=' + rawdeltasize[1] + ' totaldestinationsizechange='
 + totaldestinationsizechange[1] + ' errors=' + str(errors))
    sys.exit(0)
