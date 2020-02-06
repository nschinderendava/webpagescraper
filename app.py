from web_page_scraper import WebPageScraper
from web_page_scraper_test import WebPageScraperTest

import requests, argparse

parser = argparse.ArgumentParser(description='This is a Web Page Scraper')
parser.add_argument("--u")
parser.add_argument("--a")

args = parser.parse_args()

url = args.u
action = args.a

if action == 'test':
    wpst = WebPageScraperTest()
    wpst.run()
elif action == 'all_tags':
    html = requests.get(url).content.decode('utf-8')
    wps = WebPageScraper(html)
    output = wps.get_tags()
    print(output)
else:
    html = requests.get(url).content.decode('utf-8')
    wps = WebPageScraper(html)
    output = wps.get_most_used_tags(5)
    print(output)

