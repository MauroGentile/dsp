[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
  
Actual mean: 1.024  
Biased mean: 2.404

MY CODE: (I preferred to use my own code rather than using ThinkStat library. 
My code is probabily less efficient but I think that it is a good Python practise)

```python
resp = nsfg.ReadFemResp()

hist = {}
lines=0
mean=0

for x in resp["numkdhh"]:
    hist[x] = hist.get(x, 0) + 1
    mean+=x
    lines+=1
    
tot=sum([hist[x]*x for x in hist])
biased_pmf={x:hist[x]*x/tot for x in hist} 
biased_mean=sum([biased_pmf[x]*x for x in hist])

print("Actual mean: " + str(mean/lines))
print("Biased mean: " + str(biased_mean))
```

