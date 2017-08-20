#pip install pypiwin32
import win32com.client as win32
#excel = win32.DispatchEx('Excel.Application') #uses new instance of excel
excel = win32.gencache.EnsureDispatch('Excel.Application') #uses current instance of excel

#create new workbook
wb_new = excel.Workbooks.Add()
path = 'F:/SecExcelDownloadXLS/test/SLG-1040971-000104746913001830.xls'
wb_new.SaveAs(r'F:/SecExcelDownloadXLS/test/SLG-1040971-000110465910043119(1).xlsx')
wb_old=excel.Workbooks.Open(r'F:/SecExcelDownloadXLS/test/SLG-1040971-000110465910043119.xls')

for sh in wb_old.Sheets:
    wb_old.Worksheets(sh.Name).Move(Before=wb_new.Worksheets("Sheet1"))

wb_new.Worksheets('Sheet1').Delete()
wb_new.Save()
#excel.Application.Quit()
del excel # ensure Excel process ends
