import re                                                                      
from bs4 import BeautifulSoup


#To produce the output, the lines at the bottom of this file have to be uncommented





def read_data(file_name):
    soup = BeautifulSoup(open(file_name), "html.parser")
    table = soup.find('table', {'class': 'js-csv-data csv-data js-file-line-container'})
    return([[td.text for td in tr.find_all('td')][1:] for tr in table.find_all('tr', {'class': "js-file-line"})][1:])

   

#Q1
#_________________________________________________________________________________________________
degree={}
def degree_list(data):
    for line in data:
        for j in [re.sub(r'[^a-zA-Z0-9]+', '', w) for w in line[1].strip().lower().split(" ")]:
            degree[j]= degree.get(j,0)+1
    return(degree)



#Q2
#_________________________________________________________________________________________________
def titles_list(data):
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
    return(titles)   



#Q3
#_________________________________________________________________________________________________
def email_addresses_list(data):
    email_addresses=[]
    for line in data:
        match = re.search(r'[\w\.-]+@[\w\.-]+', line[3])
        email_addresses.append(match.group(0))
    return(email_addresses)  


#Q4
#_________________________________________________________________________________________________
def domains_list(data):
    domains={}
    for line in data:
        match = re.search(r'[\w\.-]+@([\w\.-]+)', line[3])
        domains[match.group(1)]= domains.get(match.group(1),0)+1
    return(domains)


"""


data=read_data("faculty.csv")
print("\n")
print("DEGREE")
print("_______________________________")
degree=degree_list(data)
print("Number of unique degrees: "+str(len(degree)))
print("Frequencies:")
print(degree)
print("\n")


print("TITLES")
print("_______________________________")
titles=titles_list(data)
print("Number of unique titles: "+str(len(titles)))
print("Frequencies:")
print(titles)
print("\n")

print("EMAIL ADDRESSES")
print("_______________________________")
emails=email_addresses_list(data)
print("Email list:")
print(emails)
print("\n")

print("DOMAINS")
print("_______________________________")
domains=domains_list(data)
print("Number of unique domains: "+str(len(domains)))
print("Frequencies:")
print(domains)
print("\n")
"""
