from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Challenge 2 - My solution
total_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
print(total_articles.text)
# total_articles.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Sending keyboard input to Selenium
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)


# driver.quit()
