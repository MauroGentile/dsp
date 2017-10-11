# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

They both are an order collection of items but while lists are mutable (i.e. can be modified), tuples are immutable.
This difference enables tuples to be keys for a dictionary.
In facts, dictionary keys must be immutable. 
this is why tuple can work as key in dictionaries while lists cannot.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

They are both mutable collection of items but with three major differences:
- lists are ordered collections. Sets are unordered menaing that lists support indexing while sets do not
- lists can include duplicates, set only contains unique values
- lists can be multidimensional, sets cannot


The unordered nature of sets makes them much faster in finding elements compared to lists which are ordered.
Sets support operations of math's set theory and are very useful when it is time to extract unique elements from a list


Example:
```python
#Dictionary of my best friend names:
friends=[{"name":"Ann", "surname":"Smith"},
        {"name":"Bob", "surname":"Randall"},
        {"name":"Ann", "surname":"Vitolo"},
        {"name":"Mary", "surname":"Jene"},
        {"name":"Bob", "surname":"Geldof"},
        {"name":"Niel", "surname":"O'Nieal"}]
        
#Complete  names:
[n["name"]+","+n["surname"] for n in friends]

#Unique names
set([n["name"] for n in friends])
```



---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

lambda function are anonymous one-line functions which make code much more readible.  
Example:
Back to the example above, imagine I want to order my best friends by surname:

```python
sorted(Complete_names, key=lambda x: x.split(",")[1])

```
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehnsions are a powerful and fast way to build lists/sets/dictionaries in itarative way. 


LC Example with its Map equivalent:
```python
#given a list of numbers, return a list of its elements squared
import random
A= random.sample(range(1, 100), 10)
squared=[n**2 for n in A]
squared_map=list(map(lambda x: x**2, A))
```

LC Example with its Filter equivalent:
```python
#given a list of numbers, filter the even ones
import random
A= random.sample(range(1, 100), 10)
even=[n for n in A if n%2==0]
even_filter=list(filter(lambda x: x%2==0, A))
```


Example of Dictionary comprhension:
```python
# with reference to code in Q2,the following line builds a dictionary with
#  names of my best friends as key and occurence as value
{n:[p["name"] for p in friends].count(n) for n in set([r["name"] for r in friends])}
```

```python
# with reference to code in Q2,the following line builds a set with
# my best friends'name whose lenght is less than 4,each taken only 1 time 
{n for n in [n["name"] for n in friends] if len(n)<4}
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





