# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


from bs4 import BeautifulSoup
soup = BeautifulSoup(open("football.csv"), "html.parser")

table = soup.find('table', {'class': 'js-csv-data csv-data js-file-line-container'})
data = [[td.text for td in tr.find_all('td')][1:] 
    for tr in table.find_all('tr', {'class': "js-file-line"})][1:]

team=data[0][0]
diff=int(data[0][-3])-int(data[0][-2])

for t in data[1:]:
    if int(t[-3])-int(t[-2])<diff:
        diff=int(t[-3])-int(t[-2])
        team=t[0]
        
print(team + " is the team with lowest difference between Goals done and Goals Allowed")
print("The goals difference is "+ str(diff))
        
