'''import bs4
import urllib2
opener = urllib2.build_opener()
#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
my_url = 'https://rateyourmusic.com/customchart'
response = opener.open(my_url)
page = response.read()
soup = soup(page)'''
import json
from selenium import webdriver
chrome_path = r'C:\Users\Jean Carlos\Documents\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.get('https://rateyourmusic.com/customchart')
post = driver.find_element_by_class_name("mbgen").find_elements_by_class_name("chart_detail")
for i in range(0,20):
    dict ={}
    for p in post:
        dict['artist'] = p.find_element_by_class_name("chart_detail_line1").text
        dict['year'] = p.find_element_by_class_name("chart_detail_line2").find_element_by_class_name("chart_year").text
        dict['album_name'] = (str(p.find_element_by_class_name("chart_detail_line2").text).replace(dict['year'], "")).strip()
        dict['genres'] = (p.find_element_by_class_name("chart_detail_line3").find_elements_by_class_name("chart_genres"))
        with open('scrap.json', '+a') as f:
            json.dump(dict, f)
            json.write('\\n,')

    driver.get(str(p.find_element_by_class_name("navlinknext").find_element_by_tag_name('a').get_attribute('href')))
    post = driver.find_element_by_class_name("mbgen").find_elements_by_class_name("chart_detail")

