---
title: "Command Line Interface and DOS Experience"
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
  - \setkeys{Gin}{width=0.8\textwidth}
---
<!-- The YAML block sits above this -->

\vspace{2.5em}

\noindent\fbox{%
  \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule}{%
    \textbf{Author:} Koushani Roy \\
    \textbf{Roll No:} 134 \\
    \textbf{Semester:} 1 \\
    \textbf{Paper Code:} C1PH230112P \\
    \textbf{Subject:} Clab - 1, UG (Physics) \\
    \textbf{Institution:} St. Xavier's College (Autonomous), Kolkata \\
    \textbf{Date:} August 3, 2026
  }%
}

\pagebreak

## 1. Introduction

Documentation for first major labwork on CLI in Windows

## 2. Commands and Outputs

### [Task 1: Directory creation and verification]{.underline}

```bash
cd PHY134SEM12026 
mkdir CLI_DOS_July2026 
cd CLI_DOS_July2026 dir /p

```

![](images/Task1.jpeg)

### [Task 2:  File creation]{.underline}

```Bash
echo CLI DOS Experiment Notes > notes.txt 
type notes.txt 
more notes.txt 
```

![](images/Task2.jpeg)

### [Task 3:  File Relocation]{.underline}

```Bash
mkdir Data move notes.txt Data 
cd Data dir 
cd .. 
```

![](images/Task3.jpeg)

### [Task 4: System Diagnostics Script]{.underline}

```Bash
type system_report.txt

```

![](images/Task4.jpeg)

### [Task 5: Txt File Creation and update]{.underline}

```Bash
echo Test File > test.txt
echo Updated on %DATE% >> test.txt
cls
```

![](images/Task5.jpeg)

### [Task 6: sin(x) Plotting]{.underline}

```Bash
cd gnuplot 
"C:\Program Files\gnuplot\bin\gnuplot.exe" 
plot sin(x)

```

![](Task6.jpeg)

Graph:

![](images/Task6_gnu.jpeg)

### [Task 7: Directory listing ]{.underline}

```Bash
dir /b > bare\_list.txt 
more bare\_list.txt

```

![](Task7.jpeg)

## 3. Experience (Workspace setup, MacOS)

## 4. Conclusion

### CLI and Batch Files

Using CLI for running commands is way faster than using GUI and essentially more streamlined when the number of files and folders is large and we need to run some commands like finding certain keywords or force delete something. 

### Gnuplot

Gnuplot is lightweight and fast for plotting purposes, surpassing standard methods like using Python (Matplotlib) for basic graphic and visualisation purposes. 
