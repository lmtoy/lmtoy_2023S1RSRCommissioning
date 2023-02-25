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
	w1=$(grep ^1 $log  | head -1 | txtpar - p0=1,8)
	w2=$(grep ^1 $log  | tail -1 | txtpar - p0=1,8)
	l1=$(grep ^rsr $log | head -1 | txtpar - p0=1,5)
	l2=$(grep ^rsr $log | tail -1 | txtpar - p0=1,5)
	p1=$(grep ^1 $log  | head -1 | txtpar -  p0=1,4)
	p2=$(grep ^1 $log  | tail -1 | txtpar -  p0=1,4)
	dp1=$(grep ^1 $log  | head -1 | txtpar -  p0=1,5)
	dp2=$(grep ^1 $log  | tail -1 | txtpar -  p0=1,5)
	#  mode=1
	echo "$obsnum $src  $f1 $f2  $l1 $l2  $p1 $p2"
	#  mode=2
	# echo "$obsnum $src  $p1 $p2  $dp1 $dp2"
	#  mode=3
	# echo "$obsnum $src  $w1 $w2"
    else
	echo "# $obsnum $src"
    fi
    
done

#  these are for flux2.tab for nemoplot access
echo '#PLOT grep I05189 flux2.tab   | tabhist - 3,4  0   80 resid=f'
echo '#PLOT grep I10565 flux2.tab   | tabhist - 3,4  0  160 resid=f'
echo '#PLOT grep I12112 flux2.tab   | tabhist - 3,4  0   80 resid=f'
echo '#PLOT grep I05189 flux2.tab   | tabplot - 3 4  0  80 0  80 dxcol=5 dycol=6'
echo '#PLOT grep I10565 flux2.tab   | tabplot - 3 4  0 160 0 160 dxcol=5 dycol=6'
echo '#PLOT grep I12112 flux2.tab   | tabplot - 3 4  0  80 0  80 dxcol=5 dycol=6'
