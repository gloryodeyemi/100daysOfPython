import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")


def convert_str_to_int(element):
    if ',' in element:
        return int(element.replace(',', ''))
    return int(element)


def get_store_cost():
    store = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
    store_costs = [convert_str_to_int(item.text.split('-')[1].strip()) if '-' in item.text else 0 for item in store]
    store_costs.reverse()
    return store_costs


def format_time(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


def get_store_item_ids():
    store_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
    item_ids = [item.get_attribute("id") for item in store_items]
    item_ids.reverse()
    return item_ids


# click_interval = 0.01
purchase_check_interval = 10
game_duration = 300  # 5 minutes = 300 seconds
store_item_ids = get_store_item_ids()  # Get the ids of the store items

# Continuous clicking loop
try:
    start_time = time.time()
    last_check_time = start_time
    print(f"Start time: {format_time(start_time)}\n")

    while True:
        cookie.click()
        # time.sleep(click_interval)

        if time.time() - last_check_time >= purchase_check_interval:
            # Check how many cookies clicked
            cookies = convert_str_to_int(driver.find_element(By.ID, value="money").text)
            print(f"Cookies available: {cookies}")
            item_costs = get_store_cost()  # Get the current costs of the store items
            print(f"Cost of items: {item_costs}")

            # Find the affordable store items to purchase
            for ind in range(len(store_item_ids)):
                if cookies >= item_costs[ind] != 0:
                    item_to_buy = driver.find_element(By.ID, value=f"{store_item_ids[ind]}")
                    item_to_buy.click()
                    print(f"Purchased item: {store_item_ids[ind]}")
                    break

            # Update the check time
            last_check_time = time.time()
            print(f"Last check time: {format_time(last_check_time)}\n")

        # Check if 5 minutes have passed
        if time.time() - start_time > game_duration:
            print(f"Game duration of {game_duration / 60} minutes reached. Exiting Game...")
            cookies_per_second = driver.find_element(By.ID, value="cps").text.split(":")[1].strip()
            print(f"You generated {cookies_per_second} cookies per seconds. Well done!")
            break

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()


