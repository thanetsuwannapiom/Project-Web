import requests
from bs4 import BeautifulSoup

webURL = 'https://www.mitrade.com/th/financial-tools/COPPER'
r = requests.get(webURL)
r.encoding = 'utf-8'
sup = BeautifulSoup(r.text,'lxml')

def CopperPriceCheck():
    PriceCheck = sup.find('span',{'id'}).text    
    PriceCheck2 = sup.find('strong',{'class':'sell-price-num'}).text    
    
    print(PriceCheck)
    print(PriceCheck2)   

CopperPriceCheck()       
