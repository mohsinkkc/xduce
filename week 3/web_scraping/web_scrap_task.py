import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.investing.com/holiday-calendar/"

response=requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

table=soup.find("table",{"id":"holidayCalendarData"})
data=[]
coloumns=[]
for row in table.find_all("tr"):
    cells=row.find_all(['th','td'])
    if len(cells) > 0:
        if not coloumns:
            coloumns=[cell.text.strip() for cell in cells]
        else:
            data.append([cell.text.strip() for cell in cells])

pf=pd.DataFrame(data,columns=coloumns)

excel_file='Holidya_trade.xlsx'

pf.to_excel(excel_file,index=False)

print("The Data has saved successfully in your file",excel_file)


