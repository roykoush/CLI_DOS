# CLI Documents for Lab Reports

First things first, there is always a long debate on things being 'open' when its actually something of a marked assignment but then given the odds of people actually visiting my github page and looking up things is basically pretty slim.

So, here it is.

Uniform format for all lab reports:

```Latex
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
    \textbf{Date:} August 10, 2026
  }%
}

\pagebreak
```

Apart from `xelatex` engine, if you use a lightweight distribution layer like `BasicTex`, you have to manually fetch `soul`, `luacolor`, `luacolor` (unnecessary except for document underlines using LaTex). The TeX Live Manager `tlmgr` should be used.
