import numpy as np
import pandas as pd

data = pd.read_csv('titanic_data.csv')


data = data[data.Fare != 0]
fares = data[pd.notnull(data['Fare'])]

# [0, 1][0, 8]
fares.groupby(['Survived', 'Sex']).describe().Fare.loc[1][0]

fares.groupby(['Pclass', 'Sex']).describe().Fare
