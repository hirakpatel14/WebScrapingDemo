from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import os

my_url="https://myimmitracker.com/en/au/trackers/expression-of-interest-sc190"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

print(page_html)

page_soup = soup (page_html, "html.parser")
print("Page After Parsing : ")

case_containers = page_soup.findAll('div', {'class':'ag-body-viewport-wrapper'})
print('Case Details:')

# for case in case_containers:
#     print(case)

sqlite:///C:\Users\Hirak\PycharmProjects\WebScrapingDemo\venv\crud.sqlite
basedir = os.path.abspath(os.path.dirname(__file__))
print('sqlite:///' + os.path.join(basedir, 'crud.sqlite'))