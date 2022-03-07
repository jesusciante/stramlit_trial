import pandas as pd  # pip install pandas openpyxl

df = pd.read_excel("SteelFab.xlsx", header=0,sheet_name="Sheet1")

df2 = df[df['MARK NUMBER'] == "P.2P1.DA-124/1"]
print(df2)