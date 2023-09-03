'''get all the csv files in the "data" folder and combine into one excel workbook'''


import pandas as pd

import glob

csv_files = glob.glob("data/*.csv")

combined_data = pd.DataFrame()

for csv_file in csv_files:
    data = pd.read_csv(csv_file)
    combined_data = combined_data.append(data)

#combined_data.to_excel("data/cobined.xlsx", index=False)

count = combined_data['TagNO'].value_counts()

print(count)