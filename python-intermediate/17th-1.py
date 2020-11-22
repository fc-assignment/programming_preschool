import json
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# ID, PW를 가져오는 방식은 강의 원 내용대로 쓰시거나 아래와 같이 json 파일형태로 사용하실 수 있으십니다.
# {"username": "", "password": ""}
with open('/Users/a1101256/keys/fc-test-insta-account.json') as f:
    account_info = json.load(f)

driver = webdriver.Chrome('/Users/kadencho/chromedriver')

try:
    driver.get('https://instagram.com')

    try:
        elem = driver.find_element_by_link_text('Log In')  # 한글의 경우 Log In -> 로그인
        elem.click()
    except NoSuchElementException as e:
        pass

    time.sleep(1)

    elem = driver.find_element_by_name('username')
    elem.send_keys(account_info['username'])
    elem = driver.find_element_by_name('password')
    elem.send_keys(account_info['password'])
    elem.send_keys(Keys.RETURN)

    time.sleep(3)
    input()
    elem = driver.find_element_by_class_name('coreSpriteSearchIcon')
    ac = ActionChains(driver)
    ac.move_to_element(elem)
    ac.click()
    ac.send_keys('#패스트캠퍼스')
    ac.perform()

    time.sleep(3)

    # stale element reference가 계속 발생하여 reset_actions() 대신 ac 재생성
    ac = ActionChains(driver)
    ac.move_by_offset(0, 50)
    ac.click()
    ac.perform()
    
    # 위의 move 대신 아래 사용가능
    # elem = driver.find_element_by_class_name('coreSpriteHashtag')
    # elem.click()
 
    time.sleep(3)

    # find_element_by_class_name을 쓰기 위해 자동 생성 클래스명 사용 ㅜ
    elem = driver.find_element_by_class_name('EZdmt') 
    imgs = elem.find_elements_by_tag_name('img')

    for img in imgs:
        ac = ActionChains(driver)
        ac.move_to_element(img)
        ac.click()
        ac.perform()

        time.sleep(1)

        try:
            ac = ActionChains(driver)
            elem = driver.find_element_by_css_selector("[aria-label=Like][width='24']") # 한글의 경우 Like -> 좋아요
            ac.move_to_element(elem)
            ac.click()
            ac.perform()
        except Exception:
            print('Already Liked')

        ac = ActionChains(driver)
        ac.send_keys(Keys.ESCAPE)
        ac.perform()

except Exception as e:
    print(e)
finally:
    driver.quit()