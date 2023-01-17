#! /usr/bin/env python
#
#   script generator for project=
#
#   lmtinfo.py grep LineCheck Bs

import os
import sys

#  2023S1RSRCommissioning 
project="linecheck"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['I10565'] = [103436, 103437,  103439, 103440]

on['I05189'] = [103372, 103373, 103380, 103381, 103418, 103419]

on['I12112'] = [103350, 103351]


#       common parameters per source on the first dryrun (run1, run2)
pars1 = {}

pars1['I10565']     = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I05189']     = "xlines=107.6,0.3"    # needs accuracy
pars1['I12112']     = "xlines=107.40,0.25"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['I10565']     = ""
pars2['I05189']     = ""
pars2['I12112']     = ""

# below here no need to change code
# ========================================================================

#        helper function for populating obsnum dependant argument -- deprecated
def getargs3(obsnum):
    """ search for <obsnum>.args
    """
    f = "%d.args" % obsnum
    if os.path.exists(f):
        lines = open(f).readlines()
        args = ""
        for line in lines:
            if line[0] == '#': continue
            args = args + line.strip() + " "
        return args
    else:
        return ""

#        specific parameters per obsnum will be in files <obsnum>.args -- deprecated
pars3 = {}
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        pars3[o] = getargs3(o)

#        obsnum.args is alternative single file pars file to set individual parameters
pars4 = {}
if os.path.exists("obsnum.args"):
    lines = open("obsnum.args").readlines()
    for line in lines:
        if line[0] == '#': continue
        w = line.split()
        pars4[int(w[0])] = w[1:]
        print('PJT',w[0],w[1:])

def getargs(obsnum):
    """ search for <obsnum> in obsnum.args
    """
    args = ""
    if obsnum in pars4.keys():
        print("PJT2:",obsnum,pars4[obsnum])
        for a in pars4[obsnum]:
            args = args + " " + a
    return args

run1  = '%s.run1'  % project
run1a = '%s.run1a' % project
run1b = '%s.run1b' % project
run2  = '%s.run2' % project
run2a = '%s.run2a' % project

fp1 = open(run1,  "w")
fp2 = open(run1a, "w")
fp3 = open(run1b, "w")

fp4 = open(run2,  "w")
fp5 = open(run2a, "w")

#                           single obsnum
n1 = 0
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        cmd1 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1 %s %s" % (o,s,pars1[s], pars2[s], getargs(o))
        cmd2 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1" % (o,s,pars1[s])
        cmd3 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 %s" % (o,s,pars2[s], getargs(o))
        fp1.write("%s\n" % cmd1)
        fp2.write("%s\n" % cmd2)
        fp3.write("%s\n" % cmd3)
        n1 = n1 + 1

#                           combination obsnums
n2 = 0        
for s in on.keys():
    obsnums = ""
    n3 = 0
    for o1 in on[s]:
        o = abs(o1)
        if o1 < 0: continue
        n3 = n3 + 1
        if obsnums == "":
            obsnums = "%d" % o
        else:
            obsnums = obsnums + ",%d" % o
    print('%s[%d/%d] :' % (s,n3,len(on[s])), obsnums)
    cmd4 = "SLpipeline.sh _s=%s admit=0 restart=1 obsnums=%s" % (s, obsnums)
    cmd5 = "SLpipeline.sh _s=%s admit=1 srdp=1  obsnums=%s" % (s, obsnums)
    fp4.write("%s\n" % cmd4)
    fp5.write("%s\n" % cmd5)
    n2 = n2 + 1

print("A proper re-run of %s should be in the following order:" % project)
print(run1a)
print(run2)
print(run1b)
print(run2a)
print("Where there are %d single obsnum runs, and %d combination obsnums" % (n1,n2))

