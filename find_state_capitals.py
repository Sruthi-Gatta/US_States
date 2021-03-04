from bs4 import BeautifulSoup
from collections import OrderedDict
import urllib.request
import csv

# current folder location. Please kindly change as needed.
f = open("usa.states.txt", "r")
c = csv.reader(f)
states = []
for line in c:
    states.append(line[0])
print(states)

BASE_URL = "https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210"
html = urllib.request.urlopen(BASE_URL).read()
soup = BeautifulSoup(html, "html.parser")
country_table = soup.find('div', {"class": "md-drag md-table-wrapper"})
tbody = country_table.find('table')

tbody = str(tbody)
table_data = [[cell.text for cell in row("td")]
              for row in BeautifulSoup(tbody)("tr")]
output_list = []
for item in table_data:
    if item:
        if item[0] in states:
            dict_item = {}
            dict_item['state'] = item[0]
            dict_item['captial'] = item[1]
            output_list.append(dict_item)
            print("{0},{1}".format(item[0], item[1]))
print(output_list)
keys = output_list[0].keys()
with open('capital.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(output_list)