import sys
from sklearn.linear_model import LinearRegression
import os 

if __name__ == '__main__':
    # navigate to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Read training data
    with open('trainingdata.txt', 'r') as file:
        data = [list(map(float, line.strip().split(','))) for line in file]

    # Filter out capped values (battery = 8.0)
    # this is because we want to model the uncapped relationship
    filtered = [(x, y) for x, y in data if y < 8.0]

    # Prepare features and targets
    X = [[row[0]] for row in filtered]
    y = [row[1] for row in filtered]

    # Train linear regression on the uncapped region
    model = LinearRegression()
    model.fit(X, y)

    # Read test input (charging time)
    time_to_charge = float(sys.stdin.read().strip())

    # Predict duration
    pred = model.predict([[time_to_charge]])[0]

    # Clamp to maximum battery life (8.0 hours)
    pred = min(pred, 8.0)

    # Print with two decimal places
    print(format(pred, ".2f"))
