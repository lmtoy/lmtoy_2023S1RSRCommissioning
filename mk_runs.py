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

on['I05189']  = [-103372,-103373,-103380,-103381,-103418,-103419, 103509, 103510,
                  103713, 103714, 104425, 104426, 104531, 104532,
                  104659, 104660, 104785, 104786,-104911,-104912,
                  105232, 105233, 105383, 105384, 105390, 105391,
                  106002, 106003, 106167, 106168, 106683, 106684,]

on['I10565']  = [ 103436, 103437, 103439, 103440, 103843, 103844, 103847, 103848,
                  104038, 104039, 104083, 104084, 104086, 104087, 104139, 104140,
                  104991, 104992,
                  105058, 105059, 105285, 105286, 105403, 105404, 105735, 105736,
                  105967, 105968, 105979, 105980, 106189, 106190,
                  106324, 106325, 106427, 106428, 106476, 106477, 106520, 106521,
                  106573, 106574, 106647, 106648, 106687, 106688, 107021, 107022,
                  107169, 107170, 107301, 107302, 107307, 107308, 107324, 107325,
                  108812, 108813, 108818, 108819, 108901, 108902,]


on['I12112']  = [-103350,-103351, 103851, 103852, 104163, 104164, 104397, 104398,
                  106820, 106821,
                  107405, 107406, 109015, 109016, 109036, 109037, 109118, 109119,
                  109237, 109238]

on['I17208']  = [ 103855, 103856, 106619, 106620, 106970, 106971, 108839, 108840,
                  109165, 109166]


on['VIIZw31'] = [ 103505, 103506, 103779, 103780, 104526, 104527]


#       common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1['I10565']     = "linecheck=1 cthr=0.015"
pars1['I05189']     = "linecheck=1 cthr=0.015"
pars1['I12112']     = "linecheck=1 cthr=0.015"   # badcb=1/1,2/0,2/1,2/2,2/3,2/4,2/5,3/0,3/1,3/2,3/3,3/4,3/5"
pars1['I17208']     = "linecheck=1 cthr=0.015"
pars1['VIIZw31']    = "linecheck=1 cthr=0.015"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2['I10565']     = "srdp=1"
pars2['I05189']     = "srdp=1"
pars2['I12112']     = "srdp=1"
pars2['I17208']     = "srdp=1"
pars2['VIIZw31']    = "srdp=1"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2)
