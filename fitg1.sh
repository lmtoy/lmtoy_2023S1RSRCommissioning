#! /usr/bin/env bash
#
#   for a true gauss the LineIntegral and LineFlux are statistically the same
#   flux = sqrt(2.pi) = 2.507
#   li: 2.50611 0.062951
#   lf: 2.50639 0.0385316
#
tmp=tmpg


for i in $(seq 1000); do
    # make a gauss, amp=1, center=0, width=1 with some noise
    # adding random scaling to Amp made no difference
    # adding small offset to center (B) made no difference
    A=$(nemoinp "rang(10,1)" seed=-3)
    A=1
    A=$(nemoinp "ranu(10,30)" seed=-3)    
    B=0.25
    B=0.0
    nemoinp -10:10:0.5 | tabmath  - - "$A*exp(-((%1-$B)**2)/2)+rang(0,0.02)" seed=-3 > $tmp.1
    li=$(tabint $tmp.1)
    # fit to a+b*exp(-(x-c)^2/(2*d^2))
    tabnllsqfit $tmp.1 fit=gauss1d > $tmp.2
    lf=$(txtpar $tmp.2 "%1*%2*sqrt(2*pi)" p0="b=",1,2 p1="d=",1,2)
    
    echo $li $lf
done
