from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://ozh.github.io/cookieclicker/")

language = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)
language.click()

try:
    consent = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cc_btn_accept_all"))
    )
    consent.click()
except TimeoutException:
    pass

cookie_button = driver.find_element(By.ID, value="bigCookie")
cookie_button.click()

last_check = time.time()
print(last_check)

while True:
    cookie_button.click()

    if time.time() - last_check >= 5:

        total_money = driver.find_element(By.ID, "cookies")
        number = int(total_money.text.split()[0].replace(",", ""))
        print(number)

        affordable_items = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
        best_item = None
        for item in affordable_items:
            print(item.text)
            item_price = item.find_element(By.CLASS_NAME, value="price")
            if number >= int(item_price.text):
                best_item = item
        best_item.click()

        last_check = time.time()




# items = driver.find_elements()
# cookie = driver.find_element(By.ID, value="bigCookie")
