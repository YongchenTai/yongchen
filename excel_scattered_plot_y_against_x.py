import matplotlib.pyplot as plt 
import xlrd

loc = ("1.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
x=[]
for i in range(sheet.nrows): 
    x=sheet.cell_value(i, 0)
    for j in range(30,40):
        yj=sheet.cell_value(i, j)
        plt.scatter(x, yj,s=1,color="k")

plt.show()