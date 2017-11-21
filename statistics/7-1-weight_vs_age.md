[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)




Scatterplot between mothers' age and child'weight makes one suspect that these variable are not correlated eachother since the cloud of dots is roughly a cahotic circle.

The near 0 Correlation and Spearman correlation coefficients (0.069, 0.097 resectively) gives a formal matematical evidence to the graphical intuition.   

MY CODE
```python

bins = np.arange(min(live.agepreg), max(live.agepreg), 5)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)

ages = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]


for percent in [25, 50, 75]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

thinkplot.Config(xlabel="Mothers'age",
                     ylabel="Children's weight (lb)",
                     legend=True, loc="best")
    

```
