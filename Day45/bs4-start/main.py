from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_story_links = soup.find_all(name="span", class_="titleline")
print(all_story_links)

article_titles = [tag.find("a").getText() for tag in all_story_links]
print(article_titles)

article_links = [tag.find("a").get("href") for tag in all_story_links]
print(article_links)

article_votes = [int(vote.getText()[:-7]) for vote in soup.find_all(name="span", class_="score")]
print(article_votes)

max_vote_index = article_votes.index(max(article_votes))

print("\n****************************\nArticle with the most upvote\n****************************")
print(article_titles[max_vote_index])
print(article_links[max_vote_index])
print(article_votes[max_vote_index])

