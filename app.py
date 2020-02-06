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
else:
    html = requests.get(url).content.decode('utf-8')
    wps = WebPageScraper(html)
    most_used_tags = wps.get_most_used_tags(5)

    print('URL to scrap: ' + url)
    print('The wep page has ' + str(wps.get_total_nb_of_elements()) + ' elements. ')
    print('Most used tags are: ')
    for tag in most_used_tags:
        print(' * ' + tag + ' (' + str(most_used_tags[tag]) + ' times)')

