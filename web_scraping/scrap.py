import requests
from bs4 import BeautifulSoup

url="https://www.amazon.in/s?i=apparel&bbn=1968093031&rh=n%3A1968093031%2Cn%3A1571271031%2Cp_85%3A10440599031%2Cp_36%3A-49900%2Cp_89%3AAllen+Solly%7CAmazon+Brand+-+Symbol%7CArrow%7CBewakoof%7CCampus+Sutra%7CDiverse%7CJack+%26+Jones%7CLee%7CLevi%27s%7CPepe+Jeans%7CPeter+England%7CSimon+Carter%7CSpykar%7CSymbol+premium%7CThe+Indian+Garage+Co%7CThe+Souled+Store%7CU.S.+POLO+ASSN.%7CUNITED+COLORS+OF+BENETTON%7CVan+Heusen%7CVeirdo%7CWrangler%7Cblackberrys&s=popularity-rank&dc&hidden-keywords=-women-woman-girl-shoe-boy&ds=v1%3AXQ%2F9dOumlePee%2BNgoO5SN%2FkX5TkF%2FPfD7OMoKUIMl78&pf_rd_i=6648217031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=0dcd8f0c-f9fd-42ce-9458-7a492381b0b4&pf_rd_r=47Y6SEGQQ0XX8K0M4NJ7&pf_rd_s=merchandised-search-9&qid=1709098872&ref=sr_ex_n_1"

def fetch(url,path):
    r=requests.get(url)
    with open(path,'w') as f:
        f.write(r.text)

fetch(url,'data/info.html')

