# Importing pandas library
import pandas as pd

# Reading the csv file
df=pd.read_csv('Final_Codes_With_Comments/bowling_data_2019.csv')

# Initializing lists to store total strike rate, number of players and average strike rate for each country
T=[]
S=[]
K=[]

# List of countries
L=['Australia', 'Pakistan', 'England' ,'Sri Lanka' ,'India', 'Afghanistan', 'Bangladesh', 'South Africa' ,'New Zealand', 'West Indies']

# Looping through each country to count the number of players
for o in L:
    # Filtering data for the current country
    z1=df.loc[df['Country']==f'{o}']
    
    # Counting number of players for the current country
    m1=z1['SR'].count()
    
    # Appending number of players to the list
    S.append(m1)

# Converting the 'SR' column to numeric, invalid parsing will be set as NaN
df['SR'] = pd.to_numeric(df['SR'], errors='coerce')

# Looping through each country to calculate total and average strike rate
for i in L:
    # Filtering data for the current country
    z=df.loc[df['Country']==f'{i}']
    
    # Calculating total strike rate for the current country
    t=z['SR'].sum()
    
    # Appending total strike rate to the list
    T.append(round(t,1))
    
    # Calculating and appending average strike rate for the current country
    K.append(round(round(t,1)/m1,1))

# Creating a dataframe with the calculated data
myvar=pd.DataFrame({"Country":L,"SR":T,"No. Of Players":S,"Average SR":K})

myvar.to_csv('Bowling_Data_2019_Average_Strike_Rates_By_Countries.csv', index=False)
