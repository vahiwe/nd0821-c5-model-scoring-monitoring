import os
import pandas as pd

directories = ["/udacity1/", "/udacity2/"]
final_dataframe = pd.DataFrame(columns=["peratio", "price"])

for directory in directories:
    filenames = os.listdir(os.getcwd() + directory)
    for each_filename in filenames:
        currentdf = pd.read_csv(os.getcwd() + directory + each_filename)
        final_dataframe = final_dataframe.append(currentdf).reset_index(drop=True)

final_dataframe.to_csv("demo_20210713.csv", index=False)