
import pandas as pd

    # List of countries
Lj =["Australia","Pakistan","India","Sri Lanka","Ireland","Zimbabwe","Canada","Kenya","England","West Indies","Bangladesh","South Africa","New Zealand","Netherlands"]

    # Empty list to store the sum of Runs for each country
sum = []

    # Read the batting data from a CSV file
x=pd.read_csv('C:/Users/rajja/OneDrive/Desktop/batting_data_2011.csv')

    # Iterating through each country in the list
for i in Lj:
        # Filtering the data for the current country
    z=x.loc[x['Country']==f'{i}']
    print(z)

    # Remove players having SR==0
x=x.loc[x['SR']!=0]

    # Sorting data in ascending values of SR
x=x.sort_values(by="SR", ascending=False)

    #storing dataframe with only these columns in y
y=x[["player","Country","Runs","HS","Avg","SR"]]

    #resetting index
y.index = range(0,len(y))

    #storing this new dataframe in new csv file
y.to_csv("country_vs_battingSR_2011.csv")

