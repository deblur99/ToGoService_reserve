from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys


# Open chromedriver where is your project directory and make it go to the desired website
def get_web_driver():
    driver = webdriver.Chrome("C:/Users/deblu/PycharmProjects/reserveToGo/chromedriver.exe")
    driver.get("https://www.galaxytogo.co.kr/reservation/step1")
    return driver # returns the webdriver instance


# On the step 1 page, click "Galaxy Z Flip 3" banner and enter that step 2 page
def go_to_step_2(driver, desired):
    links = driver.find_elements_by_css_selector(".btn > img")

    # find a link about desired item among the button elements
    for link in links:
        print(link.get_attribute("src"))
        if link.get_attribute("src") == desired:
            link.click()
            break

    # method going to step 2 page
    try:
        alert = driver.switch_to.alert
        alert.accept()   # go to step 2 page

    except selenium.common.exceptions.NoAlertPresentException:
        print('Unable to get alert element on your driver.')

    return None

'''
def wait_for_reservation(driver):
    if (driver.):
    region_links = driver.find_elements_by_class_name("btn")
    for region_link in region_links:
        if (region_link.):
'''

def main():
    desired = "https://stg-image.galaxytogo.co.kr/model/52d92ee3-0f68-4b9a-81b8-54020e52a40c.png"

    driver = get_web_driver()
    go_to_step_2(driver, desired)

    driver.implicitly_wait(100000)
    #wait_for_reservation(driver)

    #driver.close()


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
