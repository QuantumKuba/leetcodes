## Simplified version for hackerrank submission without hyperparameter tuning and visualization



import sys
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

input_data = sys.stdin.read().splitlines()

F, N = map(int, input_data[0].split())

X_train = []
Y_train = []

for i in range(1, N + 1):
    row = list(map(float, input_data[i].split()))
    X_train.append(row[:F])
    Y_train.append(row[F])
    
T = int(input_data[N + 1])

X_test = []

for i in range(N + 2, N + 2 + T):
    row = list(map(float, input_data[i].split()))
    X_test.append(row)

# Build pipeline with fixed degree = 3
pipeline = Pipeline([
    ('poly', PolynomialFeatures(degree=3, include_bias=False)),
    ('lin_reg', LinearRegression())
])

pipeline.fit(X_train, Y_train)

# Predict on test set
Y_pred = pipeline.predict(X_test)

# Print predictions rounded to 2 decimals
for pred in Y_pred:
    print(round(pred, 2))