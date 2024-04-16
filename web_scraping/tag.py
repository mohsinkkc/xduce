from bs4 import BeautifulSoup

with open("data/info.html",'r') as f:
    html_doc=f.read()

soup = BeautifulSoup(html_doc,'html.parser')

# print(soup.prettify()) # The prettify is a function to fetch info from the given location 
# print(soup.title) #the get the Title of Html page

# print(soup.find_all("div")) #it will get all the div tag from page

for link in soup.find_all("a"):
    print(link.get("href"))
