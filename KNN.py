import pandas as pd
import math

Data = pd.read_csv('Defaulter.csv')

age = int(input("Enter age:"))
loan = int(input("Enter loan amount:"))
K = int(input("Enter the value of K:"))


Dists = []

for i in range(len(Data)):
    sum = (Data['Age'][i]-age)**2 + (Data['Loan'][i]-loan)**2
    Distance = math.sqrt(sum)
    Dists.append(Distance)

Offsetlist = []
for i in range(K):
    min=max(Dists)
    for j in range(Dists.__len__()):
        if Dists[j]<min:
            min=Dists[j]
            Offset=j


    Offsetlist.append(Offset)
    Dists.remove(min)


yesCount=0
noCount=0
for i in Offsetlist:
    if Data['Defaulter?'][i]=="Y":
        yesCount=yesCount+1
    else:
        noCount=noCount+1

Sample = [age,loan]
if yesCount>noCount:
    print("Your sample is:-"+str(Sample))
    print("It clusters to Yes")
else:
    print("Your sample is:-" + str(Sample))
    print("It clusters to No")














