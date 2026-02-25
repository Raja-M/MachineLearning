
import pandas as pd

file_path = r'C:\projects\git\data\userdata.csv'

x = pd.read_csv( file_path , header=0).values 
print(x)

