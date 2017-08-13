# import openpyxl
import xlrd
from xlrd import open_workbook
import shutil, os
from os import listdir
from os.path import isfile, join
import pandas as pd


excelFolder = 'F://SecExcelDownload/'
onlyfiles = [f for f in listdir(excelFolder) if isfile(join(excelFolder, f))]
count = 0
for excelFile in onlyfiles:
    # xlsx file and xls file

    # if('.xlsx' in excelFile):
    #     # Use openpyxl
    #     fileName = excelFile.replace('.xlsx','')
    #     fileName = fileName.replace('.xls','')
    #     wb = openpyxl.load_workbook(excelFolder+excelFile)
    #     docInfoSheetName = wb.get_sheet_names()[0]
    #     docInfoSheet = wb.get_sheet_by_name(docInfoSheetName)
    #     for i in range(0,21):
    #         print(i, docInfoSheet.cell(row=1, column=i).value)
    #     break
    # else:
    #     # Use xlrd


    # try Panda

    xls = pd.ExcelFile(excelFolder+excelFile)

    sheetX = xls.parse(0) #2 is the sheet number

    var1 = sheetX['Statement Of Income (USD $)']

    print(var1[1])
    break


    # # just use xlrd
    # fileName = excelFile.replace('.xlsx','')
    # fileName = fileName.replace('.xls','')
    # wb = xlrd.open_workbook(excelFolder+excelFile, on_demand=True)
    # docInfoSheet = wb.sheet_by_index(0)
    # # wb = openpyxl.load_workbook(excelFolder+excelFile)
    # # docInfoSheetName = wb.get_sheet_names()[0]
    # # docInfoSheet = wb.get_sheet_by_name(docInfoSheetName)
    # for i in range(0,30):
    #     print(i, docInfoSheet.cell(i, 0).value)
    # break
    # Rename
    # shutil.move('C:\\bacon.txt', 'C:\\eggs')




    # if 'Document Type' in value:
    #     docType = value
    # else if 'Document Fiscal Year Focus' in value:
    #     year = value
    # else if 'Document Fiscal Period Focus' in value:
    #     quarter = value
