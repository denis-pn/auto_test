from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def open_site(site, word_search): # Открытие браузера и сайта
    try:
        driver = webdriver.Chrome()
        driver.get(site)
        find_searchbox(driver, word_search)
    except:
        sys.exit("Ошибка: Сайт недоступен")

def find_searchbox(driver, word_search): # Поиск и выделение поля для поиска
    if len(driver.find_element_by_xpath('//*[@id="text"]').size) > 0:
        searchbox = driver.find_element_by_xpath('//*[@id="text"]')
        send_keys(driver, searchbox, word_search)
    else:
        sys.exit("Ошибка: Поле поиска отсутствует")

def send_keys(driver, searchbox, word_search): # Набор текста
    searchbox.send_keys("Тензор")
    find_and_check_element(driver, searchbox, word_search)

def find_and_check_element(driver, searchbox, word_search): # Проверка наличия Suggest
    driver.find_element_by_css_selector('.mini-suggest__input')
    texts = [e.text for e in driver.find_elements_by_css_selector('li[id^="suggest-item-"]')]
    if len(texts) > 0:
       print("Таблица с подсказками появилась")
    else:
        print("Таблица с подсказками не появилась")
    press_search(driver, searchbox, word_search)

def press_search(driver, searchbox, word_search): # Нажатие на ENTER
    searchbox.send_keys(Keys.ENTER)
    check_results(driver, word_search)

def check_results(driver, word_search): # Проверка наличия tensor.ru в результатах
    i = 1
    check = 0
    a = []
    a.append(word_search)
    while i != 6:
        texts = [e.text for e in driver.find_elements_by_xpath('//*[@id="search-result"]/li[%s]/div/div[1]/div[1]/a/b' % i)]
        if texts == a:
            check += 1
        i += 1
    if check > 0:
        print("В пяти первых результатах есть ссылка на tensor.ru")
    else:
        print("В пяти первых результатах нет ссылки на tensor.ru")




if __name__ == '__main__':
    driver = open_site('https://yandex.ru/', 'tensor.ru')

