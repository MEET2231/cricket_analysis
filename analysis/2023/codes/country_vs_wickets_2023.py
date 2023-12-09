import pandas as pd

    # List of countries
L =["Australia","Pakistan","India","Sri Lanka","England","Afghanistan","Bangladesh","South Africa","New Zealand","Netherlands",]

    # Empty list to store the sum of Wickets for each country
sum = []

    # Read the bowling data from a CSV file
x=pd.read_csv('bowling_data_2023.csv')

    # Iterate through each country in the list
for i in L:
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
df = pd.DataFrame({"country":L,"Wickets":sum})

    # Print the DataFrame
print(df)
df.to_csv("wickets23.csv")