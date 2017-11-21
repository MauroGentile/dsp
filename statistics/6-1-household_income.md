[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> REPLACE THIS TEXT WITH YOUR RESPONSE


mean=RawMoment(sample,1)
median=Median(sample)
skewness=Skewness(sample)
pearson_median_skewness=PearsonMedianSkewness(sample)
print("mean: "+str("{0:.2f}".format(mean)))
print("median: "+str("{0:.2f}".format(median)))
print("skewness: "+str("{0:.2f}".format(skewness)))
print("pearson_median_skewness: "+str("{0:.2f}".format(pearson_median_skewness)))
