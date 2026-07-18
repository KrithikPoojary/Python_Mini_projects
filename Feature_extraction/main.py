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

a['Episodes'] = a["Title"].apply(extract)   # so this will mainly apply the changes and insert the new column to the file.

a['Episodes'] = a['Episodes'].str.replace(" eps" , "")  #Here i have replaced because it is str and in future i have to do agg.func which only integrate with int 
print(a)

type(a.loc[0]['Episodes'])     #Just for surety we have seen that it is string

a['Episodes'] = a['Episodes'].astype(int)  # through this we had change the type 'str' to 'int'

type(a.loc[0]['Episodes'])    #just to recheck 



#Just to analyse the changes
a.loc[2]['Title']   # just checking 
a.loc[34]['Title']   # just checking 
a.loc[8]['Title']   # just checking 
a.loc[1]['Title']   # just checking 


#ADDED next functions

def extract2(date):
    check = False
    time = ""
    for i in range(len(date)):
        if date[i] == ")":
            for j in range(i+1 , i+20):
                time += date[j]
            return time
                