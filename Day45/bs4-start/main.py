from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# all_story_links = soup.select("span.titleline")
all_story_links = soup.find_all(name="span", class_="titleline")
print(all_story_links)
# print("\nTesting")

# for ind in range(len(all_story_links)):
#     print(all_story_links[ind].find("a"))

article_titles = [tag.find("a").getText() for tag in all_story_links]
print(article_titles)

article_links = [tag.find("a").get("href") for tag in all_story_links]
print(article_links)

article_votes = [int(vote.getText()[:-7]) for vote in soup.find_all(name="span", class_="score")]
print(article_votes)

