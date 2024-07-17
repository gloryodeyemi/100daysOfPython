from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")

all_movie_titles = soup.find_all(name="h3", class_="title")
print(all_movie_titles)

movies_list = [title.getText() for title in all_movie_titles]
movies_list.reverse()
print(movies_list)

with open("top_100_movies.txt", "w") as movies:
    for movie in movies_list:
        movies.write(f"{movie}\n")
