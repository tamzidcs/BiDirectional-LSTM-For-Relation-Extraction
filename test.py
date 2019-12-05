import numpy as np
import matplotlib.pyplot as plt

with open("curves/contextweighted_curve.dat") as f:
	data = f.read()
print(data)
data = data.split('\n')
data = data[:-1]
print(data)
x = [row.split('\t')[0] for row in data]
y = [row.split('\t')[1] for row in data]



plt.figure(figsize=(20,10))
plt.plot(x,y)
plt.xticks([])
plt.yticks([])

plt.show()
