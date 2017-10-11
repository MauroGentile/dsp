# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

---

### Q1. Python Version 2 or 3

**Course material for the bootcamp is compatible with Python versions 2.7 and 3.0. All HackerRank Python pre-work is configured for Python 3 only.  Therefore, Python 3 is the recommended version.**  

Did you install Python 2 or 3? Why?  

I have installed Python 3.6.1 on my Mac
Despite an initial scepticism due to compatibility concerns I have read on the internet, I have finally decided to go for the version 3 for 2 reasons:
1)	v2 will be soon obsolete. Better to have an eye to the future rather than to the past
2)	I have been using Python 2.7 and I got frustrated working with encodings…. As far as I know v3 makes encodings much simpler



### Q2. Which Python Version Installed   

How can you check the version of Python installed if you happen to be on an unfamiliar computer?


To check for installations I would run this command:  
*which -a python python3*  

Dpeending on the previous command output, I would run either or both commands below:  
*>python3 --version*  
*>python --version*  


 


