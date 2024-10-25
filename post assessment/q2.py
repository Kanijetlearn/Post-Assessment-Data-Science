import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("LifeExpectancy.csv")
print(df.info())
print(len(df.columns))

# a. Rename some columns if they contain leading and trailing spaces (by removing spaces).

df.columns = df.columns.str.strip()

print(df.columns)


# b. Which columns in the dataset have missing values and how many?
missing_values = df.isnull().sum()
print(missing_values)





# c. Drop all the columns from the DataFrame containing more than 15% percent of the missing values.
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)
columns_to_drop = missing_percentage[missing_percentage > 15].index
print(columns_to_drop)
df_cleaned = df.drop(columns=columns_to_drop)
print(df_cleaned)



# # Replace the missing values in the remaining columns with the median
 
numeric_columns = df_cleaned.select_dtypes(include=['int64','float64'])
df_cleaned[numeric_columns.columns] = numeric_columns.fillna(numeric_columns.median())
print(df_cleaned.isnull().sum())


