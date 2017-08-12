import urllib
import time
from multiprocessing.dummy import Pool as ThreadPool


excelFolder = 'F://SecExcelDownload/'
compListUrl = 'C://Users/l1111/Desktop/AlphaCapture/downloadFileUrl.txt'

def downloadFile(line):
    compName = line.split(',')[0]
    cik = line.split(',')[1]
    doc = line.split(',')[2]
    url = line.split(',')[3]
    fileURLOpener = urllib.URLopener()
    try:
        testfile.retrieve(url,excelFolder+compName+'-'+cik+'-'+doc+'.xlsx' )
        with open(excelFolder+'/success.txt', "a") as myfile:
            myfile.write(url+'\n')
    except:
        print('Error: not a xlsx file. Downloading xls file')
        try:
            testfile.retrieve(url.replace('.xlsx','.xls'), excelFolder+compName+'-'+cik+'-'+doc+'.xls')
            with open(excelFolder+'/success.txt', "a") as myfile:
                myfile.write(url+'\n')
        except:
            print('Error: download failed')
            with open(excelFolder+'/fail.txt', "a") as myfile:
                myfile.write(url+'\n')


testfile = urllib.URLopener()
# testfile.retrieve("https://www.sec.gov/Archives/edgar/data/50104/000005010417000189/Financial_Report.xls", "Financial_Report.xls")

# try:
#     testfile.retrieve("https://www.sec.gov/Archives/edgar/data/50104/000005010417000189/Financial_Report.xls", "a.xls")
# except:
#     print('Error: not a xls file. Downloading xlsx file')
#     testfile.retrieve("https://www.sec.gov/Archives/edgar/data/50104/000005010417000189/Financial_Report.xlsx", "b.xlsx")
lineList = []
count = 0
with open(compListUrl) as f:
    for line in f:
        line = line.strip()
        lineList.append(line)
        # downloadFile(line)
        # break
print(len(lineList))
total = len(lineList)
with open(compListUrl) as f:
    for line in f:
        line = line.strip()
        lineList.append(line)
        with open(excelFolder+'/log.txt', "a") as myfile:
            myfile.write(str(count)+'/'+str(total)+':'+line+'\n')
        count+=1
        downloadFile(line)
#         downloadFile(line)
# # make the Pool of workers
# pool = ThreadPool(4)
# # open the urls in their own threads
# # and return the results
# results = pool.map(downloadFile, lineList)
#
# # close the pool and wait for the work to finish
# pool.close()
# pool.join()
