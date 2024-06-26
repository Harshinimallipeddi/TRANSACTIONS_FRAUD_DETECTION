# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eYDGHuVvLo73v8wLiRLHmzKsFS_XurPv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier

df= pd.read_csv('dataset.csv')

df.head()

cols_to_rename={
    'step': 'TimeStep',
    'type': 'TransactionType',
    'amount': 'TransactionAmount',
    'nameOrig': 'SenderAccountID',
    'oldbalanceOrg': 'SenderBalanceBefore',
    'newbalanceOrig': 'SenderBalanceAfter',
    'nameDest': 'RecipientAccountID',
    'oldbalanceDest': 'RecipientAccountBefore',
    'newbalanceDest': 'RecipientAccountAfter',
    'isFraud': 'IsFraudulantTransaction',
    'isFlaggedFraud': 'IsTransactionFlaggedFraudulent'
}
df.rename(columns=cols_to_rename, inplace=True)
df

categorial_cols= [col for col in df.columns if df[col].dtype=='object']
numerical_cols= [col for col in df.columns if col not in categorial_cols]
numerical_cols

unique_values = df['TransactionType'].unique()
print("Unique Transaction Types:", unique_values)

mapping = {'PAYMENT': 1, 'TRANSFER': 2, 'CASH_OUT': 3, 'CASH_IN': 4, 'DEBIT': 5}

df['TransactionType'] = df['TransactionType'].replace(mapping)
df.head()

unique_senders = df['SenderAccountID'].nunique()
unique_receivers = df['RecipientAccountID'].nunique()

print("sender :", unique_senders)
print("receiver: ", unique_receivers)

df = df.drop(df.index[-1])
df.isnull().sum()

missing_values = df.isnull().sum()

print("Missing values :")
print(missing_values)

plt.figure(figsize=(8, 6))
plt.boxplot(df['TransactionAmount'])
plt.title('Box Plot of Transaction Amount')
plt.ylabel('Transaction Amount')
plt.show()

Q1 = df['TransactionAmount'].quantile(0.25)
Q3 = df['TransactionAmount'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_filtered = df[(df['TransactionAmount'] >= lower_bound) & (df['TransactionAmount'] <= upper_bound)]

plt.figure(figsize=(8, 6))
plt.boxplot(df_filtered['TransactionAmount'])
plt.title('Box Plot of Transaction Amount')
plt.ylabel('Transaction Amount')
plt.show()

df_filtered

float_columns = ['TransactionAmount', 'SenderBalanceBefore', 'SenderBalanceAfter', 'RecipientAccountBefore', 'RecipientAccountAfter']

scaler = StandardScaler()

df_filtered[float_columns] = scaler.fit_transform(df_filtered[float_columns])
df_filtered

drop = ['TimeStep','SenderAccountID','RecipientAccountID']
df_filtered = df_filtered.drop(columns=drop)

df_filtered.info()

X = df_filtered.drop(['IsFraudulantTransaction', 'IsTransactionFlaggedFraudulent'], axis=1)
y = df_filtered['IsFraudulantTransaction']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)



