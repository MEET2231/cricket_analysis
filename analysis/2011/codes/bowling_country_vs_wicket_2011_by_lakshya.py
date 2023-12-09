import pandas as pd

    # List of countries
Lakshya =["Australia","Pakistan","India","Sri Lanka","Ireland","Zimbabwe","Canada","Kenya","England","West Indies","Bangladesh","South Africa","New Zealand","Netherlands"]

    # Empty list to store the sum of Wickets for each country
sum = []

    # Read the bowling data from a CSV file
x=pd.read_csv('C:/Users/rajja/OneDrive/Desktop/bowling_data_2011.csv')

    # Iterate through each country in the list
for i in Lakshya:
        # Filter the data for the current country
    z=x.loc[x['Country']==f'{i}']
    print(z)
    
        # Convert the "Wickets" column to integer type
    z["Wickets"] = z["Wickets"].astype(int)

        # Calculate the sum of Wickets for the current country
    t = z['Wickets'].sum()
    
        # Append the sum to the list
    sum.append(t)

    # Create a DataFrame with the country and Wickets data
df = pd.DataFrame({"country":Lakshya,"Wickets":sum})

    # Print the DataFrame
print(df)
df.to_csv("country_vs_wicket_2011_by_lakshya.csv")