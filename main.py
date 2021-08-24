from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from datetime import datetime


# Open chromedriver where is your project directory and make it go to the desired website
def get_web_driver(file_path, url):
    driver = webdriver.Chrome(file_path)
    driver.get(url)
    return driver # returns the webdriver instance


# On the step 1 page, click "Galaxy Z Flip 3" banner and enter that step 2 page
def go_to_desired_item_page(driver, desired_item_url):
    links = driver.find_elements_by_css_selector(".btn > img")

    # find a link about desired item among the button elements
    for link in links:
        print(link.get_attribute("src"))
        if link.get_attribute("src") == desired_item_url:
            link.click()
            break

    # method going to step 2 page
    try:
        alert = driver.switch_to.alert
        alert.accept()   # go to step 2 page

    except selenium.common.exceptions.NoAlertPresentException:
        print('Unable to get alert element on your driver.')

    return None


def get_info_stores(driver, url):
    store_info_lists = list()

    try:
        # Find region links (e.g: Seoul, Gyeong-gi/Incheon, ... )
        if driver.current_url == url:
            region_links = driver.find_elements_by_css_selector(".location > a")
        else:
            raise ValueError

        for region_link in region_links:
            if region_link.get_attribute("innerText") == "경기/인천":
                region_link.click() # Move to the specified region section
                break

        reserve_shops = driver.find_elements_by_css_selector(".store_list > .list > li")

        # Get info about stores what you want to go
        for reserve_shop in reserve_shops:
            store_info_list = list()

            store_name = reserve_shop.find_element_by_css_selector("dl > dt").get_attribute("innerText")
            store_address = reserve_shop.find_element_by_css_selector("dl > dd").get_attribute("innerText")
            store_remaining = reserve_shop.find_element_by_css_selector(".status > strong").get_attribute("innerText")[:-1]

            store_info_list.append(store_name)
            store_info_list.append(store_address)
            store_info_list.append(store_remaining)

            store_info_lists.append(store_info_list)

            '''
            # for finding activated button
            select_button = reserve_shop.find_element_by_css_selector(".lnk > a:last-child")
            print(select_button.get_attribute("innerText"))
            
            # for noticing any vacant stores
            vacant_store = reserve_shop.find_element_by_css_selector("p.status > strong").get_attribute("innerText")
            if (vacant_store != "0대"):
                print(datetime.now(), "에 발견!")
            '''

        return store_info_lists

    except:
        print("An error occurred")
        return None


def get_whitelist_from_user():
    # retrieve user's whitelist
    whitelist = list()
    device = 0
    region_dict = {
        1: "서울",
        2: "경기/인천",
        3: "충청/강원",
        4: "경상/제주",
        5: "전라"
    }
    prefer_cities = list()

    while True:
        try:
            # 1) select a set of devices
            print("")
            print("-" * 20)
            print("대여를 희망하는 기종을 선택해주세요")
            print("1. Galaxy Z Flip 3")
            print("2. Galaxy Z Flip 3, Watch 4")
            print("3. Galaxy Z Flip 3, Watch 4 Classic")
            print("4. Galaxy Z Fold 3")
            print("5. Galaxy Z Fold 3, Watch 4")
            print("6. Galaxy Z Fold 3, Watch 4 Classic")
            print("-" * 20)
            print("")

            decision = int(input("선택 : "))

            if (decision < 1 or decision > 6):
                raise ValueError

            whitelist.append(decision)

            # 2) select regions where you are willing to go
            print("")
            print("-" * 20)
            print("매장이 위치한 지역들 중 희망하는 지역을 선택해주세요")
            print("1. 서울")
            print("2. 경기/인천")
            print("3. 충청/강원")
            print("4. 경상/제주")
            print("5. 전라")
            print("-" * 20)
            print("")

            decision = int(input("선택 : "))

            if (decision < 1 or decision > 5):
                raise ValueError

            whitelist.append(region_dict[decision])

            # 3) specify city where you are really willing to go
            print("")
            print("-" * 20)
            print("우선적으로 방문하고자 하는 시를 입력하세요")
            print("여러 개 입력 가능하며, 공백으로 각 시를 구분합니다.")
            print("-" * 20)
            print("")

            decision = input("선택 : ")

            whitelist.append(decision.split(" "))

            return whitelist

        except:
            print("입력 값을 확인해주세요.")
            continue


if __name__ == "__main__":
    file_path = "C://Users//deblu//PycharmProjects//reserve_ToGo//chromedriver.exe"
    step1_url = "https://www.galaxytogo.co.kr/reservation/step1"
    desired_item_url = "https://stg-image.galaxytogo.co.kr/model/52d92ee3-0f68-4b9a-81b8-54020e52a40c.png"
    step2_url = "https://www.galaxytogo.co.kr/reservation/step2"

    whitelist = get_whitelist_from_user()
    print(whitelist)

    driver = get_web_driver(file_path, step1_url)
    go_to_desired_item_page(driver, desired_item_url)
    store_info_lists = get_info_stores(driver, step2_url)
    #driver.close()