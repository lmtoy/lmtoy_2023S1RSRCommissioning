#! /usr/bin/env bash
#
# Example output from rsr_peak.log
#  peak   a (mK)        b (mK)           c (GHz)               d (Ghz)
# 1 1.08929 0.521246 124.966 2.21946 110.518 0.000651176 0.0322452 0.000685516

for obsnum in $*; do
    log=$obsnum/rsr_peaks.log
    src=$(nemopars src $obsnum/lmtoy_$obsnum.rc | tail -1)
    if [ -e $log ]; then
	f1=$(grep ^1 $log  | head -1 | txtpar - "%1/1000/%2*%3*2.507*c/1000"  p0=1,4 p1=1,6 p2=1,8)
	f2=$(grep ^1 $log  | tail -1 | txtpar - "%1/1000/%2*%3*2.507*c/1000"  p0=1,4 p1=1,6 p2=1,8)
	l1=$(grep ^rsr $log | head -1 | txtpar - p0=1,5)
	l2=$(grep ^rsr $log | tail -1 | txtpar - p0=1,5)
	p1=$(grep ^1 $log  | head -1 | txtpar -  p0=1,4)
	p2=$(grep ^1 $log  | tail -1 | txtpar -  p0=1,4)
	dp1=$(grep ^1 $log  | head -1 | txtpar -  p0=1,5)
	dp2=$(grep ^1 $log  | tail -1 | txtpar -  p0=1,5)
	#  mode=1
	#echo $obsnum $src a $f1 b $f2 c $l1 d $l2 e $p1 $p2
	#  mode=2
	echo $obsnum $src  $p1 $p2 $dp1 $dp2
    else
	echo "# $obsnum $src"
    fi
    
done

