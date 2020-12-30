import numpy as np
import dimod

print("starting app 1")
f = open("code/Q_excel.csv")
print("starting app 2")
Q = np.loadtxt(f,delimiter = ",")
print("starting app 3")
bqm = dimod.BinaryQuadraticModel.from_numpy_matrix(Q)
print("starting app 4")
print(Q)

