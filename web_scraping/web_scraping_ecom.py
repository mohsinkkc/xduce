from bs4 import BeautifulSoup
import requests

url="https://www.amazon.in/dp/B0CCYGC3TS/ref=AF_WIN_bub_w_cml_t_2?pf_rd_r=H3A4JY3KY39N70TW2D1X&pf_rd_p=d8ebe7af-d819-40af-8c03-e8aa95b7d149&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-8&pf_rd_t=&pf_rd_i=7198569031"


proxies = { 
              "http"  :  "http://10.10.1.10:3128", 
              "https" : "https://10.10.1.11:1080"
            }

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url,headers=headers)



soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())