import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class Mylistener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("before_navigate_to %s" % url)

    def after_navigate_to(self, url, driver):
        print("after_navigate_to %s" % url)

    def before_click(self, element, driver):
        print("before_click %s" % element)

    def after_click(self, element, driver):
        print("after_click %s" % element)

    def after_navigate_forward(self, driver):
        print("after_navigate_forward");

    def before_navigate_forward(self, driver):
        print("before_navigate_forward")

    def after_navigate_back(self, driver):
        print("after_navigate_back")

    def before_navigate_back(self, driver):
        print("before_navigate_back")

    def before_change_value_of(self, element, driver):
        print("before_change_value_of")

    def after_change_value_of(self, element, driver):
        print("Value Changed")


listener = Mylistener()


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


def worldMeter():
    driver = webdriver.Firefox()
    edriver = EventFiringWebDriver(driver, Mylistener())
    edriver.get("https://www.worldometers.info/world-population/")
    time.sleep(5)

    # Get Births Today
    birth_today = edriver.find_elements_by_xpath("//span[@rel='births_today']")
    listener.after_change_value_of(birth_today[0], edriver)
    print(f"Birth Today : {birth_today[0].text}")

    # Get Births this Year
    birth_year = edriver.find_elements_by_xpath("//span[@rel='births_this_year']")
    listener.after_change_value_of(birth_year[0], edriver)
    print(f"Birth this Year : {birth_year[0].text}")

    # Get Deaths Today
    death_today = edriver.find_elements_by_xpath("//span[@rel='dth1s_today']")
    listener.after_change_value_of(death_today[0], edriver)
    print(f"Death Today : {death_today[0].text}")

    # Get Deaths this Year
    death_year = edriver.find_elements_by_xpath("//span[@rel='dth1s_this_year']")
    listener.after_change_value_of(death_year[0], edriver)
    print(f"Death this Year : {death_year[0].text}")

    # Get Population Growth Today
    population_growth_today = edriver.find_elements_by_xpath("//span[@rel='absolute_growth']")
    listener.after_change_value_of(population_growth_today[0], edriver)
    print(f"Population Growth Today : {population_growth_today[0].text}")

    # Get Population Growth this Year
    population_growth_year = edriver.find_elements_by_xpath("//span[@rel='absolute_growth_year']")
    listener.after_change_value_of(population_growth_year[0], edriver)
    print(f"Population Growth this Year : {population_growth_year[0].text}")



if __name__ == '__main__':
    worldMeter()


