#selenium
from selenium import webdriver
import os
from selenium.webdriver import Chrome

#misc
import re
import time

#beautifulsoup
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

import grade_config

#pulling up website
browser = webdriver.Chrome()
browser.get('https://ic.hewlett-woodmere.net/campus/hewlettw.jsp')
#typing in username, password
username = browser.find_element_by_name('username').send_keys(grade_config.personal_username)
password = browser.find_element_by_name('password').send_keys(grade_config.personal_password)
#logging in
login = browser.find_element_by_css_selector('#signinbtn')
login.click()

#hopping on to grades page once logged in
browser.get("https://ic.hewlett-woodmere.net/campus/nav-wrapper/student/portal/student/grades")

#trying to fool websit into thinking im human
time.sleep(3)

#changing frame of reference (iframe)
try:
    iframes = browser.find_elements_by_tag_name('iframe')
    browser.switch_to.frame(iframes[0])
except:
    pass

page_html = browser.page_source

#BeautifulSoup can be used now bc we have static page html ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#grabbing page data in html format
page_soup = soup(page_html, "html.parser")

grade_updates = page_soup.findAll('a')

browser.close()
#getting rid of some unecessary noise
grade_updates.pop(12)
grade_updates.pop(15)

course_name_list = []
course_grade_list = []

def value(num):
    if int(num) < 65:
        return "F"
    elif int(num) > 65 and int(num) < 70:
        return "D"
    elif int(num) > 70 and int(num) < 76:
        return "C"
    elif int(num) >= 76 and int(num) <= 79:
        return "C+"
    elif int(num) >= 80 and int(num) <= 83:
        return "B-"
    elif int(num) >= 84 and int(num) <= 85:
        return "B"
    elif int(num) >= 86 and int(num) <= 89:
        return "B+"
    elif int(num) >=90  and int(num) <= 93:
        return "A-"
    elif int(num) >=94  and int(num) <= 95:
        return "A"
    elif int(num) >=96:
        return "A+"


#loops for name of course and adds it to list
for i in range(0,len(grade_updates),2):
        course_name_list.append(grade_updates[i].text)

#loops for grade (avg) of course and adds to list
for g in range(1,len(grade_updates),2):
        try:
            course_grade_list.append(value((re.search(r'\d+', grade_updates[g].text).group())))
        except:
            course_grade_list.append('N/A')

#pairs course names and grades together
grade_list = [None]*(len(course_name_list)+len(course_grade_list))
grade_list[::2] = course_name_list
grade_list[1::2] = course_grade_list
