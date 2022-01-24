import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("iris_csv.csv")
plt.figure(figsize=(10,3))
data.boxplot()

