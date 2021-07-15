import timeit
import os

starttime = timeit.default_timer()

os.system('python3 addnumbers.py')

timing=timeit.default_timer() - starttime

print(timing)

final_output=[]

final_output.append(timing)
print(final_output)