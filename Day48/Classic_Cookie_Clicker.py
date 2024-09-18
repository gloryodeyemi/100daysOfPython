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
    store = driver.find_element(By.ID, value="store")
    store = store.text.split("\n")
    store_costs = [convert_str_to_int(item.split('-')[1].strip()) for item in store if '-' in item]
    store_costs.reverse()
    return store_costs


def format_time(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


store_ids = ['buyTime machine', 'buyPortal', 'buyAlchemy lab', 'buyShipment', 'buyMine', 'buyFactory', 'buyGrandma',
             'buyCursor']
click_interval = 0.01
purchase_check_interval = 10

# Continuous clicking loop
try:
    last_check_time = time.time()
    print(f"Start time: {format_time(last_check_time)}")

    while True:
        cookie.click()
        time.sleep(click_interval)

        if time.time() - last_check_time >= purchase_check_interval:
            # Check how many cookies clicked
            cookies = convert_str_to_int(driver.find_element(By.ID, value="money").text)
            print(f"Cookies available: {cookies}")
            item_costs = get_store_cost()  # Get the current costs of the store items

            # Find the affordable store items to purchase
            for ind in range(len(store_ids)):
                if cookies >= item_costs[ind]:
                    item_to_buy = driver.find_element(By.ID, value=f"{store_ids[ind]}")
                    item_to_buy.click()
                    print(f"Purchased item: {store_ids[ind]}")
                    break

            # Update the check time
            last_check_time = time.time()
            print(f"Last check time: {format_time(last_check_time)}\n")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()


