import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#Открытие страницы входа
s = Service('C:/Users/Дмитрий/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://mail.yandex.ru/")
driver.find_element(By.CSS_SELECTOR, "#root > div > div.PSHeader."
                                     "PSHeader_theme_light.PSHeader_noCenter.Header"
                                     "_2LmwLn89QheMR2KyKhEGlR.PSHeader_LW3jBtGE8p"
                                     "_8DMgGbrX_v > div.PSHeader-Right > button").click()
#Ввод логина#
driver.find_element(By.ID, "passp-field-login").send_keys("te5t.aa")
driver.find_element(By.ID, "passp:sign-in").click()

#Ввод пароля
time.sleep(2)
driver.find_element(By.ID, "passp-field-passwd").send_keys("nK6BR2M5DU6EHnS")
driver.find_element(By.ID, "passp:sign-in").click()
