import scrapy
def read():
    result = []
    compListUrl = 'C:\Users\l1111\Desktop\AlphaCapture/sp500list.txt'
    searchUrl = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=10&dateb=&owner=exclude&count=100&CIK='
    with open(compListUrl) as f:
        for line in f:
            line = line.strip()
            result.append(searchUrl+line)
    return result
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # download_delay = 2
    def start_requests(self):
        urls = read()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = 'C:\Users\l1111\Desktop\AlphaCapture/DownloadHtmls/%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
