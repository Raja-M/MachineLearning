import pandas as pd
import matplotlib.pyplot as plt

intArray = pd.array([1, 2, 3, 4, 5])
print(intArray)
print("\n")
print(type(intArray))

ts3 = pd.Timestamp(year=2025, month=3, day=31, hour=23, minute=59, second=59)

print(ts3.is_month_end)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)


a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])
print(myvar)
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(myvar)
print(df.loc[0])
print(df.loc[[0, 1]])
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])#named index
print(df) 
print(df.loc["day2"])

df = pd.read_csv('data.csv')
print(df)#print 5 records only
print(df.to_string()) #print entire df
print(df.head(10))
print(df.tail()) 
print(pd.options.display.max_rows) 
print(df.info()) 

new_df = df.dropna()
df.fillna(130, inplace = True)
df.fillna({"Calories": 130}, inplace=True)

x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].median()
df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].mode()[0]
df.fillna({"Calories": x}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df)

print(df.duplicated())
df.drop_duplicates(inplace = True)

df.corr()

df.plot()
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

df = pd.read_json('data.json')
print(df.to_string()) 