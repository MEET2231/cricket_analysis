import numpy as np
import pandas as pd

# List of countries
L=['Australia', 'Pakistan', 'England' ,'Sri Lanka' ,'India', 'Afghanistan', 'Bangladesh', 'South Africa' ,'New Zealand', 'United Arab Emirates','Ireland','West Indies','Scotland','Zimbabwe']


# Empty list to store the sum of runs for each country
sum = []

# Read the batting data from a CSV file
x=pd.read_csv("C:/Users/Tushar's Device/OneDrive/Desktop/Python/batting_data_2015.csv")

# Iterate through each country in the list
for i in L:
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
df = pd.DataFrame({"country":L,"runs":sum})

# Print the DataFrame
print(df)
df.to_csv("cache/runs_2015.csv")
