import pandas as pd

intArray = pd.array([1, 2, 3, 4, 5])
print(intArray)
print("\n")
print(type(intArray))

ts3 = pd.Timestamp(year=2025, month=3, day=31, hour=23, minute=59, second=59)

print(ts3.is_month_end)


