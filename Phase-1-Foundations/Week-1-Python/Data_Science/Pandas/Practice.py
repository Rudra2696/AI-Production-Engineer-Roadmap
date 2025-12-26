from email import header
import pandas as pd

# # To read CSV file 

df = pd.read_csv('Student.csv')
# print(df)

# # To read particular rows data from top & Bottom

# print(df.head(6)) # From Top
# print(df.tail(6)) # From Bottom

# # If you do not pass numbers of rows so it will take 5 by default

# To get data type & Information & Description & Shape about data

# print(df.dtypes)      # Returns Datatype
# print(df.info())      # Returns Information
# print(df.describe())  # Retuen the statics of data (integer & float only)
# print(df.shape)       # Returns the shpae of data

# # To get columns list & Change column name

# print(df.columns)        # Return list of column
# df.columns = ['StudentID', 'Full_Name', 'Age', 'Gender', 'Curriculum', 'Marks', 'City']  # Just copy column list and change name 
# df.rename(columns={'Name' : 'Full_Name', 'Course' : 'Curriculum'}, inplace=True)         # Using rename function
# print(df)

# # To remove header

# df1 = pd.read_csv('Student.csv',header = None)  # This will remove header and assisgn indexes as header
# print(df1)

# # To get particular columns

# col = ['StudentID','Age','Marks'] 
# print(df[col])
# print(df[['StudentID','Age','Marks']])  # Another method
# print(df['Name'])  # For only one column
# print(df.Name)       # Another method

# # To create dataframe from another data

# # df2 = df[['Name','Age']]
# df2 = df['Name']     # For one column
# df2 = df.Name        # Another method
# print(df2,type(df2))

# # To get specific row & column

# print(df.iloc[3:7]) # End index will not include row only
# print(df.iloc[3:7:2]) # End index will not include with step value row only (iloc --> index locatio
# print(df.iloc[1:5,2:5]) # Particular rows & column
# print(df.iloc[1:5:2,2:5:2]) # Particular rows & column with step value
# print(df.loc[2:5:2,['Course','Gender','Age']]) # Using loc function & this will include ending index

## To set column as a index

# print(df.set_index('Name'))
# df.set_index('StudentID',inplace = True) # It will commit changes in dataframe by inplace function
# print(df)
# print(df.loc['Arjun'])  # After setting column as a index you can also access particular row by element of that column 
# print(df.loc['Arjun','Age':"City"])  # To get limited columns 

## We can not get data by name of column using iloc

## To rseset index

# df.reset_index(inplace=True) # If you set column as index so using this function you can reset index
# print(df)

## To sort data in ascending & descending order based on  index

# df.sort_index(inplace=True)   # For ascending
# df.sort_index(ascending=False,inplace=True) # For descending
# df.sort_values(by='Marks',ascending=False,inplace=True) # This will sort by column
# df.sort_values(by=['Marks','Age'],ascending=[False,True],inplace=True) # This will sort by first column if there is same so then column2
# print(df)

## To filter data (select particular data from specific row)

# fn = df['Marks']>=91      # For all columns
# fn1 = (df['Marks']>=91) &  (df['Age']>=20) # For more than one condition (same for 'OR'use '|' and also for 'NOT' just use '~')
# print(df.loc[fn1])        # With 'loc' method
# print(df[(df['Marks']>=91) &  (df['Age']>=20)])   # Without 'loc' method

# # To add new column and add value in that column or drop column 

# df['State']='Gujarat'    # It can modify existing column of all values of that column
# df.drop(columns='State',inplace=True)   # If you want to drop more than one columnn so just passs a list of column
# print(df)

## To modify particular value of column

# df.loc[df["Marks"] > 90, "Grade"] = 'A++'  # For single condition
# df.loc[(df["Marks"] > 80) & (df["Marks"] <= 90), "Grade"] = 'A+'  # For multiple condition
# print(df)

# ## To apply function on particular column

# df['Name_length'] = df['Name'].apply(len)
# print(df)