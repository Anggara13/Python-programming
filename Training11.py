# Introduction to Pandas
# Pandas (Python for Data Analysis) helps in computing with spreadsheet or tabular data.
# 
# Pandas = Numpy + Relational Database such as SQL.
# 
# There are 2 types of objects in Pandas: 1. Series (1-dimensional) 2. DataFrame (n-dimensional)

import pandas as pd

#1. Series: Consists of index (0-2) and values
obj=pd.Series([2,3,4],index=[x for x in range(1,4)]) 
obj # index (0-2) and values (1-3). Can be done slice, assign etc

print(obj.index)
print(obj.values)

# Series also can be calculated with other series
obj2=pd.Series([4,5,6], index=[1,2,3])
obj+obj2 
# If the index names are not the same it will result in NaN (Not a Number)/NA Not Available

#2. Dataframe for storing Transaction data per product
data = {
    "roti":[3,2,0,1],
    "cola":[0,3,7,2],
    "tisu":[5,1,1,8],
}
transaction = pd.DataFrame(data)
transaction

# Add additional index to dataframe
customer = ['Zakka','Adit','Yoga','Asep']
transaction = pd.DataFrame(data, index=customer)
transaction

transaction.columns

# SLICING in pandas based on index name
# Take values only in Zakka's transaction
transaction.loc["Zakka"] # It's also possible to use transaction.loc[["Zakka","Yoga"]]

# SLICING in pandas based on index order
# Take values based on index order
transaction.iloc[2]
# It's also possible to take transaction.iloc[[0,2]]
# It's also possible to take transaction.iloc[0:2]

# Slicing in pandas based on columns
transaction["roti"]

# Operations inside Pandas
print(transaction.mean(), end='\n \n')
print(transaction.std(), end='\n \n')
print(transaction.sum(), end='\n \n')
print(transaction.describe(), end='\n \n') #Complete