---
title: 'Python Basics'
mainfont: "Times New Roman"
monofont: "Courier New"
fontsize: 12pt
linestretch: 1.15
geometry: margin=1in
toc: true
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhf{} 
  - \fancyhead[L]{Koushani Roy} 
  - \fancyhead[R]{\thepage}
  - \renewcommand{\headrulewidth}{0.5pt} 
  - \fancypagestyle{plain}{\fancyhf{}}
  - \setkeys{Gin}{width=0.6\textwidth}
  - \usepackage{fvextra}
  - \usepackage{framed}
  - \fvset{breaklines=true}
  - \definecolor{shadecolor}{RGB}{248,248,248}
  - \renewenvironment{Shaded}{\begin{snugshade}}{\end{snugshade}}
  - \usepackage{float}
  - \makeatletter
  - \def\fps@figure{H}
  - \makeatother
---
\vspace{2.5em}

\noindent\fbox{%
  \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule}{%
    \textbf{Author:} Koushani Roy \\
    \textbf{Roll No:} 134 \\
    \textbf{Semester:} 1 \\
    \textbf{Paper Code:} C1PH230112P \\
    \textbf{Subject:} Clab - 1, UG (Physics) \\
    \textbf{Institution:} St. Xavier's College (Autonomous), Kolkata \\
    \textbf{Date:} October 26, 2026
  }%
}

\pagebreak

## Exercise 1

```bash
roykoush@Koushanis-MacBook-Air Exercises % python3
Python 3.14.8 (main, Sep 30 2026, 17:55:09) [Clang 21.0.0 (clang-2100.3.34.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1+2j
>>> b = 3+4j
>>> print(a,b)
(1+2j) (3+4j)
>>> r = a/b
>>> p = a*b.conjugate()
>>> print(r,p)
(0.44+0.08j) (11+2j)

```

## Exercise 2

```python
n = int(input('n: '))

#Left justified
for i in range(n+1):
    print(('*'*i).ljust(n))

#Right justified
for i in range(n+1):
    print(('*'*i).rjust(n))

#Centre justified
for i in range(n+1):
    print(('*'*(2*i-1)).center(2*n-1))
```

## Exercise 3

```python
n = 26
for i in range(27, 52):
    print(i%26, end=',')

```

## Exercise 4

```python
>>> import phyconsts
>>> help(phyconsts)

>>> print(dir(phyconsts))
['G', 'M_earth', 'M_sun', 'NA', 'R', 'R_earth', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c', 'e', 'epsilon0', 'g', 'giga', 'h', 'hbar', 'kB', 'kilo', 'me', 'mega', 'micro', 'milli', 'mp', 'mu0', 'sigma']
>>>
```

## Exercise 5

```python
from turtle import *
mode('logo')
rt(30)
for i in range(3):    
    fd(50); rt(120)done()
```

## Exercise 6

```python
import random
from turtle import *
L = [0, 90, 180, 270]
L2 = ['red', 'blue', 'green', 'purple']
reset()
mode('logo')
for i in range(20):    
    color(random.choice(L2))    
    rt(random.choice(L))    
    fd(30)
    done()
```
## Exercise 7

```python
import turtle
turtle.mode('logo')

def draw_polygon(s, l):
    angle = 360 / s
    for i in range(s):
        turtle.fd(l)
        turtle.rt(angle)

draw_polygon(3, 100)

# Move over to avoid drawing on top of each other
turtle.up()
turtle.rt(90)
turtle.fd(150)
turtle.lt(90)
turtle.down()

# Shape 2: Pentagon
draw_polygon(5, 80)

# 4. Hold the canvas screen open
turtle.done()

```

## Exercise 8

```python
n = int(input('Enter a number to get its multiplication table:'))
for i in range(1,101):    
    print(n, 'x', i, '=', n*i)
```

## Exercise 10

```python
from turtle import *
reset()
speed(0)
color('gold')
pensize(10)
for i in range(10):    
    forward(250)    
    right(144)done()
```

#Exercise2#11
st = "gcatgactattccttgac"ac = st.count('a')cc = st.count('c')gc_ = st.count('g')tc = st.count('t')print('The counts of a,c,g and t are respectively: ', ac, ',', cc, ',', gc_, ',', tc)
#12
st = "gcatgactattccttgac"print(st[::-1])