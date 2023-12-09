import numpy as np
import pandas as pd

# List of countries
Lj =["Australia","Pakistan","India","Sri Lanka","Ireland","Zimbabwe","Canada","Kenya","England","West Indies","Bangladesh","South Africa","New Zealand","Netherlands"]

# Empty list to store the sum of runs for each country
sum = []

# Read the batting data from a CSV file
x=pd.read_csv('C:/Users/rajja/OneDrive/Desktop/batting_data_2011.csv')


# Iterate through each country in the list
for i in Lj:
    # Filter the data for the current country
    z=x.loc[x['Country']==f'{i}']
    print(z)
    
    # Convert the "Runs" column to integer type
    z["Runs"] = z["Runs"].astype(int)

    # Calculate the sum of runs for the current country
    t = z['Runs'].sum()
    
    # Append the sum to the list
    sum.append(t)

# Create a DataFrame with the country and runs data
S = pd.DataFrame({"country":Lj,"runs":sum})

S.to_csv("Batting_data_2011.csv")
