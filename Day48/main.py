from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.ca/PanOxyl-Creamy-Acne-Wash-Peroxide/dp/B09NYTQ2KM")
driver.get("https://www.python.org/")

# Find by class name
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is ${price_dollar.text}.{price_cents.text}")

# Find by name
search_bar = driver.find_element(By.NAME, value='q')
print(f"Search Bar - Tag name: {search_bar.tag_name}")
print(f"Search Bar - Placeholder: {search_bar.get_attribute('placeholder')}")

# Find by id
button = driver.find_element(By.ID, value="submit")
print(f"Button Size: {button.size}")

# Find by CSS selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(f"Documentation Link: {documentation_link.text}")

# Find by XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(f"Bug Link: {bug_link.text}\n")

# Challenge 1 - My solution
event_data = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
event_data = event_data[0].text.split('\n')
events = {}
start = 0

for num in range(5):
    events[num] = {
        "time": event_data[start],
        "name": event_data[start + 1]
    }
    start += 2
print(f"Event Dictionary: {events}")

# Challenge 1 - Angela's solution
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }
print(f"Event Dictionary: {events}")


# driver.close()  # closes a particular tab
driver.quit()  # quits the entire browser
