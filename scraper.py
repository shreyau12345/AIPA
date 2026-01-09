# import requests
# from bs4 import BeautifulSoup
# college="https://iert.ac.in/"
# respons=requests.get(college)
# if respons.status_code==200:
#     print("sucessfully fetched web page")
# else: 
#     print(" error fetching page")
# html_content=respons.text
# if html_content:
#     soup=BeautifulSoup(html_content,"html.parser")
#     title=soup.title.string
#     print(title)

# import requests
# from bs4 import BeautifulSoup
# college="https://iert.ac.in/"
# respons=requests.get(college)
# if respons.status_code==200:
#     print("sucessfully fetched web page")
# else: 
#     print(" error fetching page")
# html_content=respons.text
# if html_content:
#     soup=BeautifulSoup(html_content,"html.parser")
#     title=soup.title.string
#     print(title)


# for i in range(1,7):
#     for heading in  soup.find_all(f"h{i}"):
#         print(f"heading{i}{heading.get_text(strip=True)}")


# extract all content in webpage
# for paragraph in soup.find_all("p"):
#     print(paragraph.get_text(strip=True))

#extract all links in webpage
# for a in soup.find_all("a"):
#     text=a.get_text(strip=True)
#     href=a["href"]
#     print(text , href)

#extract all images in webpage
# for img in soup.find_all("img"):
#     src=img["src"]
#     print(src)

import requests
from bs4 import BeautifulSoup
url="http://quotes.toscrape.com/"
respons= requests.get(url)
soup= BeautifulSoup(respons.text, "html.parser")
qoutes=soup.find_all("span", class_="text")
authors=soup.find_all("small", class_="author")

print("Qoutes from the page:")
for q, a in zip(qoutes,authors):
    print(f"{q.get_text()} - {a.get_text()}")
