import os
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from time import sleep

SIMILAR_ACCOUNT = os.environ["SIMILAR_ACCOUNT"]
USERNAME = os.environ["FOLLOWER_USERNAME"]
PASSWORD = os.environ["FOLLOWER_PASSWORD"]
BASE_URL = os.environ["FOLLOWER_BASE_URL"]
LOGIN_URL = f"{BASE_URL}/login"

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True) # keep the browser open
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(LOGIN_URL)

        self.wait = WebDriverWait(self.driver, 2)

        username_input = self.wait.until(ec.element_to_be_clickable((By.ID, "username")))
        username_input.clear()
        username_input.send_keys(USERNAME)

        password_input = self.wait.until(ec.element_to_be_clickable((By.ID, "password")))
        password_input.clear()
        password_input.send_keys(PASSWORD)

        login_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/form/button')))
        login_button.click()

        save_login_info_popup_dismiss = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="popup-save-login"]/div/div[2]')))
        save_login_info_popup_dismiss.click()

        notification_popup_dismiss = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="popup-notifications"]/div/button[2]')))
        notification_popup_dismiss.click()

    def find_followers(self):

        search_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/button/span')))
        search_button.click()

        search_input = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/aside/div[2]/input')))
        search_input.clear()
        search_input.send_keys(SIMILAR_ACCOUNT)

        sleep(2)

        search_input.send_keys(Keys.ENTER)

        followers_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a/b')))
        followers_button.click()

    def follow(self):

        # base_window = self.driver.window_handles[0]
        # sleep(2)
        # followers_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(followers_window)
        # popup = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]')
        #
        # sleep(5)
        #
        # self.driver.execute_script(
        #     "arguments[0].scrollTop = arguments[0].scrollHeight;",
        #     popup
        # )
        #
        # sleep(2)
        #
        # self.driver.execute_script(
        #     "arguments[0].scrollTop = arguments[0].scrollHeight;",
        #     popup
        # )

        popup = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll")

        processed = set()

        while True:
            buttons = self.driver.find_elements(
                By.CSS_SELECTOR,
                ".followers-scroll .naan-follow-btn"
            )

            for button in buttons:
                user = button.get_attribute("data-handle")

                if user in processed:
                    continue

                try:
                    button.click()
                    sleep(1)

                except ElementClickInterceptedException:
                    cancel = self.driver.find_element(
                        By.XPATH,
                        '//button[normalize-space()="Cancel"]'
                    )
                    cancel.click()
                    sleep(1)

                    button.click()

                sleep(1)
                processed.add(user)

            old_height = self.driver.execute_script(
                "return arguments[0].scrollHeight;", popup
            )

            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight;",
                popup
            )

            sleep(2)

            new_height = self.driver.execute_script(
                "return arguments[0].scrollHeight;", popup
            )

            if new_height == old_height:
                break

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
