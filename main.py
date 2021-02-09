import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

def twitterPost():

    # Facebook login
    # options = Options()
    # # options.add_argument("--headless")
    #
    # driver = webdriver.Firefox(options=options)
    # driver.get("https://www.facebook.com")
    # print(driver.title)
    # email = driver.find_element_by_id("email")
    # email.send_keys("mahadmunir10@gmail.com")
    # print(email.text)
    # password = driver.find_element_by_id("pass")
    # password.send_keys("mahadmuneer1456")
    # password.send_keys(Keys.RETURN)
    #
    # # post.send_keys("I am posting this on facebook")
    # # post.send_keys(Keys.RETURN)
    # # print(post)
    # post = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div")
    # print('post')

    # Twitter login
    options = Options()

    driver = webdriver.Firefox(options=options)
    driver.get("https://twitter.com/login")
    time.sleep(5)
    email = driver.find_element_by_name("session[username_or_email]")
    email.send_keys("03040072542")
    password = driver.find_element_by_name("session[password]")
    password.send_keys("Maddy6234")
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    tweetBtn = driver.find_element_by_xpath("//a[@aria-label='Tweet']")
    tweetBtn.click()
    time.sleep(2)
    textbox = driver.find_element_by_xpath("//div[@role='textbox']")
    textbox.send_keys("My First Tweet")
    button = driver.find_element_by_xpath("//div[@data-testid='tweetButton']")
    button.click()



if __name__ == '__main__':
    twitterPost()


