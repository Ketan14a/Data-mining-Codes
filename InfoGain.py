from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


Data = pd.read_csv('data.csv')

Data = Data[['Outlook','TemperatureNominal','HumidityNominal','Windy','Play']]
Data['Outlook'] = Data['Outlook'].map({'overcast': 0,'rainy': 1,'sunny': 2})
Data['TemperatureNominal'] = Data['TemperatureNominal'].map({'cool': 0,'mild': 1,'hot': 2})
Data['HumidityNominal'] = Data['HumidityNominal'].map({'normal': 0,'high': 1})
#Data['Windy'] = Data['Windy'].map({'FALSE': 0,'TRUE': 1})
print(Data)
#Data.dropna()

X = Data.drop('Play', axis=1)
Y = Data['Play']
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42,test_size=0.2)
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
print(accuracy_score(y_test, y_predict))

Cmatrix=pd.DataFrame(
    confusion_matrix(y_test, y_predict))
print(Cmatrix)

print(y_test)










