[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)




SOLUTIONS:

mean: 74278.71    
median: 51226.45   
skewness: 4.95   
pearson_median_skewness: 0.74    
Fraction with income below the mean: 0.6600   



MY CODE:
```python
mean=RawMoment(sample,1)
median=Median(sample)
skewness=Skewness(sample)
pearson_median_skewness=PearsonMedianSkewness(sample)
print("mean: "+str("{0:.2f}".format(mean)))
print("median: "+str("{0:.2f}".format(median)))
print("skewness: "+str("{0:.2f}".format(skewness)))
print("pearson_median_skewness: "+str("{0:.2f}".format(pearson_median_skewness)))


print("Fraction with income below the mean: "+str("{0:.4f}".format(len(sample[sample<mean])/len(sample))))

```
