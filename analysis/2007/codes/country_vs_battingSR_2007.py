import pandas as pd

    # List of countries
L=['Australia', 'Pakistan', 'England' ,'Kenya' ,'India', 'Scotland', 'Bangladesh', 'West Indies' ,'New Zealand', 'Zimbabwe']
    # Empty list to store the sum of Runs for each country
sum = []

    # Read the batting data from a CSV file
x=pd.read_csv('2007/batting_data_2007.csv')

    # Iterating through each country in the list
for i in L:
        # Filtering the data for the current country
    z=x.loc[x['Country']==f'{i}']
    # Remove players having SR==0
x=x.loc[x['SR']!=0]

    # Sorting data in ascending values of SR
x=x.sort_values(by="SR", ascending=False)

    #storing dataframe with only these columns in y
y=x[["player","Country","Runs","HS","Avg","SR"]]

    #resetting index
y.index = range(0,len(y))

    #storing this new dataframe in new csv file
y.to_csv("country_vs_battingSR_2007.csv")