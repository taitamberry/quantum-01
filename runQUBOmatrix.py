import numpy as np
import dimod
import pandas as pd
from dwave.system import EmbeddingComposite, DWaveSampler

print("step1: loading matrix Q")

f = open("code/Q_excel.csv")
Q = np.loadtxt(f,delimiter = ",")
bqm = dimod.BinaryQuadraticModel.from_numpy_matrix(Q, variable_order=None, offset=0.0, interactions=None)

print("step2: create and run sampler")
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads = 1000)

#print("step3: results")
#print(sampleset)

print("step4: saving results")
df_results = SampleSet.to_pandas_dataframe()
writer = pd.ExcelWriter('output.xlsx')
df_results.to_excel(writer)
writer.save()