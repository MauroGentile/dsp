[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

81.7%



import scipy.stats
mean = 178.0
stand_dev = 7.7
heights = scipy.stats.norm(loc=mean, scale=stand_dev)

h_min=155
h_max=185
heights.cdf(h_max)-dist.cdf(h_min)
