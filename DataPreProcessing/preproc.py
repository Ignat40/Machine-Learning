import numpy as np 
import matplotlib as plt
import pandas as pd

dataset = pd.read_csv('/content/sample_data/Data.csv')
# splitting the data 
x = dataset.iloc[:, :-1].values # taking all the features (independent variables) excluding the last column
y = dataset.iloc[:, -1].values # taking just the last column (dependent variable)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")

imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')
x = np.array(ct.fit_transform(x))

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])