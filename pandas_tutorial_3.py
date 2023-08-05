import pandas as pd

df1 = pd.read_csv(r"C:\Users\bowie\OneDrive\Masaüstü\LOTR.csv")
df2 = pd.read_csv(r"C:\Users\bowie\OneDrive\Masaüstü\LOTR 2.csv")

test = df1.merge(df2, "inner", on = ["FellowshipID","FirstName"])

test = df1.merge(df2, "outer")

test = df1.merge(df2, "left")

test = df1.merge(df2, "right")

test = df1.merge(df2, "cross")

test = df1.join(df2, how = "outer", on = "FellowshipID", lsuffix = "_Left", rsuffix = "_Right")

df3 = df1.set_index("FellowshipID").join(df2.set_index("FellowshipID"), lsuffix = "_Left", rsuffix = "_Right", how = "outer")
test = df3

test = pd.concat([df1,df2], join = "outer", axis = 1)

print(test)

