#! /usr/bin/env python
#
#   script generator for project=2023S1RSRCommissioning
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

on['I05189']  = [ 103372, 103373, 103380, 103381, 103418, 103419, 103509, 103510,
                  103713, 103714, 104425, 104426, 104531, 104532,
                  104659, 104660, 104785, 104786, 104911, 104912,]


on['I10565']  = [ 103436, 103437, 103439, 103440, 103843, 103844, 103847, 103848,
                  104038, 104039, 104083, 104084, 104086, 104087, 104139, 104140,
                  104991, 104992,]

on['I12112']  = [ 103350, 103351, 103851, 103852, 104163, 104164, 104397, 104398]

on['I17208']  = [ 103855, 103856]

on['VIIZw31'] = [ 103505, 103506, 103779, 103780, 104526, 104527]


#       common parameters per source on the first dryrun (run1, run2)
pars1 = {}

pars1['I10565']     = "linecheck=1 srdp=1"
pars1['I05189']     = "linecheck=1 srdp=1"
pars1['I12112']     = "linecheck=1 srdp=1"
pars1['VIIZw31']    = "linecheck=1 srdp=1"
pars1['I17208']     = "linecheck=1 srdp=1"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}

pars2['I10565']     = ""
pars2['I05189']     = ""
pars2['I12112']     = ""
pars2['VIIZw31']    = ""
pars2['I17208']     = ""

runs.mk_runs(project, on, pars1, pars2)
