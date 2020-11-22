from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/a1101256/Downloads/chromedriver')

try:
    driver.get('https://naver.com')

    elem = driver.find_element_by_id('query')
    elem.send_keys('패스트캠퍼스')
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_class_name('_blogBase')
    lis = elem.find_elements_by_tag_name('li')
    for li in lis:
        atag = li.find_element_by_class_name('sh_blog_title')
        print(atag.get_attribute('title'))
        print(atag.get_attribute('href'))

    print('-'*20)

    elem = driver.find_element_by_class_name('news')
    lis = elem.find_elements_by_xpath('./ul/li')
    for li in lis:
        atag = li.find_element_by_class_name('_sp_each_title')
        print(atag.text)
        print(atag.get_attribute('href'))

    print('-'*20)

    elem = driver.find_element_by_class_name('_cafeBase')
    lis = elem.find_elements_by_tag_name('li')
    for li in lis:
        atag = li.find_element_by_class_name('sh_cafe_title')
        title = atag.get_attribute('title')
        if not title:
            title = atag.text
        print(title)
        print(atag.get_attribute('href'))

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()
