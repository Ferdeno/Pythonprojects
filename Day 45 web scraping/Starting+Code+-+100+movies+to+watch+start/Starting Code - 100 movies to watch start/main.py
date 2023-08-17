import requests
from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = "http://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(URL)
response.encoding="utf-8"
data=response.text

soup=BeautifulSoup(data,"html.parser")

title=[]
heading=soup.find_all(name="h3")
for i in heading:
    title.append(i.text)

title=title[::-1]
print(title)

with open("movies","w") as file:
    for i in title:
        file.write(f"{i}\n")
        

# Write your code below this line 👇


