#! /usr/bin/env python
#
#   script generator for project=
#
#   lmtinfo.py grep LineCheck Bs

import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

#  2023S1RSRCommissioning 
project="linecheck"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['I10565'] = [103436, 103437,  103439, 103440]

on['I05189'] = [103372, 103373, 103380, 103381, 103418, 103419, 103509, 103510]

on['I12112'] = [103350, 103351]

on['VIIZw31'] = [103505, 103506]


#       common parameters per source on the first dryrun (run1, run2)
pars1 = {}

pars1['I10565']     = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I05189']     = "xlines=110.53,0.25"
pars1['I12112']     = "xlines=107.40,0.25"
pars1['VIIZw31']    = "xlines=109.34,0.25"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['I10565']     = ""
pars2['I05189']     = ""
pars2['I12112']     = ""
pars2['VIIZw31']    = ""

runs.mk_runs(project, on, pars1, pars2)
