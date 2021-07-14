import ast
import numpy as np

newr2=0.3625

with open('previousscores.txt', 'r') as f:
    f1list = ast.literal_eval(f.read())

# Raw comparision test
firsttest = newr2<np.min(f1list)
print(firsttest)

# Parametric Outlier Test
secondtest = newr2<np.mean(f1list)-2*np.std(f1list)
print(secondtest)

# Non parametric Outlier Test
iqr = np.quantile(f1list,0.75)-np.quantile(f1list,0.25)
thirdtest = newr2<np.quantile(f1list,0.25)-iqr*1.5
print(thirdtest)
