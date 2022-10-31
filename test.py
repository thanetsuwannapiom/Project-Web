from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey, String
from sqlalchemy.orm import sessionmaker
import csv



engine = sqlalchemy.create_engine('postgresql://webadmin:ONDcqt19301@node37013-watcharakorn.proen.app.ruk-com.cloud:11251/project')#11251
Base = declarative_base()


url = 'https://www.goldtraders.or.th'
req = requests.get(url)
req.encoding = 'utf-8'
sup = BeautifulSoup(req.text,'lxml')


class Data_table(Base):
    __tablename__ = "CopperpriceCheck"
    id = Column(Integer, primary_key=True)
    subject_id = Column(String, nullable=False)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

courses = sup.find(id="DetailPlace_uc_goldprices1_lblAsTime")
courses1 = sup.find(id="DetailPlace_uc_goldprices1_lblBLSell")
courses2 = sup.find(id="DetailPlace_uc_goldprices1_lblBLBuy")
courses3 = sup.find(id="DetailPlace_uc_goldprices1_lblOMSell")
courses4 = sup.find(id="DetailPlace_uc_goldprices1_lblOMBuy")

Session = sessionmaker(bind=engine)
session = Session()


commit_data = Data_table(subject_id = courses.string)
commit_data1 = Data_table(subject_id = courses1.string)
commit_data2 = Data_table(subject_id = courses2.string)
commit_data3 = Data_table(subject_id = courses3.string)
commit_data4 = Data_table(subject_id = courses4.string)

session.add_all([commit_data,commit_data1,commit_data2,commit_data3,commit_data4])

session.commit()