#pip install selenium
# pip install webdriver-manager
#(ChromeDriverManager().install())

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd

web = "https://www.investing.com/holiday-calendar/"
driver = webdriver.Chrome(service=Service((ChromeDriverManager().install())))
driver.maximize_window()

driver.get(web)

table = driver.find_element(By.ID, "holidayCalendarData")
rows = table.find_elements(By.TAG_NAME, "tr")


columns = []
data_rows = []
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
    if len(cells) > 0:
        if not columns:
            columns = [cell.text.strip() for cell in cells]
        else:
            data_rows.append([cell.text.strip() for cell in cells])

# num_colmns=len(columns)
# data_rows_filter=[row for row in data_rows if len(row) == num_colmns]

# print(data_rows_filter)
# pf = pd.DataFrame(data_rows_filter, columns=columns)

pf = pd.DataFrame(data_rows, columns=columns)


excel_file='holiday.xlsx'
pf.to_excel(excel_file,index=False)

print("Your File is extracted succesfully in ",excel_file)

time.sleep(5)


