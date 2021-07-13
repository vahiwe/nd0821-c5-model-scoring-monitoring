import os
import pandas as pd

directories = ["/data1/", "/data2/", "/data3/"]
final_dataframe = pd.DataFrame(columns=["col1", "col2", "col3"])

for directory in directories:
    filenames = os.listdir(os.getcwd() + directory)
    for each_filename in filenames:
        currentdf = pd.read_csv(os.getcwd() + directory + each_filename)
        final_dataframe = final_dataframe.append(currentdf).reset_index(drop=True)

# Deduplicate the data
final_dataframe = final_dataframe.drop_duplicates()

final_dataframe.to_csv("result.csv", index=False)