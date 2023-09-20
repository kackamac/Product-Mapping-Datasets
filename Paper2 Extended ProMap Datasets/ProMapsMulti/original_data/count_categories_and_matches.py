import pandas as pd
import numpy as np
data = pd.read_csv('ag-train.csv')
dataa = pd.read_csv('ag-valid.csv')

data = pd.concat([data, dataa])

