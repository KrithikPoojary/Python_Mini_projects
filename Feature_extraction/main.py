import numpy as np
import pandas as pd

a = pd.read_csv(r'Feature_extraction/anime.csv')
print(a)

a.head()   # This will give us top rated files
a.loc[4]['Title']   #Through this we can analysis the contant

# Here the first function to extract more information

def extract(title):
    see = False
    episode = ""
    for i in title:
        if i == ")":
            see = False
            return episode
        if see == True:
            episode+=i
        if i == "(":
            see = True


