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
    email.send_keys("mahadmunir10@gmail.com")
    print(email.text)
    password = driver.find_element_by_id("pass")
    password.send_keys("mahadmuneer1456")
    password.send_keys(Keys.RETURN)

    post = driver.find_element_by_class_name("a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7")
    # post.send_keys("I am posting this on facebook")
    # post.send_keys(Keys.RETURN)
    print(post)
    driver.find_elements_by_xpath()



if __name__ == '__main__':
    run()


