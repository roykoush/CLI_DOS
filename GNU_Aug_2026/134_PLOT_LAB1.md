# Plotting functions with GnuPlot in 2D

## Plotting Functions

```bash

 G N U P L O T
        Version 6.0 patchlevel 4    last modified 2025-12-18 

        Copyright (C) 1986-1993, 1998, 2004, 2007-2025
        Thomas Williams, Colin Kelley and many others

        gnuplot home:     http://www.gnuplot.info
        faq, bugs, etc:   type "help FAQ"
        immediate help:   type "help"  (plot window: hit 'h')

        Terminal type is now windows
gnuplot> set term win enh 

Terminal type is now 'windows'
Options are '0 color solid butt enhanced standalone'
gnuplot> plot sin(1/x)
gnuplot> 0
         ^
         invalid command

gnuplot> plot sin(1/x**2)
gnuplot> plot[-pi:pi] sin(x)
gnuplot> set zeroaxis
gnuplot> plot [-pi:pi] sin(1/x**2)
gnuplot> �plot [-2pi:2pi] [:] f(x) ls 2 lw 3
         ^
         invalid character �

gnuplot> plot [-2pi:2pi] [:] f(x) ls 2 lw 3  
                 ^
         ':' or keyword 'to' expected

gnuplot> plot [-2pi:2pi] f(x) ls 2 lw 3     
                 ^
         ':' or keyword 'to' expected

gnuplot> plot [-2pi:2pi] [:] sin(x) ls 2 lw 3  
                 ^
         ':' or keyword 'to' expected

gnuplot> plot [-pi:pi] [:] f(x) ls 2 lw 3   
         undefined function: f

gnuplot> plot [-pi:pi] [:] sin(x) ls 2 lw 3  
gnuplot> plot [-pi:pi] [:] sin(x) ls 2 lw 3, cos(x) ls 7 lw 3
gnuplot> plot [-pi:pi] [:] sin(x) ls 2 lw 3, cos(x) ls 7 lw 3 lc 'blue'
gnuplot> h(x) = x**2 - 2**x + 1 
gnuplot> 0 color solid butt enhanced standalone
         ^
         invalid command

gnuplot> plot h(x)

```
