from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_story_links = soup.select("span.titleline a")
# all_story_links = soup.select(selector=".titleline")
print(all_story_links)

article_titles = [tag.getText() for tag in all_story_links]
print(article_titles)

article_links = [tag.get("href") for tag in all_story_links]
print(article_links)

article_votes = [int(vote.getText()[:-7]) for vote in soup.find_all(name="span", class_="score")]
print(article_votes)

