from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:/Users/Дмитрий/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.ru/")

driver.find_element(By.XPATH," /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("купить кофемашину bork c804")

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
