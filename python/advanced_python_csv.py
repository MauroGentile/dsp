from bs4 import BeautifulSoup
import csv
import re

from advanced_python_regex import read_data, email_addresses_list




data=read_data("faculty.csv")
emails=email_addresses_list(data)


with open("emails.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in emails:
        writer.writerow([line])
