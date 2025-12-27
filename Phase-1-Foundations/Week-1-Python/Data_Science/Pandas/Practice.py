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

# df['Name_length'] = df['Name'].apply(len)  # For inbuilt method
# print(df)

# def Grade(Marks): # For user defined function
#     if(Marks>=90):
#         return 'A++'
#     elif(Marks>=80 and Marks<90):
#         return 'A+'
#     elif(Marks>=70 and Marks<80):
#         return 'A'
#     elif(Marks>=60 and Marks<70):
#         return 'B'
#     else:
#         return 'C'
    
# df['Grade'] = df['Marks'].apply(Grade)
# print(df)

## To appply string function

# print(df['Name'].str.lower())  # Without creating new column
# df['Name_lower'] = df['Name'].str.lower() # By creating new function
# print(df)

## To remove a column

# df.drop(columns=['Gender','Age'],inplace=True)  # For single value just pass only one column name
# print(df)

## To check weater there is a null value in data

# print(df.isnull())  # It will return table of True/false (True->null)
# print(df.isnull().sum())  # It will return total number of null vaalue of each column
# print(df.info())      # It will return details of Null/Total/Not-Null/Datatypes values of each column

## To drop null value row

# df.dropna(inplace=True)
# df.dropna(subset=['Name','Age'],inplace=True)  # It will drop only that row in which has null value only in 'Name' column
# print(df)

## To fill null value

# df.fillna('Unknown',inplace=True) # For all colummn
# df['Name'].fillna('Unknown',inplace=True) # For specific colummn
# df['Marks'].fillna(df['Marks'].mean(),inplace=True) # It will fill average value of that column in null-value
# print(df)
# df.fillna(method='ffill',inplace=True)  # It will fill previous (upper) value to current value (after uppper value if null value)
# df["Marks"].ffill(inplace=True) # Another method
# print(df)

# df.fillna(method='bfill',inplace=True)  # It will fill next (lower) value to current value (befor lowe value if null value)
# df["Marks"].bfill(inplace=True) # Another method
# print(df)

## To remove duplicates

# df = {                                                 # Created new Dicitonary
#     'Name' : ['Rudra','Dhruv','Yug','Kunj','Kunj'],
#     'Age' : [19,16,17,13,13]
# }
# df = pd.DataFrame(df)       # Converted dictionary to dataframe
# print(df)

# df.drop_duplicates(inplace=True)   # It will remove duplicates and keep first value
# df.drop_duplicates(keep='last',inplace=True)   # It will remove duplicates and keep last value
# print(df)
# df.drop_duplicates(subset='Age',inplace=True) # It will remove duplicate based on column (for multiple column pass in list)
# print(df)

## To convert datatype in date & time (just date & time only)

df['AdmissionDate'] = pd.to_datetime(df['AdmissionDate']) # If date is not in yyyy-mm-dd format so use format method 
df['ExamDateTime'] = pd.to_datetime(df['ExamDateTime']) # If date is not in yyyy-mm-dd format so use format method 

## To perform operations on date

# df['Year'] = df['AdmissionDate'].dt.year             # It will return year
# df['Month'] = df['AdmissionDate'].dt.month           # It will return month
# df['Day'] = df['AdmissionDate'].dt.day               # It will return day
# df['Weekday'] = df['AdmissionDate'].dt.day_name()    # It will return name of week day (Monday/Friday/Sunday)
# print(df)
# print(df[df['AdmissionDate']>='2023-07-15'])         # It will return only rows which satisfies following condition
# df.sort_values('AdmissionDate',inplace=True)           # To sort data by dates  
# print(df)
# df['TermDays'] = (df['ExamDateTime'] - df['AdmissionDate']).dt.days   # It return days from admission date to exam date
# print(df)

## To perform aggregate operation

# print(df['Marks'].sum())       # It will return sum of column values
# print(df['Marks'].mean())      # It will return average of column values 
# print(df['Marks'].min())       # It will return minimum value of column
# print(df['Marks'].max())       # It will return maximum value of column
# print(df['Course'].count())     # It will return total number of values
# print(df['Course'].nunique())   # It will return total number of unique value
# print(df['Course'].unique())    # It will return all the unique values

## To perform aggregate function with groupby

# print(df.groupby('Course')['Marks'].mean())   # It wil return average values with groupby method for single column
# print(df.groupby('Course')['Marks'].min())   # It wil return minimum values with groupby method for single column
# print(df.groupby('Course')['Marks'].max())   # It wil return maximum values with groupby method for single column
# print(df.groupby(['Course','City'])['Marks'].mean())   # It wil return average values with groupby method for multiple column
# print(df.groupby(['Course','City'])['Marks'].min())   # It wil return minimum values with groupby method for multiple column
# print(df.groupby(['Course','City'])['Marks'].max())   # It wil return maximum values with groupby method for multiple column

## To perform more than one aggregate function in one line

# print(df.groupby(['Course','City'])['Marks'].agg(['min','max','mean'])) # It will return mutiple aggregate values 

## To perform aggregate function on multiple column with groupby

# print(df.groupby('Course').agg({'Marks' : 'mean', 'AdmissionDate': 'min'}))
# print(df['City'].value_counts()) # It will return numbers of unique values in particular column with total values
# print(df.groupby('City').agg({'City' : 'count','Marks' : 'mean'}))  # Another method

## To set column name instead of aggregate function name

# print(df.groupby('City').agg(
#     Minimum_marks = ('Marks','min'),
#     Maximum_marks = ('Marks','max'),
# ))

## To create pivot table

# print(pd.pivot_table(
#     df,
#     index = 'City',
#     columns = 'Course',
#     values = 'Marks',
#     aggfunc = 'mean',
#     fill_value = 0
# ))