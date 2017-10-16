import re                                                                      
 
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("faculty.csv"), "html.parser")

table = soup.find('table', {'class': 'js-csv-data csv-data js-file-line-container'})


data = [[td.text for td in tr.find_all('td')][1:] 
    for tr in table.find_all('tr', {'class': "js-file-line"})][1:]


#Q1
#_________________________________________________________________________________________________
degree={}
for line in data:
    for j in [re.sub(r'[^a-zA-Z0-9]+', '', w) for w in line[1].strip().lower().split(" ")]:
        degree[j]= degree.get(j,0)+1
        
print(degree)     


#Q2
#_________________________________________________________________________________________________
titles={"assistant professor":0,
        "associate professor":0,
        "professor":0}


lis=['assistant professor','associate professor','professor']
for line in data:
    for l in lis:
        p = re.compile(l)
        m = p.match(line[2].strip().lower())
        if m:    
            titles[l]= titles.get(l,0)+1
print(titles)


#Q3
#_________________________________________________________________________________________________
email_addresses=[]
for line in data:
    match = re.search(r'[\w\.-]+@[\w\.-]+', line[3])
    email_addresses.append(match.group(0))
print(email_addresses)


#Q3
#_________________________________________________________________________________________________

domains={}
for line in data:
    match = re.search(r'[\w\.-]+@([\w\.-]+)', line[3])
    domains[match.group(1)]= domains.get(match.group(1),0)+1

domains
