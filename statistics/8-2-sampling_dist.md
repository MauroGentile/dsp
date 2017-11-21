[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

The 90% confidence interval is: [1.28,3.72]    
The standard error is: 1.91    


MYCODE    

sample_size=9 
repetitions=1000 
lam=2

resuts=[]
for _ in range(repetitions):
    xs = np.random.exponential(1.0/lam, sample_size)
    Lbar = 1 / np.mean(xs)
    results.append(Lbar)
        
    
results=simulate_exponetial(9, 1000, 2)
cdf = thinkstats2.Cdf(results)
ci = cdf.Percentile(5), cdf.Percentile(95)
    
stderr = RMSE(results, 1/2)    
print ("The 90% confidence interval is: ["+ "{0:.2f}".format(ci[0])+","+"{0:.2f}".format(ci[1])+"]")    
print ("The standard error is: "+"{0:.2f}".format(stderr))

