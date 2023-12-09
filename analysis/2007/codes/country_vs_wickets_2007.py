import pandas as pd
import numpy as np

    # List of countries
L=['Australia', 'Pakistan', 'England' ,'Kenya' ,'India', 'Scotland', 'Bangladesh', 'West Indies' ,'New Zealand', 'Zimbabwe']

    # Empty list to store the sum of Wickets for each country
sum = []

    # Read the bowling data from a CSV file
x=pd.read_csv('2007/bowling_data_2007.csv')

    # Iterate through each country in the list
for i in L:
        # Filter the data for the current country
    z=x.loc[x['Country']==f'{i}']
    
    
        # Convert the "Wickets" column to integer type
    z["Wickets"] = z["Wickets"].replace('-', np.nan).astype(float)

        # Calculate the sum of Wickets for the current country
    t = z['Wickets'].sum()
    
        # Append the sum to the list
    sum.append(t)

    # Create a DataFrame with the country and Wickets data
df = pd.DataFrame({"country":L,"Wickets":sum})

df.to_csv("country_vs_wickets_2007.csv")