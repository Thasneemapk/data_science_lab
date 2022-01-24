import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
iris=pd.read_csv("iris_csv.csv")
iris.plot(kind="scatter",x="sepallength",y="petallength")
plt.grid()
plt.show()
