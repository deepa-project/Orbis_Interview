"""
from website:https://realpython.com/python-web-scraping-practical-introduction/

"""
from urllib.request import urlopen
#The above package opens an url
#Below is the url from the example
url = "http://www.spdrs.com"
#using the package to open the url
page = urlopen(url)
#The value of page in my idle:
#>>> page
#<http.client.HTTPResponse object at 0x0000013DA6B144F0>

#
#To extract the HTML from the page, first use the HTTPResponse object’s .read() method,
# which returns a sequence bytes. Then use .decode() to decode the bytes to a string using UTF-8:
html_bytes = page.read()

html = html_bytes.decode("utf-8")
print(html)