import pandas as pd
import morestats as m

df = pd.read_csv('baseball.csv')

# find average height, weight, age for all players  using morestats

avg_height = m.mean(df.Height)
avg_weight = m.mean(df.Weight)
avg_age = m.mean(df.Age)

# group by team name and show mean height, weight, Age

teams = df.groupby(['Team'])['Height', 'Weight', 'Age'].agg(['mean'])

# find team with the highest average Height
tallest_team = teams.idxmax()['Height']

# find a subset
bal_to_cle = teams.loc['BAL':'CLE', 'Height':'Weight']
