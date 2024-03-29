import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os

# Specifying the full path to the file
dataset = pd.read_csv(r'C:\Users\Lenovo\Desktop\New folder\Data.csv')
X =  dataset.iloc[: , :-1].values
Y =  dataset.iloc[: , -1].values

#taking care of missing data

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')
imputer.fit(X[: , 1:3])
X[: , 1:3] = imputer.transform(X[: , 1:3])


#encoding the categorical data

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct= ColumnTransformer(transformers=[('encoder' , OneHotEncoder() , [0])] , remainder ='passthrough' ) # here tranformer will specify the kind of transformation and index where the transformation will take place
X = np.array(ct.fit_transform(X))


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Y = le.fit_transform(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X , Y , test_size=0.2 , random_state= 1)

#Feature Scaling :- the main aim is to have all the values on the same level
#so that while training our model it will not be biased towards any particular feature .

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[: , 3:] = sc.fit_transform(X_train[: , 3:])
X_test[: , 3:] = sc.transform(X_test[: , 3:])
print(X_train)
print(X_test)
