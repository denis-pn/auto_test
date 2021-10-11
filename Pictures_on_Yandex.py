from selenium import webdriver
import time

def open_site(site): # Открытие браузера и сайта
    driver = webdriver.Chrome()
    driver.get(site)
    find_batton_image(driver)

def find_batton_image(driver): # Поиск и клик по кнопке картинка
    searh = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a/div[2]').click()
    check_URL(driver)

def check_URL(driver): # Проверка URL
    window_after = driver.window_handles[2]
    driver.switch_to_window(window_after)
    if driver.current_url.find("https://yandex.ru/images/", 0) == 0:
        print("URL: https://yandex.ru/images/")
    open_first_category(driver, window_after)

def open_first_category(driver, window_after): #Открытие первой категории
    elem = driver.find_element_by_class_name('PopularRequestList-SearchText').text
    driver.find_element_by_class_name('PopularRequestList-SearchText').click()
    check_text(elem, driver, window_after)

def check_text(elem, driver, window_after): #Проверка на соответствие страницы
    elem_ = driver.find_element_by_xpath("html").text
    mas = []
    for i in elem_.split():
        try:
            mas.append(i)
        except ValueError:
            pass

    mas_ = []
    for i in elem.split():
        try:
            mas_.append(i)
        except ValueError:
            pass
    caunter = 0
    for i in mas:
        if i == mas_[0]:
            caunter += 1
    if caunter >0:
        print("В поиске верный текст")

    time.sleep(2)

    open_first_image(driver, window_after)

def open_first_image(driver, window_after): #Открытие первой картинки и проверка

    driver.find_element_by_class_name('serp-item__link').click()
    time.sleep(3)
    if driver.find_element_by_class_name('MMImage-Origin'):
        print("Картинка открылась")
    else:
        driver.find_element_by_class_name('serp-item__link').click()
    moving(driver)

def moving(driver):
    one = driver.find_element_by_class_name('MMImage-Origin')

    driver.find_element_by_class_name('CircleButton_type_next').click()
    driver.find_element_by_class_name('CircleButton_type_prev').click()

    two = driver.find_element_by_class_name('MMImage-Origin')

    if one == two:
        print("Это то же изображение")
    else:
        print("Это другое изображение ")



if __name__ == '__main__':
    driver = open_site('https://yandex.ru/')