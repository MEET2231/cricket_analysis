"""
author@Meet_Modi
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.espncricinfo.com/records/tournament/averages-bowling/icc-cricket-world-cup-2019-12357")
print(r.status_code)
soup = BeautifulSoup(r.text,"lxml")




table1 = soup.find("table")

headers = table1.thead.find_all("td")
c_names =[]
for i in headers:
    c_names.append(i.text)

# print(len(c_names))

all_rows = table1.tbody.find_all("tr", class_ = "ds-table-row-compact-bottom !ds-border-b-0")+table1.tbody.find_all("tr", class_ = "ds-table-row-compact-bottom ds-bg-ui-fill-translucent !ds-border-b-0")

name = []
span = []
mat= []
inns = []
balls = []
mdns = []
runs = []
wkts = []
bbi = []
avg = []
ecn = []
sr = []
five = []
ten = []
ct = []
st = []

for j in all_rows:
    rows = j.find_all("td")

    # print(rows)

    for i in range(len(rows)):
        if i== 0:
            name.append(rows[i].text)
        elif i== 1:
            span.append(rows[i].text)
        elif i== 2:
            mat.append(rows[i].text)
        elif i== 3:
            inns.append(rows[i].text)
        elif i== 4:
            balls.append(rows[i].text)
        elif i== 5:
            mdns.append(rows[i].text)
        elif i== 6:
            runs.append(rows[i].text)    
        elif i== 7:
            wkts.append(rows[i].text)
        elif i== 8:
            bbi.append(rows[i].text)
        elif i== 9:
            avg.append(rows[i].text)
        elif i== 10:
            ecn.append(rows[i].text)
        elif i== 11:
            sr.append(rows[i].text)
        elif i== 12:
            five.append(rows[i].text)
        elif i== 13:
            ten.append(rows[i].text)
        elif i== 14:
            ct.append(rows[i].text)
        elif i== 15:
            st.append(rows[i].text)

    # print(name,avg)  
            
    







player_country = table1.tbody.find_all("tr", class_ = "ds-table-row-compact-top ds-text-tight-xs")+table1.tbody.find_all("tr", class_ = "ds-table-row-compact-top ds-text-tight-xs ds-bg-ui-fill-translucent")
 

country =[]
for i in player_country:
    country.append(i.text)

# print(player_info)



df = pd.DataFrame({"player":name,"span":span,"Mat":mat,"Inns":inns,"Balls":balls,"Mdns":mdns,"Runs":runs,"Wickets":wkts,"Avg":avg,"SR":sr,"ecnomy":ecn,"BBI":bbi,"5":five,"10":ten,"ST":st,"CT":ct,"Country":country})

# print(df)
df.to_csv("bowling_data_2019.csv")
