import itertools import groupby
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

TV=pd.read_csv(r'C:\Users\kevin\OneDrive\Documents\BZAN_544_Decision_Support\final_project\TV_Ratings_onesheet.csv')#Kevin 
GAMES=pd.read_csv(r'C:\Users\kevin\OneDrive\Documents\BZAN_544_Decision_Support\final_project\games_flat_xml_2012-2018.csv') #Kevin

TV=pd.read_csv('TV_Ratings_onesheet.csv')
TV.head()
GAMES=pd.read_csv('games_flat_xml_2012-2018.csv')
GAMES.head()

#Finding average viewers per Network
TV.groupby(['Network']).mean()

#ABC has the most viewers per game


#Home pass yards stats
GAMES['pass_yds_home'].describe()
#the mean home pass yards is 238. More than that might be more exciting for fans and get more views

plt.bar(TV['HomeTeamID'], TV['VIEWERS'])
plt.xticks(rotation = 90)
plt.title('TV viewership per home team')
plt.show()

plt.scatter(TV['VIEWERS'], TV['RATING'])
plt.xticks(rotation = 90)
plt.title('TV ratings per viewers')
plt.show()
#Shows that ratings and viewers are directly related

#Total Tv viewership by network
plt.bar(TV['Network'], TV['VIEWERS'])
plt.title('Total TV viewership by network')
plt.show()

#Which networks have the most games
plt.bar(TV['Network'], TV['GAME'])
plt.title('Which networks have the most games')
plt.show()



#which Networks get the higest rating games
#TV['RATING2'] = filter(TV.where(TV['RATING'] > 3))

#TV['RATING3'] = TV['RATING']>3
#TV['RATING3'].astype(int)


#Total Tv viewership by network
# plt.bar(TV['Network'], TV['RATING'].mean())
# plt.bar(TV['Network'], TV['RATING3'].count())
# plt.title('Total TV viewership by network')
# plt.show()
