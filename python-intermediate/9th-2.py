from selenium import webdriver

driver = webdriver.Chrome('/Users/kadencho/chromedriver')

try:
    driver.get('http://news.naver.com')

    elem = driver.find_element_by_class_name('section_list_ranking_press')

    atags = elem.find_elements_by_class_name("list_tit")

    for atag in atags:
        print(atag.text)

except Exception as e:
    print(e)
finally:
    driver.quit()