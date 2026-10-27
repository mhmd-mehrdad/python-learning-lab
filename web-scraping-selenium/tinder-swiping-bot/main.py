import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]
TINDOG_URL = os.environ["DATING_APP_URL"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDOG_URL)

sleep(2)
login_button = driver.find_element(By.XPATH, value="/html/body/header/button")
login_button.click()

sleep(1)
login_with_facebook_button = driver.find_element(By.XPATH, value='//*[@id="login-modal"]/div/div/div/button[1]')
login_with_facebook_button.click()

base_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)

wait = WebDriverWait(driver, 2)

facebook_email_input = wait.until(ec.presence_of_element_located((By.ID, "email")))
facebook_email_input.clear()
facebook_email_input.send_keys(ACCOUNT_EMAIL)

facebook_password_input = wait.until(ec.presence_of_element_located((By.ID, "pass")))
facebook_password_input.clear()
facebook_password_input.send_keys(ACCOUNT_PASSWORD)

facebook_login_button = driver.find_element(By.XPATH, value="/html/body/div[2]/div/form/button")
facebook_login_button.click()

sleep(1)

driver.switch_to.window(base_window)

allow_location_button = driver.find_element(By.XPATH, value="/html/body/main/div/div/form/button")
allow_location_button.click()

sleep(1)

not_interested_button = driver.find_element(By.XPATH, value="/html/body/main/div/div/form/button[2]")
not_interested_button.click()

sleep(1)

accept_cookies_button = driver.find_element(By.XPATH, value="/html/body/main/div/div/form/button")
accept_cookies_button.click()

sleep(2)

like_button = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.CLASS_NAME, "btn-like"))
)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", like_button)

sleep(1)
like_button.click()



