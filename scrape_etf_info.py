#
# help from following sites for coding
#
# handling modal and popup in selenium
#    https://www.youtube.com/watch?v=p_X99_PwFWo
# web scraping with bs4
#    https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
#    https://www.youtube.com/watch?v=4d5px1jFL_A
#
#Shankar helped with Deepa's project-this is the code!-Copied from Shankar's Mac
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.ssga.com/us/en/individual/etfs/fund-finder")

# clear popups
driver.find_element_by_xpath('//*[@id="individual"]').click()
driver.find_elements_by_xpath('//*[@id="js-ssmp-clrButtonLabel"]')[0].click()

elem = driver.find_element_by_xpath('//*[@id="fund-input"]')
elem.clear()
elem.send_keys("EBND")
elem.send_keys(Keys.RETURN)
pg_source = driver.page_source
page_url = driver.find_elements_by_class_name('fundname a')[1].get_attribute('href')
driver.close()

page = requests.get(page_url)

soup = BeautifulSoup(page.text, 'html.parser')

# get all tables
x = soup.find_all(class_ = 'data-table')

tbl = x[0]
tbl_head = [xi.text for xi in x[0].find_all('th')]
tbl_body = []
for xi in tbl.find_all('tr'):
    drow = [xii.text for xii in xi.find_all('td')]
    tbl_body.append(drow)

