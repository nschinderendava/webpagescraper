from web_page_scraper import WebPageScraper
from web_page_scraper_test import WebPageScraperTest

import requests, argparse

def main():
    parser = argparse.ArgumentParser(description='This is a Web Page Scraper')
    parser.add_argument("--u", help="URL to scrap (mandatory if we are not running tests)")
    parser.add_argument("--t", help="use this param to run tests", default=False, type=bool)

    args = parser.parse_args()

    url = args.u
    run_tests = args.t

    if run_tests:
        wpst = WebPageScraperTest()
        wpst.run()
    else:
        try:
            if not url:
                print('You must provide a URL')
            html = requests.get(url).content.decode('utf-8')
            wps = WebPageScraper(html)
            most_used_tags = wps.get_most_used_tags(5)
            total_nb_of_elements = wps.get_total_nb_of_elements()
            print('URL to scrap: ' + url)
            print('The page has ' + str(total_nb_of_elements) + ' elements. ')
            if total_nb_of_elements:
                nb_of_tags = wps.get_total_nb_of_html_tags()
                print('Number of HTML tags: ' + str(nb_of_tags))
                print('Most used tags are: ')
                for tag in most_used_tags:
                    print(' * ' + tag + ' (' + str(most_used_tags[tag]) + ' times)')
        except Exception as err:
            print("The script failed: {0}".format(err))

if __name__ == '__main__':
    main()