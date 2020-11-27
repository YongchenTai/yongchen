import matplotlib.pyplot as plt 
import xlrd
import numpy as np


loc = ("2.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
x=sheet.row_values(0)
for i in range (30,35):
    yi=sheet.row_values(i)
    yy=np.array(yi)
    ymax=max(yi)
    yn=yy/ymax
    plt.scatter(x, yn,s=1,color="k")
plt.show()
