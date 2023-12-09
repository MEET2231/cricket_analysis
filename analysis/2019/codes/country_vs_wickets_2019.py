import numpy as np
import pandas as pd

    # List of countries
L =["Pakistan","India","Sri Lanka","England","Afghanistan","Bangladesh","South Africa","New Zealand","West Indies","Australia"]

    # Empty list to store the sum of"Wickets for each country
sum = []

    # Read the batting data from a CSV file
x=pd.read_csv("bowling_data_2019.csv")


    # Iterate through each country in the list
for i in L:
    # Filter the data for the current country
    z=x.loc[x['Country']==f'{i}']
 
    
    # Convert the "Wickets" column to integer type
    z["Wickets"] = z["Wickets"].astype(int)

    # Calculate the sum of"Wickets for the current country
    t = z['Wickets'].sum()
    
    # Append the sum to the list
    sum.append(t)

    # Create a DataFrame with the country and"Wickets data
df = pd.DataFrame({"country":L,"Wickets":sum})

    # Print the DataFrame
df.to_csv("country_vs_wickets_2019.csv")
