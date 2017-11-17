[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
import numpy as np

a_thousand_num=np.random.random(1000)
pmf = thinkstats2.Pmf(a_thousand_num)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Config(xlabel='Random variate', ylabel='PMF')

```
from the PMF is hard to say if this is a uniform sitribution.
I would say yes: there are many vertical lines (1000 lines I would dare to say) well distribuited between 0 and 1.
Of course each line has a height equal to 0.001: each value is a real number and it is highly unlikely that it can be exctracted twice...


```python
cdf = thinkstats2.Cdf(pmf)
thinkplot.Cdf(cdf, linewidth=1)
```

My understanding is that cdf confirms this is a uniform distribution since cdf is a straight line from 0 to 1, with a slope of 45 degrees. This only happens for uniforms distributions

