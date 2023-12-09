import numpy as np
import pandas as pd

# List of countries
L =["Australia","Pakistan","India","Sri Lanka","England","Afghanistan","Bangladesh","South Africa","New Zealand","West Indies",]

# Empty list to store the sum of runs for each country
sum = []

# Read the batting data from a CSV file
x=pd.read_csv('batting_data_2019.csv')

# Iterate over each country in the list
for i in L:
    # Filter the data for the current country
    z=x.loc[x['Country']==f'{i}']
    
    # Print the player, runs, and country for the current country
#    print(z[['player','Runs','Country']])
    
    # Convert the runs column to integer type
    z["Runs"] = z["Runs"].astype(int)

    # Calculate the sum of runs for the current country
    t = z['Runs'].sum()
    
    # Append the sum to the list
    sum.append(t)

# Create a DataFrame with the country and sum of runs
df = pd.DataFrame({"country":L,"runs":sum})

# Save the DataFrame to a CSV file
df.to_csv('batting_vs_runs_2019.csv')
