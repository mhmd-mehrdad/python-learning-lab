import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

movies = soup.find_all(name="h3", class_="title")
print(movies)

movies_list = []

for movie in movies:
    text = movie.get_text()
    movies_list.append(text)


movies_list.reverse()

print(movies_list)

with open("notes.txt", "w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(movie + "\n")
