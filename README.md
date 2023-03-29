# 2023S1RSRCommissioning

This is mostly for linechecks now, but also includes historic data from 2018 (50m), 

# sources

The command

      lmtinfo.py grep 2023 LineCheck Bs | awk '{print $5}' | sort | uniq -c

should give something like this

...

According to http://wiki.lmtgtm.org/lmtwiki/RSR%20Spectral%20Line%20Check?action=AttachFile&do=view&target=LineCheckSources.pdf
the fluxes of the sources we cover here are (for 32m dish)

      I10565      68 mK
      I17208      60 mK
      I23365      16 mK


# How to run

Normally the command
     
     ./mk_runs.py
	 
generates the text file for slurm, but currently RSR cannot run in parallel. But when it does,
this will be the command

      sbatch_lmtoy.sh linecheck.run1

to run *everything* (historic data too).  And

      sbatch_lmtoy.sh linecheck.run2
	  
to run the combinations.


Here's a way to make a new mk_runs.py file. Normally one would view and diff/merge it with an existing one, but in
theory one should be able to work from scratch::

      source_obsnum.sh -l  2023S1RSRCommissioning > ./mk_runs_new.py

the output of which can be compared to mk_runs.py

# Reduction comments

## I05189

I05189 had two bad obsnums: 104911 and 104912 (rms/rms0 = 4.2 and 3.6)
The resulting 103372_106684 has rms/rms0 = 7.9
After removing them this went to 2.8

I05189    - still has some bad ones

remove the bad LO2 cases (103372 103373  103380 103381) - now rms/rms0 = 1.37

now the bad band 0 show up:    103418 103419 - now rms/rms0 = 1.31. Not much lower, but spectrum is clean.

peak=32.581 vs. peak=28.734

## I12112    - has bad obsnums

First two were labeled that the 2nd LO was off.  Still, band 5 looked ok, though the sum and driver were discrepant

After taking out 103350 and 103351 , rms/rm0 went from 2.8 to 1.4 and look much better.


TEST: should try banning all chassis 2,3 from accumulations?   This gives rms/rms0=1.46

Discrepent flux from driver vs. sum !!! 

obsnums=103851,103852,104163,104164,104397,104398                => peak=40.564 22.625
rms=0.795 mK base=-0.103 mK peak=40.564 mK line=107.448 GHz sigma=0.0548657 GHz
rms=0.688 mK base=-0.470 mK peak=22.625 mK line=107.445 GHz sigma=0.0518511 GHz 

obsnums=103851,103852,104163,104164,104397,104398,106820,106821  => peak=38.055 21.715
rms=0.761 mK base=-0.090 mK peak=38.055 mK line=107.448 GHz sigma=0.0556704 GHz
rms=0.564 mK base=-0.452 mK peak=21.715 mK line=107.443 GHz sigma=0.0531466 GHz

- and if chassis 2 and 3 removed [badcb=1/1,2/0,2/1,2/2,2/3,2/4,2/5,3/0,3/1,3/2,3/3,3/4,3/5]
rms=0.550 mK base=-0.059 mK peak=26.621 mK line=107.444 GHz sigma=0.0528601 GHz 
rms=0.553 mK base=-0.436 mK peak=21.239 mK line=107.443 GHz sigma=0.0526131 GHz

interesting that if chassis 2 and 3 are removed, the rms is lower!

## I10565

peak=102.843 vs. peak=80.461

## VIIZw31

looks fine

peak=101.791 vs. peak=98.261

## I17208

looks fine.

peak=104.759 vs. peak=95.762 mK
