import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vgsales.csv')
print(df.info())

# a.The Year and Publisher columns contain a few missing values. Treat them accordingly.
df.drop(df[df.Year.isnull()].index, inplace = True) 
df.drop(df[df.Publisher.isnull()].index, inplace = True)

print(df.info())

# b.Convert the values contained in the Year column into integer values.
df['Year'] = df['Year'].astype(int)
print(df.info())

# c. Find the trend in growth in the number of total units sold across the given regions and the world. 
# Also, create year-wise line plots for the total number of units sold across different regions and the world.

sales_by_year = df.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()


plt.figure(figsize=(10,6))


plt.plot(sales_by_year.index, sales_by_year['NA_Sales'], label='North America')
plt.plot(sales_by_year.index, sales_by_year['EU_Sales'], label='Europe')
plt.plot(sales_by_year.index, sales_by_year['JP_Sales'], label='Japan')
plt.plot(sales_by_year.index, sales_by_year['Other_Sales'], label='Other Regions')
plt.plot(sales_by_year.index, sales_by_year['Global_Sales'], label='Global Sales')

plt.title('Trend of Video Game Sales by Region and Globally (in Millions)')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Units Sold (Millions)')
plt.legend()
plt.grid(True)

plt.show()


# d. In which year, the most number of games were sold globally and how many?
sales_by_year = df.groupby('Year')['Global_Sales'].sum()
highest_sales_year = sales_by_year.sort_values(ascending = False).head(1)
print("The year in which most number of games sold globally: ", highest_sales_year)

# e. Which region among North America, Europe and Japan had the highest sales in 2005?
data_2005 = df[df['Year'] == 2005]

na_sales_2005 = data_2005['NA_Sales'].sum()
eu_sales_2005 = data_2005['EU_Sales'].sum()
jp_sales_2005 = data_2005['JP_Sales'].sum()

if na_sales_2005 > eu_sales_2005 and na_sales_2005 > jp_sales_2005:
    highest_region = "North America"
    highest_sales = na_sales_2005
elif eu_sales_2005 > na_sales_2005 and eu_sales_2005 > jp_sales_2005:
    highest_region = "Europe"
    highest_sales = eu_sales_2005
else:
    highest_region = "Japan"
    highest_sales = jp_sales_2005

#FINAL RESULT
print(f"The region with the highest sales in 2005 is:", highest_region)
print("Highest sales in this region is :", highest_sales )