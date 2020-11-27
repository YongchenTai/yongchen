import matplotlib.pyplot as plt 
import xlrd
import numpy as np
from numpy import *
loc = ("3.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
x=sheet.row_values(0)
for i in range (1,sheet.nrows):
    for j in range(0, 31):
        yb=sheet.cell_value(i,j)
        ybb=mean(yb)
        yi=sheet.row_values(i)-ybb
        yy=np.array(yi)
        ymax=max(yi)
        yn=yy/ymax
        plt.plot(x, yn,color="lightgrey", alpha=0.005,zorder=1)
for k in range(0,31):
    ybm=sheet.cell_value(62,k)
    ybbm=mean(ybm)
    yim=sheet.row_values(62)-ybbm
    yym=np.array(yim)
    ymaxm=max(yim)
    ynm=yym/ymaxm
    plt.scatter(x,ynm,s=3,color="chocolate", alpha=1,zorder=2)
plt.xlabel('Time')
plt.ylabel('Binding')
plt.axis([0, 90, 0, 1])
plt.show()
