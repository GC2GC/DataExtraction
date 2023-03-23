#Written by Gawain Coughlan. Enjoy :)

import pandas as pd

df = pd.read_csv("dataForTest.csv") 


maxnum = df[(df["price"] >25)]

sorted_df = df.sort_values(by=["price"], ascending=True)

print(sorted_df.head(15))




#searching and storing a text value in a variable
containsText = df.ip_address.str.contains("161.236.76.128")
print(containsText.to_string())
fraud = df.iloc[561].ip_address

#searching for numeric value in any specified column
containsNum = df[(df["price"] == 33)]

#searching for null values
nullValues = df.gender.isnull()
print(nullValues)


bryna = df.iloc[709].first_name
print(bryna)

print(fraud)

print(containsNum)

#head for top 5

#USE .to_string() for getting rid of the truncation in terminal

#tail() for bottom 5, can specify more if needed in brackets


