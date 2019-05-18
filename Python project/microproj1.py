import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

matrix = np.mat([[-3,3],[5,-5]])
prec = 0.01

exp = [expm(matrix * i * prec) for i in range(100)]
valx = [i * prec for i in range(100)]

val1, val2, val3, val4 = [], [], [], []
for mat in exp:
    val1.append(mat[0][0])
    val2.append(mat[0][1])
    val3.append(mat[1][0])
    val4.append(mat[1][1])
    
#Create the graph
plt.plot(valx, val1, linewidth = 1, color = 'blue')
plt.plot(valx, val2, linewidth = 1, color = 'blue')
plt.plot(valx, val3, linewidth = 1, color = 'red')
plt.plot(valx, val4, linewidth = 1, color = 'red')

#Resize the figure
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 15
fig_size[1] = 5

#Add the title and the axis caption
plt.title('Exponential of a matrix')
plt.ylabel('Y value')
plt.xlabel('X value')

#Add the grid
plt.grid(True)

plt.savefig("Pplots.pdf")
plt.savefig("Pplots.png")