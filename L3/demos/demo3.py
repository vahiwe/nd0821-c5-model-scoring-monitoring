import ast
import numpy as np

newf1=0.38

with open('previousscores_l3demo.txt', 'r') as f:
    f1list = ast.literal_eval(f.read())

# Raw comparision test
firsttest = newf1<np.min(f1list)
print(firsttest)

# Parametric Outlier Test
secondtest = newf1<np.mean(f1list)-2*np.std(f1list)
print(secondtest)

# Non parametric Outlier Test
iqr = np.quantile(f1list,0.75)-np.quantile(f1list,0.25)
thirdtest = newf1<np.quantile(f1list,0.25)-iqr*1.5
print(thirdtest)