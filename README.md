# sec_edgar_analysis


sec_edgar_analysis is a SEC EDGAR analysis system with tools to crawl and analyse the Excel files of 10Ks and 10Qs from each company.

The tool-kit contains:

  - Html spider of EDGAR document list page
  - Parser tool  for parsing html into downloadable urls
  - Downloader tool for downloading all the xlsx and xls files
  - Converting tool for transfering the unformatted old xls files into Pythong-readable xlsx files

## How to run the code

### Html spider:

Change file output and company list input directory in python_crawler/spiders/cikdoc_spider.py

In project root directory run
```sh
$ scrapy crawl cikdoc
```

### Parser tool:

Change file output and input directory in parser/parse.py

In project root directory run
```sh
$ python parser/parse.py
```

### Downloader tool:

Change file output and input directory in parser/download.py

In project root directory run
```sh
$ python downloader/download.py
```

### Converter tool:

Change file output and input directory in converter/xls2xlsx.py

Copy xls2xlsx.py to directory with xls files and run
```sh
$ python xls2xlsx.py
```
or change directories in xls2xlsx.py and run
```sh
$ python converter/xls2xlsx.py
```
