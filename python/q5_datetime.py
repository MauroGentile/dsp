# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015' 

(datetime.strptime(date_stop, "%m-%d-%Y")-datetime.strptime(date_start, "%m-%d-%Y")).days
#result: 937 days

####b)  
date_start = '12312013'  
date_stop = '05282015'  
abs((datetime.fromtimestamp(int(date_stop))-datetime.fromtimestamp(int(date_start))).days)

#result: 82 days. 
##Technically it would make -82 but I consider negative days as meaningless.
#On the other hand, date_start-date_stop is not an option since 
#it would not be the same as date_stop-date_start not even taking the absolute values. 
#I therefore took the absolute value of date_stop-date_end after conversion



####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
(datetime.strptime(date_stop, "%d-%b-%Y")-datetime.strptime(date_start, "%d-%b-%Y")).days

#result: 7850 days. 
