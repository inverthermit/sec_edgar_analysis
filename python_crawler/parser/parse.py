from os import listdir
from os.path import isfile, join
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import urlparse

downloadPath = 'C:/Users/l1111/Desktop/AlphaCapture/DownloadHtmls/'
fileUrlPath = 'C:/Users/l1111/Desktop/AlphaCapture/downloadFileUrl.txt'
onlyfiles = [f for f in listdir(downloadPath) if isfile(join(downloadPath, f))]
count = 0
for htmlFile in onlyfiles:
    compName = htmlFile.replace('.html','')
    count+=1
    print(count,':',compName)
    with open(downloadPath+htmlFile, 'r') as myfile:
        data=myfile.read() # .replace('\n', '')
        # cikSelector = Selector(text=data).xpath('//*[@id="contentDiv"]/div[1]/div[3]/span/a') #.extract()
        # for link in cikSelector.css('a *::text'):
        #     cik = link.extract().replace(' (see all company filings)','')
        #     print(compName+'-'+cik)

        # //*[@id="seriesDiv"]/table/tbody/tr[2]/td[3]/text()[2]
        docSelector = Selector(text=data).xpath("//a[@id='interactiveDataBtn']/@href").extract()
        for element in docSelector:
            par = urlparse.parse_qs(urlparse.urlparse(element).query)
            doc = par['accession_number'][0].replace('-','')
            cik = par['cik'][0]
            # print(par['accession_number'][0].replace('-',''))
            # print(par['cik'][0])
            strDownload = (compName+','+cik+','+doc+',https://www.sec.gov/Archives/edgar/data/'+cik+'/'+doc+'/Financial_Report.xlsx\n')
            with open(fileUrlPath, "a") as myfile:
                myfile.write(strDownload)

        # count +=1
        # if(count == 2):
        #     break
        # for link in docSelector.css('a *::text'):
        #     cik = link.extract().replace(' (see all company filings)','')
        #     print(compName+'-'+cik)
        # break;
