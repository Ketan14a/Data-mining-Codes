import pandas as pd

Data = pd.read_csv('data.csv')
TotalYesCount=0
TotalNoCount=0
Rows = 0
DecisionVector = []
for i in Data['Play']:
    if i=="yes":
        TotalYesCount=TotalYesCount+1
    else:
        TotalNoCount=TotalNoCount+1

    DecisionVector.append(i)
    Rows=Rows+1


PrYes = TotalYesCount/Rows
PrNo = TotalNoCount/Rows

pos=0
SunnyYes=0
SunnyNo=0
OverYes=0
OverNo=0
RainyNo=0
RainyYes=0

for i in Data['Outlook']:
    if i=="sunny":
        if Data['Play'][pos]=="yes":
            SunnyYes=SunnyYes+1
        else:
            SunnyNo=SunnyNo+1
        pos=pos+1
    elif i=='rainy':
        if Data['Play'][pos]=="yes":
            RainyYes=RainyYes+1
        else:
            RainyNo=RainyNo+1
        pos=pos+1

    else:
        if Data['Play'][pos]=="yes":
            OverYes=OverYes+1
        else:
            OverNo=OverNo+1

        pos=pos+1

PrSunnyYes=SunnyYes/TotalYesCount
PrSunnyNo=SunnyNo/TotalNoCount
PrRainyYes=RainyYes/TotalYesCount
PrRainyNo=RainyNo/TotalNoCount
PrOvercastYes=OverYes/TotalYesCount
PrOvercastNo=OverNo/TotalNoCount

HotYes=0
HotNo=0
ColdYes=0
ColdNo=0
MildYes=0
MildNo=0
pos=0
for i in Data['TemperatureNominal']:
    if i=="hot":
        if Data['Play'][pos]=="yes":
            HotYes=HotYes+1
        else:
            HotNo=HotNo+1
        pos=pos+1
    elif i=="mild":
        if Data['Play'][pos]=="yes":
            MildYes=MildYes+1
        else:
            MildNo=MildNo+1
        pos=pos+1
    else:
        if Data['Play'][pos]=="yes":
            ColdYes=ColdYes+1
        else:
            ColdNo=ColdNo+1
        pos=pos+1


PrHotYes=HotYes/TotalYesCount
PrHotNo=HotNo/TotalNoCount
PrMildYes=MildYes/TotalYesCount
PrMildNo=MildNo/TotalNoCount
PrColdYes=ColdYes/TotalYesCount
PrColdNo=ColdNo/TotalNoCount


HighYes=0
HighNo=0
NormalYes=0
NormalNo=0
pos=0

for i in Data['HumidityNominal']:
    if i=="high":
        if Data['Play'][pos]=="yes":
            HighYes=HighYes+1
        else:
            HighNo=HighNo+1
        pos=pos+1
    else:
        if Data['Play'][pos]=="yes":
            NormalYes=NormalYes+1
        else:
            NormalNo=NormalNo+1
        pos=pos+1

PrHighYes=HighYes/TotalYesCount
PrHighNo=HighNo/TotalNoCount
PrNormalYes=NormalYes/TotalYesCount
PrNormalNo=NormalNo/TotalNoCount



WindyTrueYes=0
WindyTrueNo=0
WindyFalseYes=0
WindyFalseNo=0
pos=0

for i in Data['Windy']:
    if i=="TRUE":
        if Data['Play'][pos]=="yes":
            WindyTrueYes=WindyTrueYes+1
        else:
            WindyTrueNo=WindyTrueNo+1
        pos=pos+1
    else:
        if Data['Play'][pos]=="no":
            WindyFalseYes=WindyFalseYes+1
        else:
            WindyFalseNo=WindyFalseNo+1
        pos=pos+1


PrWindyTrueYes=WindyTrueYes/TotalYesCount
PrWindyFalseYes=WindyFalseYes/TotalYesCount
PrWindyTrueNo=WindyTrueNo/TotalNoCount
PrWindyFalseNo=WindyFalseNo/TotalNoCount

print("Naive Bayes Model trained!")

Outlook=input("Enter Outlook:")
Temp=input("Enter temperature:")
Humidity=input("Enter humidity:")
Windy=input("Is it Windy?:")

Vector = [Outlook,Temp,Humidity,Windy]

YesProb=PrYes
NoProb=PrNo

if Vector[0]=="overcast":
    YesProb=YesProb*PrOvercastYes
    NoProb=NoProb*PrOvercastNo
elif Vector[0]=="sunny":
    YesProb=YesProb*PrSunnyYes
    NoProb=NoProb*PrSunnyNo
elif Vector[0]=="rainy":
    YesProb=YesProb*PrRainyYes
    NoProb=NoProb*PrRainyNo


if Vector[1]=="hot":
    YesProb=YesProb*PrHotYes
    NoProb=NoProb*PrHotNo
elif Vector[1]=="mild":
    YesProb=YesProb*PrMildYes
    NoProb=NoProb*PrMildNo
elif Vector[1]=="cool":
    YesProb=YesProb*PrColdYes
    NoProb=NoProb*PrColdNo



if Vector[2]=="high":
    YesProb=YesProb*PrHighYes
    NoProb=NoProb*PrHighNo
elif Vector[2]=="normal":
    YesProb=YesProb*PrNormalYes
    NoProb=NoProb*PrNormalNo


if Vector[-1]=="TRUE":
    YesProb=YesProb*PrWindyTrueYes
    NoProb=NoProb*PrWindyTrueNo

elif Vector[-1]=="FALSE":
    YesProb=YesProb*PrWindyFalseYes
    NoProb=NoProb*PrWindyFalseNo




print("Yes Probability:"+str(YesProb))
print("No Probability:"+str(NoProb))

if YesProb>NoProb:
    print("Your Sample is " + str(Vector))
    print("It classifies to YES")
    print("Hence, there will be a play under above conditions")

else:
    print("Your Sample is " + str(Vector))
    print("It classifies to NO")
    print("Hence, there won't be a play under above conditions")




























































