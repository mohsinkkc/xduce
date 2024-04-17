import requests
from bs4 import BeautifulSoup
import pandas as pd


url=""

response=requests.get(url)

soup=BeautifulSoup(response.content,'html.parser')


