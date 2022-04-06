import pandas as pd  # pip install pandas
import numpy as np

df = pd.read_excel(r'C:\Users\tsink\Downloads\1.xlsx', sheet_name='Лист1')


# for i in range(5):
#     print(f'{df.iloc[1:7, 1]}   {df.iloc[:, ]}')

print(df.iloc[2:, np.r_[1:8]])