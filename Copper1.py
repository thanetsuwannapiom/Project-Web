
import requests
from bs4 import BeautifulSoup

webURL = 'https://www.mitrade.com/th/financial-tools/COPPER'
r = requests.get(webURL)
r.encoding = 'utf-8'
sup = BeautifulSoup(r.text,'lxml')

def CopperPriceCheck():
    PriceCheck = sup.find_all('div')
    #PriceCheck2 = sup.find('span',{'class':'dailyPercent'}).text    
    
    print(PriceCheck)
    #print(PriceCheck2)   

CopperPriceCheck()       