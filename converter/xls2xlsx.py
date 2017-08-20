import os
import win32com.client as win32
# only work in windows
path = os.getcwd()
successFile = "./success.txt"
failFile = "./fail.txt"
excel = win32.gencache.EnsureDispatch('Excel.Application')
for fname in os.listdir():
	# print((fname+'x') in os.listdir())
	if (fname[-3:] =='xls' and (fname+'x') not in os.listdir()):
		try:
			wb = excel.Workbooks.Open(os.path.join(path, fname))
			wb.SaveAs(os.path.join(path, fname)+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
			wb.Close()
			print(fname+"x √")
			with open(successFile,"a") as myfile:
				myfile.write(fname+'\n')
		except:
			print(fname+"x X")
			with open(failFile,"a") as myfile:
				myfile.write(fname+'\n')
excel.Application.Quit()
