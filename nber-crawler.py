import requests
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

fieldnames = ['Paper', 'Author']
driver = webdriver.PhantomJS(executable_path=r'/Users/bernardc/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
writer = csv.writer(open('/Users/bernardc/Downloads/thefile.csv', 'w'))
writer.writerow(fieldnames)

for paper_num in range(7525, 16654):
    driver.get('http://www.nber.org/papers/w' + str(paper_num))
    page_source = driver.page_source
    page = BeautifulSoup(page_source, "lxml")
    row = []

    h1_title = page.select('#mainContentTd h1.title')[0].get_text()
    print (h1_title)
    h2_name = page.select('#mainContentTd h2.bibtop')[0].get_text()
    print (h2_name)
    row.append(h1_title)
    names = h2_name.split(',');

    for name in names:
        row.append(name)

    writer.writerow(row)

driver.close()

