import urllib
import time
from multiprocessing.dummy import Pool as ThreadPool


excelFolder = 'F://SecExcelDownload2/'
compListUrl = 'C://Users/l1111/Desktop/AlphaCapture/downloadFileUrl.txt'
successFile = excelFolder+'/success.txt'
failFile = excelFolder+'/fail.txt'
logFile = excelFolder+'/log.txt'

def downloadFile(line):
    compName = line.split(',')[0]
    cik = line.split(',')[1]
    doc = line.split(',')[2]
    url = line.split(',')[3]
    print(cik)
    print(doc)
    print(url)
    fileURLOpener = urllib.URLopener()
    try:
        fileURLOpener.retrieve(url,excelFolder+compName+'-'+cik+'-'+doc+'.xlsx' )
        with open(successFile, "a") as myfile:
            myfile.write(url+'\n')
    except:
        print('Error: not a xlsx file. Downloading xls file')
        try:
            fileURLOpener.retrieve(url.replace('.xlsx','.xls'), excelFolder+compName+'-'+cik+'-'+doc+'.xls')
            with open(successFile, "a") as myfile:
                myfile.write(url+'\n')
        except:
            print('Error: download failed')
            with open(failFile, "a") as myfile:
                myfile.write(url+'\n')

def slowSingleThread():
    lineList = []
    count = 0
    with open(compListUrl) as f:
        for line in f:
            line = line.strip()
            lineList.append(line)
            # downloadFile(line)
            # break
    # print(len(lineList))
    # total = len(lineList)
    # with open(compListUrl) as f:
    #     for line in f:
    #         line = line.strip()
    #         with open(logFile, "a") as myfile:
    #             myfile.write(str(count)+'/'+str(total)+':'+line+'\n')
    #         count+=1
    #         downloadFile(line)
    for line in lineList:
        downloadFile(line)


def fastMultiThread():
    lineList = []
    count = 0
    with open(compListUrl) as f:
        for line in f:
            line = line.strip()
            lineList.append(line)
    # make the Pool of workers
    pool = ThreadPool(20)
    # open the urls in their own threads
    # and return the results
    results = pool.map(downloadFile, lineList)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()

fastMultiThread()
# slowSingleThread()
