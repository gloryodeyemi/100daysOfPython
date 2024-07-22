from bs4 import BeautifulSoup
import requests

desired_year = input("What year would you like to travel to? (Enter the date using this format YYYY-MM-DD): ")

# scrape the top 100 song titles from Billboard Hot 100
response = requests.get(F"https://www.billboard.com/charts/hot-100/{desired_year}/")
# response = requests.get(F"https://www.billboard.com/charts/hot-100/1999-07-10/")

bill_page = response.text

soup = BeautifulSoup(bill_page, "html.parser")

top_100 = soup.select("li h3#title-of-a-story")
top_100_titles = [title.getText().replace('\n', '').replace('\t', '') for title in top_100]
print(top_100_titles)

# Takes top 100 music from a date in the past to create a Spotify playlist.
