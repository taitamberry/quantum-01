import numpy as np
import dimod

f = open("Q_excel.csv")
Q = np.loadtxt(f,delimiter = ",")

bqm = dimod.BinaryQuadraticModel.from_numpy_matrix(Q)
