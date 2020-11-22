import json
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/Users/a1101256/Downloads/chromedriver')

try:
    driver.get('https://cafe.naver.com/joonggonara')

    elem = driver.find_element_by_id('topLayerQueryInput')
    elem.send_keys('자전거')
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

    iframe = driver.find_element_by_id('cafe_main')
    driver.switch_to_frame(iframe)
    
    result = []
    
    curr_page = 1
    while True:
        elem = elem = driver.find_element_by_xpath("//div[@id='upperArticleList']/following-sibling::div")
        trs = elem.find_elements_by_xpath('./table/tbody/tr')

        for tr in trs:
            # 각 게시물의 제목을 얻음
            atag = tr.find_element_by_xpath(".//a[@class='article']")
            result.append([atag.text])
            print(atag.text)

        if curr_page == 1:  # break 할 페이지 넘버
            break

        curr_page = curr_page + 1
        # 1, 2 등의 텍스트를 가진 a tag를 찾음
        page = driver.find_element_by_link_text(str(curr_page))
        page.click()

    print(result)
    input()
except Exception as e:
    print(e)
finally:
    driver.close()