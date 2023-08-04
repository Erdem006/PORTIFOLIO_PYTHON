import pandas as pd

df = pd.read_csv(r"C:\Users\bowie\OneDrive\Masaüstü\world_population.csv")

##print(df[df['Rank'] <= 10])

specific_countries = ["Bangladesh","Brazil"]
##print(df[df["Country"].isin(specific_countries)])

##print(df[df["Country"].str.contains("United")])

df2 = df.set_index("Country")
##print(df2)

##print(df2.filter(items = ["Continent","Rank"]))

##print(df2.loc["United States"])

##print(df2.iloc[66])

print(df[df['Rank'] <= 10].sort_values(by = "Rank"))


