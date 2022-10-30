from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.mitrade.com/th/financial-tools/COPPER')

def CopperPrice():
    price  = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div[2]/p[1]/span[1]').text
    Max    = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div[2]/p[2]/span[1]').text
    Min    = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div[2]/p[2]/span[2]').text
    Change = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div[2]/p[1]/span[2]').text
    Sell   = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div[3]/a[1]/strong').text
    Buy    = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div[3]/a[2]/strong').text


    driver.refresh()
    return price , Max , Min , Change , Sell , Buy

while True:
    price = CopperPrice()
    print('______________________')
    print('Copper :' + price[0])
    print(price[1])
    print(price[2])
    print('Change % :' + price[3])
    print('Sell :' + price[4])
    print('Buy :' + price[5])
    print('______________________')

    time.sleep(10)

