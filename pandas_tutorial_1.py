import pandas as pd

df = pd.read_csv(r"C:\Users\bowie\OneDrive\Masaüstü\countries of the world.csv")
df2 = pd.read_table(r"C:\Users\bowie\OneDrive\Masaüstü\countries of the world.txt", sep = "\t")
df3 = pd.read_json(r"C:\Users\bowie\OneDrive\Masaüstü\json_sample.json")
df4 = pd.read_excel(r"C:\Users\bowie\OneDrive\Masaüstü\world_population_excel_workbook.xlsx", sheet_name = "Sheet", engine = 'openpyxl')

pd.set_option("display.max.rows",235)

##df4.info()

##Size of sheet
##print(df4.shape)

##First 10 row
##print(df4.head)

##Last 10 row
##print(df4.tail)

print(df4.loc[222])
print(" ")
print(df4.iloc[222])


