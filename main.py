from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

def run():
    options = Options()
    # options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.facebook.com")
    print(driver.title)
    email = driver.find_element_by_id("email")
    email.send_keys("gmail")
    print(email.text)
    password = driver.find_element_by_id("pass")
    password.send_keys("password")
    password.send_keys(Keys.RETURN)

    # post.send_keys("I am posting this on facebook")
    # post.send_keys(Keys.RETURN)
    # print(post)
    post2 = driver.find_elements_by_xpath("//span[@display='-webkit-box']")
    print(post2)



if __name__ == '__main__':
    run()


