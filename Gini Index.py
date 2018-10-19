from pandas import read_csv
import pandas as pd
import numpy as np
import itertools


# reading a csv file
file = r'dataset.csv'
data = pd.read_csv(file)
Ginis = {}
L = data['outlook']
S = set(L)
#print(S)


Subsets = set(itertools.combinations(S,2))

totalRows=0
for i in data:
    totalRows+=1


for i in Subsets:
    Totalfavour=0
    pos=0
    yes1=0
    no1=0
    yes2=0
    no2=0
    TotalNotFavour=0
    MaxGini = -999
    print("For " + str(i))
    for j in data['outlook']:
        if j in i:
            Totalfavour+=1
            if data['play'][pos]=='yes':
                yes1+=1
            else:
                no1+=1
            pos+=1
        else:
            TotalNotFavour+=1
            if data['play'][pos]=='yes':
                yes2+=1
            else:
                no2+=1
            pos+=1

    print("total Favour:-" + str(Totalfavour))
    print("toal not Favour:-" + str(TotalNotFavour))
    print("yes1="+str(yes1))
    print("no1="+str(no1))
    print("yes2="+str(yes2))
    print("no2="+str(no2))

    #sum1 = (Totalfavour / totalRows) * (1 - (((yes1 / Totalfavour) ** 2) - ((no1 / Totalfavour) ** 2)))
    #sum2 = (TotalNotFavour / totalRows) * (1 - (((yes2 / TotalNotFavour) ** 2) - ((no2 / TotalNotFavour) ** 2)))
    gini = sum1 + sum2
    print(gini)

    if gini > MaxGini:
        MaxGini = gini



Ginis['outlook'] = MaxGini






















