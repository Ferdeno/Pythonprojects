import requests
from bs4 import BeautifulSoup

response=requests.get("https://news.ycombinator.com/")
website_details=response.text

soup=BeautifulSoup(website_details,"html.parser")
print(soup.prettify())
article=soup.find_all(name="a",rel="noreferrer")

text=[]
link=[]

for i in article:
    text.append(i.text)
    link.append(i.get("href"))
# print(article)

# for i in article:
#     print(i.text)
# print(article_link)

article_upvote=soup.find_all(name="span",class_="score")
score=[]
for i in article_upvote:
    score.append(int(i.text.split()[0]))


# print(text)
# print(link)
print(score)

print(text[score.index(max(score))],link[score.index(max(score))])
# print(article_upvote)

# with open("website.html") as f:
#     contents=f.read()x
#     # print(contents)

# soup=BeautifulSoup(contents,'html.parser')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())

# anchor_tag=soup.find_all(name="a")
# print(anchor_tag)

# for i in anchor_tag:
#     print(i)
#     print()
#     print(i.getText())
#     print()
    # print(i.get("href"))

# heading=soup.findAll(name='h1',id="name")
# print(heading)

# section=soup.find_all(class_="heading")
# print(section)

# select_one=soup.select_one(selector="p a")
# print(select_one)

# select_hash=soup.select("#name")
# print(select_hash)

# select_class=soup.select(".heading")
# print(select_class)