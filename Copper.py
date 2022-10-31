from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey, String
from sqlalchemy.orm import sessionmaker

 
engine = sqlalchemy.create_engine('postgresql://webadmin:VCNtps41396@node37019-thanet.proen.app.ruk-com.cloud:11235/project') 
Base = declarative_base()


class COPPER(Base):
        __tablename__ = 'copper'
        Price = Column(String(13),nullable=True)
        Max = Column(String(30),nullable=True)
        Min = Column(String(30),nullable=True)
        Change = Column(String(10),nullable=True)
        Time = Column(String(30),nullable=True)
        Country = Column(String(10),primary_key=True,nullable=True)

        def __repr__(self) :
                return '<User(Price = {} , Max = {} , Min = {} , Change = {}, Time = {} , Country = {})>'.format(self.Price,self.Max,self.Min,self.Change,self.Time,self.Country)

driver = webdriver.Chrome()
driver.get('https://th.investing.com/commodities/metals')

def CopperPrice():
    price  = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[4]').text
    max    = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[6]').text
    min    = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[7]').text
    change = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[9]').text
    times   = driver.find_element(By.XPATH,'//*[@id="pair_959211"]/td[10]').text
    country    = "USA"
    price2  = driver.find_element(By.XPATH,'//*[@id="pair_8831"]/td[4]').text
    max2    = driver.find_element(By.XPATH,'//*[@id="pair_8831"]/td[6]').text
    min2    = driver.find_element(By.XPATH,'//*[@id="pair_8831"]/td[7]').text
    change2 = driver.find_element(By.XPATH,'//*[@id="pair_8831"]/td[9]').text
    times2   = driver.find_element(By.XPATH,'//*[@id="pair_8831"]/td[10]').text
    country2    = "US"
    price3  = driver.find_element(By.XPATH,'//*[@id="pair_49771"]/td[4]').text
    max3    = driver.find_element(By.XPATH,'//*[@id="pair_49771"]/td[6]').text
    min3    = driver.find_element(By.XPATH,'//*[@id="pair_49771"]/td[7]').text
    change3 = driver.find_element(By.XPATH,'//*[@id="pair_49771"]/td[9]').text
    times3   = driver.find_element(By.XPATH,'//*[@id="pair_49771"]/td[10]').text
    country3    = "IND"


    driver.refresh()
    return price , max , min , change , times , country , price2 , max2 , min2 , change2 , times2 , country2 , price3 , max3 , min3 , change3 , times3 , country3

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

price = CopperPrice()
c1 = COPPER(Price= price[0] ,Max=price[1],Min=price[2],Change=price[3],Time=price[4],Country=price[5])
c2 = COPPER(Price= price[6] ,Max=price[7],Min=price[8],Change=price[9],Time=price[10],Country=price[11])
c3 = COPPER(Price= price[12] ,Max=price[13],Min=price[14],Change=price[15],Time=price[16],Country=price[17])


session.add_all([c1,c2,c3])
print(session.query(COPPER).all())
session.commit()

'''
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

    time.sleep(43200)

'''
