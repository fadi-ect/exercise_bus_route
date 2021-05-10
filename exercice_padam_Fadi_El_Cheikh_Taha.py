# Author : Fadi El Cheikh Taha

import pandas as pd
import numpy as np

from Clusterization import matches

###############################################################################
# Loading Dataset
print("\n-----------------")
print("|Loading Dataset|")
print("-----------------\n")

df = pd.read_csv("OD.csv", names=['longitude_depart', 'latitude_depart',
                                  'longitude_destination', 'latitude_destination'], delimiter=';')
print(df.info())
###############################################################################
#Data Preparation
print("\n------------------")
print("|Data Preparation|")
print("------------------\n")

# Check for missing or duplicates values
print("Null values ?", df.isnull().values.any(), "\t", "Duplicate values ?", df.duplicated().any())

# Delete duplicates
df_prepared = df.drop_duplicates(keep='last')
print("\nShape of our DataFrame whitout duplicate values : ", df_prepared.shape)
###############################################################################
#Clusterization
print("\n--------------")
print("|Clusterization|")
print("----------------\n")
result = df_prepared.apply(lambda row: matches(row, df_prepared), axis=1)
result = [elem[0] for elem in result.to_numpy() if len(elem) > 0]

keepCols = ['longitude_depart', 'latitude_depart', 'longitude_destination', 'latitude_destination']
df_final = pd.DataFrame(result, columns=keepCols).drop_duplicates(keep='last').reset_index(drop=True)

print('DataFrame after clusterization\n')
df_final.info()

print("\nNumber of bus routes before clustering :", len(df_prepared))
print("Number of bus routes after clustering :", len(df_final))
###############################################################################
