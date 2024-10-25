import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Restaurant.csv")
print(df.info())


counts = df["day"].value_counts()
print(counts)


labels = counts.index  
sizes = counts.values  



plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Percentage of Customers Visiting the Restaurant on Different Days')
plt.show()


data= df[(df["tip"]<5) & (df["time"]=="Dinner")]
print(data)


max_party_size = df['size'].max()

max_party_day = df[df['size'] == max_party_size]


print("Maximum party size:", max_party_size)
print(max_party_day[['day', 'size']])

