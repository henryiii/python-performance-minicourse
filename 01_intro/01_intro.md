---
title: |
  Introduction to high performance Python
author: Henry Schreiner
date: November 20, 2019
fontsize: 10pt
aspectratio: 169
---


# Why Python?

Python is now the second most popular language on GitHub, after only JavaScript.

\begin{center}
\includegraphics[width=.6\textwidth]{images/GitHubLang.png}
\end{center}

* Still growing at a rate of 151%!
* Jupyter notebooks growth over 100% every year for the last three years!

[State of the Octoverse, 2019](https://octoverse.github.com)


# Why Python?

\begin{center}
\includegraphics[width=.9\textwidth]{images/PYPLLang.png}
\end{center}

[PyPL rankings](http://pypl.github.io/PYPL.html) of some of the most popular languages for data science.

# Timeline of Python

* 1994: Python 1.0 released
* 1995: First array package: Numeric
* 2003: Matplotlib
* 2005: Numeric and numarray merged into Numpy
* 2008: Pandas introduced
* 2012: The Anaconda python distribution was born
* 2014: IPython produces the Jupyter project and notebook
* 2016: LIGO's discovery was shown in a Jupyter Notebook, and was written in Python
* 2017: Google releases TensorFlow
* 2019: All Machine Learning libraries are primarily or exclusively used through Python


# Timeline of Python, key points


## 2005: Numpy
* Merged two competing codebases, created single ecosystem

## 2008: Pandas
* Took on specialised statistics languages (like R) with a *library* in a general purpose language
* Pioneered "Pythonic" shortcuts, breaking down traditional design barriers

## 2014: Jupyter
* The notebook format, with code, outputs, and descriptions interleaved, became multilingual


# Python vs. a compiled language

Python is an interpreted language. When we talk about Python, we usually mean CPython, which is not even Just In Time (JIT) compiled; it's purely interpreted.

TLDR: Python is *slow*.

Hundreds to thousands of times slower than C/C++/Fortran/Go/Swift/Rust/Haskell... You get the point.

Python is like a car. Compiled languages are like a plane.

So why use it?

# A hybrid approach

If you want to get to South America, the fastest way to do so is take a car to get to the airport to catch a plane. 

Same idea for Python and compiled languages. You can do the big, common, easy tasks in compiled languages, and steer it with Python.

