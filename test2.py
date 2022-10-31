from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey, String
from sqlalchemy.orm import sessionmaker
import csv
 

driver = webdriver.Chrome()
driver.get('https://th.investing.com/commodities/metals')


def CopperPrice():
    price  = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[4]').text
    Max    = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[6]').text
    Min    = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[7]').text
    Change = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[9]').text
    Time   = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[10]').text
    Country    = 'USA'

    print(type(price))
    driver.refresh()
    return price , Max , Min , Change , Time , Country

while True:
    price = CopperPrice()
    print('______________________')
    print('Copper :' + price[0])
    print('Max :' + price[1])
    print('Min :'  + price[2])
    print('Change % :' + price[3])
    print('Time :' + price[4])
    print('Coutry :' + price[5])
    print('______________________')
    print(type(price[0]))
    time.sleep(43200)
