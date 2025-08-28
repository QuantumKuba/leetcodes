#!/bin/python3

import math
import os
import random
import re
import sys
from sklearn.linear_model import LinearRegression

# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    # Read input from file
    with open('trainingdata.txt', 'r') as file:
        # the charging time as input
        # the batery lasts as output
        data = [list(map(float, line.strip().split(','))) for line in file]
        charge_times = [row[0] for row in data]
        durations = [row[1] for row in data]
        
    # Reshape data for scikit-learn
    # X should be a 2D array, y can be a 1D array
    X = [[t] for t in charge_times]
    y = durations

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Read the charging time for which we want to predict the battery life
    time_to_charge = float(input())

    # Predict the battery duration
    # The model expects a 2D array for prediction
    predicted_duration = model.predict([[time_to_charge]])

    # The problem states that if the charging time is more than 4 hours,
    # the battery life is capped at 8 hours.
    if time_to_charge >= 4.0:
        print(8.0)
    else:
        print(round(predicted_duration[0], 2))




