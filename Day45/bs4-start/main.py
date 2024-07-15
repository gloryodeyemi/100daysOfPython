from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string, "\n")

print(soup.a)  # first anchor tag
print(soup.li)  # first list tag
print(soup.p, "\n")  # first paragraph tag

# find all by tag name
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

# find by attributes
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

h3_heading = soup.find_all(name="h3", class_="heading")
print(h3_heading, "\n")

# soup selector
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")  # select using id
print(name)

class_selector = soup.select(selector=".heading")  # select using class
print(class_selector)
