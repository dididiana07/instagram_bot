from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstagramBot:
    def __init__(self, chromedriver_path, ig_user, ig_password, **kwargs):
        """Initialize the InstagramBot class."""
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.user = ig_user
        self.password = ig_password
        self.instagram_url = "http://instagram.com"
        self.account_instagram = kwargs["get_followers_from"]

    def __str__(self):
        """Return this string when you try to print the class."""
        return f"Instagram Bot {self.user} - Follow People"

    def login_instagram(self):
        """Log into your instagram account."""
        accept_cookies = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/' \
                         'div/div/div/div[2]/div/button[1]'
        self.driver.get(url=self.instagram_url)
        sleep(5)
        self.driver.find_element(By.XPATH, accept_cookies).click()
        sleep(5)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        sleep(10)
        self.followers_of()

    def followers_of(self):
        search = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/' \
                 'div[2]/div/a/div/div[1]/div'
        div = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div'
        search_btn = self.driver.find_element(By.XPATH, search)
        search_btn.click()
        sleep(5)
        search_bar = self.driver.find_element(By.CSS_SELECTOR, "div input")
        search_bar.send_keys(self.account_instagram)
        sleep(5)
        results = [account for account in self.driver.find_elements(By.CSS_SELECTOR, 'div a') if len(account.text) != 0]
        first_result = results[0]
        first_result.click()
        sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, "div ul li a")
        followers.click()
        sleep(5)
        followers_div = self.driver.find_element(By.XPATH, div)
        followers_account = followers_div.find_elements(By.CSS_SELECTOR, "div button")
        followers_buttons = [account for account in followers_account if len(account.text) != 0]
        for follower_button in followers_buttons:
            follower_button.click()
        sleep(10)



