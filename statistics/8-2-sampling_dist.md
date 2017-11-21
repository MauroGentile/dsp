[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

The 90% confidence interval is: [1.26,3.72]
The standard error is: 0.88 

Increasing the sample size from (simulated up to 1000), both confidence interval length and standard error go asympthotically to 0


MYCODE    
```pythonn=9
n_max=1000
repetitions=1000
lam=2
    
results=simulate_exponetial(n, repetitions, lam)
cdf = thinkstats2.Cdf(results)
ci = cdf.Percentile(5), cdf.Percentile(95)
    
stderr = RMSE(results, lam)    
print ("The 90% confidence interval is: ["+ "{0:.2f}".format(ci[0])+","+"{0:.2f}".format(ci[1])+"]")    
print ("The standard error is: "+"{0:.2f}".format(stderr))


stderr=[]
ci_len=[]

for i in range(n,n_max):
    results=simulate_exponetial(i, repetitions, lam)
    stderr.append(RMSE(results, lam) )   
    cdf = thinkstats2.Cdf(results)
    ci_len.append(cdf.Percentile(95)-cdf.Percentile(5))
    


plt.plot(range(n,n_max), stderr,label="StdErr")
plt.plot(range(n,n_max), ci_len, label="CI length")
plt.legend()
    

```


