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
import random
import time
chrome_path = r'C:\Users\Jean Carlos\Documents\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.get('https://rateyourmusic.com/customchart?page='+str(88)+'&chart_type=top&type=single&year=alltime&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=')
#driver.get('https://rateyourmusic.com/customchart?page=1&chart_type=top&type=ep&year=alltime&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=')


for i in range(88,126):
    if driver.find_element_by_class_name("mbgen").find_elements_by_class_name("chart_detail"):
        post = driver.find_element_by_class_name("mbgen").find_elements_by_class_name("chart_detail")
        post1 = driver.find_element_by_class_name("mbgen").find_elements_by_class_name("chart_stats")
    else:
        time.sleep(3)
        post = driver.find_element_by_class_name("mbgen").find_elements_by_class_name("chart_detail")
        post1 = driver.find_element_by_class_name("mbgen").find_elements_by_class_name("chart_stats")
    d = len(post)
    l = []
    for p in range(0, d):
        year = (post[p].find_element_by_class_name("chart_detail_line2").find_element_by_class_name("chart_year").text).replace('(','').replace(')', '')
        k = {
                'type': "Singles",
                'artist': post[p].find_element_by_class_name("chart_detail_line1").text,
                'year': year,
                'album_name': (str(post[p].find_element_by_class_name("chart_detail_line2").text).replace('(' + year + ')', "")).strip(),
                'genres': [x for x in (post[p].find_element_by_class_name("chart_detail_line3").text).split(',')],
                'score': float(post1[p].find_elements_by_tag_name('b')[0].text),
                'ratings': int((post1[p].find_elements_by_tag_name('b')[1].text).replace(',',''))
            }
        with open('scrapSingles.json', '+a') as f:
            json.dump(k, f, indent=2)
    print('pagina ' + str(i+1))
    time.sleep(random.randint(5, 7))
    if random.randint(1,3)>2:
        driver.get('https://rateyourmusic.com/customchart?page='+str(i+1)+'&chart_type=top&type=single&year=alltime&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=')
    else:
        if driver.find_element_by_class_name("navlinknext").click():
            driver.find_element_by_class_name("navlinknext").click()
        else:
            driver.get('https://rateyourmusic.com/customchart?page='+str(i+1)+'&chart_type=top&type=single&year=alltime&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=')
    '''if driver.find_element_by_class_name("navlinknext") and driver.find_element_by_class_name("mbgen"):
        if driver.find_element_by_class_name("navlinknext").click():
            driver.find_element_by_class_name("navlinknext").click()
        else:
            time.sleep(3)
            driver.find_element_by_class_name("navlinknext").click()'''

#driver.quit()

