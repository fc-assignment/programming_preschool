from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/kadencho/chromedriver')

try:
    driver.get('https://naver.com')

    elem = driver.find_element_by_id('query')
    elem.send_keys('패스트캠퍼스')
    elem.send_keys(Keys.RETURN)
    
    elem = driver.find_element_by_xpath("//section[contains(@class, '_prs_web_gen')]")
    lis = elem.find_elements_by_tag_name('li')

    for li in lis:
        div = li.find_element_by_class_name('total_tit')
        atag = div.find_element_by_tag_name("a")
        print(div.text)
        print(atag.get_attribute('href'))

    print('-'*20)
    elem = driver.find_element_by_xpath("//h2[contains(text(), '뉴스')]/../..")
    lis = elem.find_elements_by_xpath(".//ul[@class='list_news']/li")
    for li in lis:
        atag = li.find_element_by_class_name('news_tit')
        print(atag.text)
        print(atag.get_attribute('href'))

    print('-'*20)

    elem = driver.find_element_by_xpath("//h2[contains(text(), '동영상')]/../..")
    lis = elem.find_elements_by_tag_name('li')
    for li in lis:
        atag = li.find_element_by_class_name('info_title')
        title = atag.text
        print(title)
        print(atag.get_attribute('href'))

except Exception as e:
    print(e)
finally:
    driver.quit()
