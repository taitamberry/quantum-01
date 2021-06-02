import numpy as np
import dimod
import pandas as pd
import neal
from dwave.system import EmbeddingComposite, DWaveSampler

print("step1: loading matrix Q")
f = open("code/Q_excel.csv")
Q = np.loadtxt(f,delimiter = ",")
#dummy matrix for testing
#Q = np.matrix([[-31,0,0,0,0],[21,-29,0,0,0],[18,18,-32,0,0],[21,21,21,-29,0],[18,18,21,18,-32]])

bqm = dimod.BinaryQuadraticModel.from_numpy_matrix(Q, variable_order=None, offset=0.0, interactions=None)

#print("step2a: create quantum sampler")
#sampler = EmbeddingComposite(DWaveSampler())
print("step2b: create simulated annealing sampler")
sampler = neal.SimulatedAnnealingSampler()

print("step3: run sampler")
sampleset = sampler.sample(bqm, chain_strength=1000, num_reads = 10)

#print("step4: display results")
#print(sampleset)

print("step5: saving results to csv file")
df_results = sampleset.to_pandas_dataframe()
filepath = 'results.csv'
df_results.to_csv(filepath, index = False)