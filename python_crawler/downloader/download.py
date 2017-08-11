import urllib

testfile = urllib.URLopener()
# testfile.retrieve("https://www.sec.gov/Archives/edgar/data/50104/000005010417000189/Financial_Report.xls", "Financial_Report.xls")

try:
    testfile.retrieve("https://www.sec.gov/Archives/edgar/data/50104/000005010417000189/Financial_Report.xls", "Financial_Report.xls")
except:
    print('Error: not a xls file. Downloading xlsx file')
    testfile.retrieve("https://www.sec.gov/Archives/edgar/data/50104/000005010417000189/Financial_Report.xlsx", "Financial_Report.xlsx")
