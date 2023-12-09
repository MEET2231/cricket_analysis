import pandas as pd

    # List of countries
L=['Australia', 'Pakistan', 'England' ,'Sri Lanka' ,'India', 'Afghanistan', 'Bangladesh', 'South Africa' ,'New Zealand', 'United Arab Emirates','Ireland','West Indies','Scotland','Zimbabwe']


    # Empty list to store the sum of Wickets for each country
sum = []

    # Read the bowling data from a CSV file
x=pd.read_csv("C:/Users/Tushar's Device/Downloads/bowling_data_2015.csv")

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
df.to_csv("cache/wickets_2015.csv")