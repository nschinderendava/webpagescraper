from web_page_scraper import WebPageScraper
from web_page_scraper_test import WebPageScraperTest
import requests

url = 'https://www.pequenitosbabyshop.com.ar/'
html = requests.get(url).content.decode('utf-8')

wps = WebPageScraper(html)
output = wps.get_most_used_tags(5)

wpst = WebPageScraperTest()
wpst.run()
''' 
html = '<html><head attr="dlalal"><title>JournalDev HTMLParser</title></head><body attr="lala">' \
       '<div>lalalala</div><h2>Prueba</h2><h1 attr="prueba" >Python html.parse module</h1><div attr="lalaatdiv">holis</div>' \
        '<div><div><!-- COMMENT <!-- COMMENT 2 <h2>Lalala</h2>--> --></div></div>' \
       '</body><footer>lalala aldjskasd</footer></html>'
'''

print(output)
