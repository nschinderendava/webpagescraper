from web_page_scraper import WebPageScraper

class WebPageScraperTest:

    def __init__(self):
        self.failures_counter = 0

    def run(self):
        self.test_scrap()

        if self.failures_counter > 0:
            print(str(self.failures_counter) + ' tests failed')
        else:
            print('all tests passed')

    def test_scrap(self):
        html1 = """
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body attr="attr1">
                    <div>lalalala</div>
                    <h2>Prueba</h2>
                    <h1 attr="prueba">Python test</h1>
                    <div attr="lalaatdiv">hello</div>
                </body>
                <footer>lalala aldjskasd</footer>
            </html>"""
        html2 = """
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body>
                    <h1 attr="prueba">Python test</h1>
                    <div attr="div1">hello 1</div>
                    <div attr="div2">hello 2</div>
                    <div attr="div3">hello 3</div>
                </body>
            </html>"""
        html3 = """
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body>
                    <h1 attr="prueba">Python test</h1>
                    <div attr="div1">hello 1</div>
                    <div attr="div2">hello 2</div>
                    <div attr="div3">hello 3</div>
                    <!-- COMMENT HERE -->
                    <h2>Subtitle 1</h2>
                    <div attr="div4 wrapper">
                        <!-- COMMENT HERE -->
                        <div attr="div4 child1">hello 1</div>
                        <div attr="div4 child1">hello 2</div>
                        <div attr="div4 child1">hello 3</div>
                    </div>
                    <!-- <form id="searchform" method="get" action="https://cse.google.com/cse?cx=001850405712132341878:zpzujznek7w" style="margin:0; padding:0; height:32px; float:left;">' \
                    <input type="hidden" name="site" value="my_collection"/>' \
                    <!-- <label for="searchinputbox" style="margin-left:-999px; margin-top:0; font-size:10px;">Enter search term:</label>-->' \
                    <!-- <input type="text" name="q" id="searchinputbox" alt="searchinputbox" size="20" maxlength="255" value="" style="margin-right:6px;float:left;" aria-label="textbox for Search"/><input type="submit" name="btnG" value="search" id="searchbutton" style="padding:1px 8px; float:right; margin-left:0;margin-top:-1px;">-->' \
                    </form> -->
                    <h2>Subtitle 2 </h2>
                    <div attr="div5">hello 5</div>
                </body>
            </html>"""
        tests = [
            {
                'html': html1,
                'expected': {
                    'div': 2,
                    'h2': 1,
                    'h1': 1
                }
            },
            {
                'html': html2,
                'expected': {
                    'div': 3,
                    'h1': 1
                }
            },
            {
                'html': html3,
                'expected': {
                    'div': 8,
                    'h2': 2,
                    'h1': 1
                }
            }
        ]

        for test in tests:
            htmlContent = test['html']
            wps = WebPageScraper(htmlContent)
            output = wps.get_tags()
            passed = True
            for tag in test['expected']:
                if tag not in output or (tag in output and output[tag] != test['expected'][tag]):
                    passed = False
                    times = output[tag] if tag in output else 0
                    print(tag + ' was expected to be found exactly ' + str(
                        test['expected'][tag]) + ' times (was found ' + str(times) + ' times)')

            if passed == False:
                self.failures_counter += 1
