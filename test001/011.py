from bs4 import BeautifulSoup
import requests
url='https://www.baidu.com/'
response =requests.get(url)
response.encoding="utf-8"
soup =BeautifulSoup(response.text,"lxml")
# title_tag=soup.find("title")
# print(title_tag)
# first_link=soup.find("a")
# print(first_link)
# first_link_url=first_link.get("href")
# print(first_link_url)
# all_links=soup.find_all("a")
# print(all_links)
# paragraph_text=soup.find('p').get_text()
all_text=soup.get_text()
print(all_text)
