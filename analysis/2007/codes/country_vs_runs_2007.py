import numpy as np
import pandas as pd

# List of countries
L=['Australia', 'Pakistan', 'England' ,'Kenya' ,'India', 'Scotland', 'Bangladesh', 'West Indies' ,'New Zealand', 'Zimbabwe']
# Empty list to store the sum of runs for each country
sum = []

# Read the batting data from a CSV file
x=pd.read_csv('2007/batting_data_2007.csv')

# Iterate through each country in the list
for i in L:
    # Filter the data for the current country
    z=x.loc[x['Country']==f'{i}']
    
    # Replace '-' with np.nan and convert the "Runs" column to float
    z["Runs"] = z["Runs"].replace('-', np.nan).astype(float)

    # Calculate the sum of runs for the current country
    t = z['Runs'].sum()
    
    # Append the sum to the list
    sum.append(t)

# Create a DataFrame with the country and runs data
df = pd.DataFrame({"country":L,"runs":sum})

df.to_csv("country_vs_runs_2007.csv")
