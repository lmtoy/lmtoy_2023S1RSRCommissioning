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
theory one should be able to work from scratch:

      source_obsnum.sh -l  2023S1RSRCommissioning > ./mk_runs_new.py

