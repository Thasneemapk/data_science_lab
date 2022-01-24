import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
iris=pd.read_csv("iris_csv.csv")
plt.figure(figsize=(10,3))
x=iris["sepallength"]
plt.hist(x,bins=30,color="green")
plt.xlabel("sepallength in cm")
plt.ylabel("count")
plt.show
