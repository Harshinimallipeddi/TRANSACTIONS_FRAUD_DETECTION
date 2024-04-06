# TRANSACTIONS_FRAUD_DETECTION

This project is an implementation of a Fraud Detection System using a Decision Tree algorithm, built with Python's scikit-learn library. It features a web interface created with Flask, allowing users to interactively predict and analyze fraudulent activities in financial transactions.

->What things you need to install the software and how to install them:
Copy code
Python 3.x
Flask
scikit-learn
pandas
numpy

The Decision Tree model is trained on a dataset containing historical transaction data, where each transaction is labeled as fraudulent or legitimate. The model learns patterns from this data, enabling it to predict fraud in new transactions.

Commands used:
import pickle
import sklearn
from flask import Flask, request, render_template

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
