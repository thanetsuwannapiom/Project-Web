import requests
from bs4 import BeautifulSoup

webURL = 'https://www.mitrade.com/th/financial-tools/COPPER'
r = requests.get(webURL)
r.encoding = 'utf-8'
sup = BeautifulSoup(r.text,'lxml')


course_list = []

courses = sup.find_all('span',{'class':'nowPrice'})


for course in courses:

    # Create a new variable --> obj to store 
    # only course name getting rid of unwanted tags
    obj = course

    # Append each course into a course_list variable
    course_list.append(obj)
print(course_list)