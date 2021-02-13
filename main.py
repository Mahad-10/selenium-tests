import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.action_chains import ActionChains


# Listener class to listen to events
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


# Driver for Chrome
def createChromeDriver():
    options = ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver


# Driver for Chrome
def createFirefoxDriver():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    return driver


# Facebook login
def facebookLogin(driver, email, password):
    driver.get("https://www.facebook.com")
    emailInput = driver.find_element_by_id("email")
    emailInput.send_keys(email)
    passwordInput = driver.find_element_by_id("pass")
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.RETURN)
    print("Facebook Login Successful")


# Twitter login and tweet
def twitterPost(driver, email, password):
    driver.get("https://twitter.com/login")
    time.sleep(5)
    emailInput = driver.find_element_by_name("session[username_or_email]")
    emailInput.send_keys(email)
    passwordInput = driver.find_element_by_name("session[password]")
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.RETURN)
    time.sleep(5)

    tweetBtn = driver.find_element_by_xpath("//a[@aria-label='Tweet']")
    tweetBtn.click()
    time.sleep(2)
    textbox = driver.find_element_by_xpath("//div[@role='textbox']")
    textbox.send_keys("My First Tweet")
    button = driver.find_element_by_xpath("//div[@data-testid='tweetButton']")
    button.click()


# Get World Population
def worldPopulation(driver):
    edriver = EventFiringWebDriver(driver, Mylistener())
    edriver.get("https://www.worldometers.info/world-population/")


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

    for country in edriver.find_elements_by_class_name("t20-country"):
        print(country.text)

    worldPopulation(driver)

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")


def cookieClick():
    driver.implicitly_wait(5)
    cookie = driver.find_element_by_id("bigCookie")
    cookie_count = driver.find_element_by_id("cookies")
    items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

    actions = ActionChains(driver)
    actions.click(cookie)

    for i in range(20):
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])

        for item in items:
            value = int(item.text)

            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()
    cookieClick()

    driver.quit()


if __name__ == '__main__':
    driver = createChromeDriver()
    worldPopulation(driver)
    driver.quit()
    # cookieClick()
