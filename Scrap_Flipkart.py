from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.primevideo.com/search/ref=atv_tv_hom_c_ws9x98_9_seemre?query=p_n_entity_type%3DTV%20Show%26search-alias%3Dinstant-video%26index%3Deu-amazon-video-other%26adult-product%3D0%26bq%3D%28and%20sort:%27featured-rank%27%20%28and%20studio:%27amazon%20studios%27%20%29%29%26av_offered_in_territory%3DIN%26qs-av_request_type%3D4%26qs-is-prime-customer%3D2&ie=UTF8"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup (page_html, "html.parser")
print("Page After Parsing : ")
# print(page_soup)
containers = page_soup.findAll('a', {'class':'dv-copy-button'})
print("div tags only-------------------------------------------------------------------------------------------------")

filename = 'LinksOnPage.csv'

file = open(filename, 'w')

headers = " this is the heading of the page"
for links in containers:
    print (links.get('href'))

file.write(headers)
for links in containers:
    file.writelines(links.get('href')+"\n")
file.close()