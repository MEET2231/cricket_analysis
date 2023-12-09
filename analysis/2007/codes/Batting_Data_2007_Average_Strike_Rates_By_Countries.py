# Importing pandas library
import pandas as pd

# Reading the csv file
df=pd.read_csv('2007/batting_data_2007.csv')

# Initializing lists to store total strike rate, number of players and average strike rate for each country
T=[]
S=[]
K=[]

# List of countries
L=['Australia', 'Pakistan', 'England' ,'Kenya' ,'India', 'Scotland', 'Bangladesh', 'West Indies' ,'New Zealand', 'Zimbabwe']

# Looping through each country
for i in L:
    # Filtering data for the current country
    z=df.loc[df['Country']==f'{i}']
    
    # Calculating total strike rate for the current country
    t=z['SR'].sum()
    
    # Counting number of players for the current country
    m=z['SR'].count()
    
    # Appending total strike rate and number of players to their respective lists
    T.append(round(t,2))
    S.append(m)
    
    # Calculating and appending average strike rate for the current country
    K.append(round(round(t,2)/m,2))

# Creating a dataframe with the calculated data
myvar=pd.DataFrame({"Country":L,"SR":T,"No. Of Players":S,"Average SR":K})

myvar.to_csv("Batting_Data_2007_Average_Strike_Rates_By_Countries.csv")
