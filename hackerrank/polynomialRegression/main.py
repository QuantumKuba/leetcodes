import sys
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import csv
import os
import numpy as np
import matplotlib.pyplot as plt

def plot_3d_regression_surface(ax, degree, title, X_train_np, Y_train_np):
    """Helper function to plot a 3D regression surface for a given degree."""
    # Train a pipeline for the specified degree
    pipeline = Pipeline([
        ('poly', PolynomialFeatures(degree=degree, include_bias=False)),
        ('lin_reg', LinearRegression())
    ])
    pipeline.fit(X_train_np, Y_train_np)

    # Scatter plot of the actual data points
    ax.scatter(X_train_np[:, 0], X_train_np[:, 1], Y_train_np, color='blue', label='Training data', s=15)

    # Create a meshgrid to plot the surface
    x0_min, x0_max = X_train_np[:, 0].min() - 1, X_train_np[:, 0].max() + 1
    x1_min, x1_max = X_train_np[:, 1].min() - 1, X_train_np[:, 1].max() + 1
    x0_grid, x1_grid = np.meshgrid(np.arange(x0_min, x0_max, 0.2),
                                   np.arange(x1_min, x1_max, 0.2))

    # Predict on every point of the grid
    grid_points = np.c_[x0_grid.ravel(), x1_grid.ravel()]
    Y_pred_grid = pipeline.predict(grid_points)
    Y_pred_grid = np.reshape(Y_pred_grid, x0_grid.shape)

    # Plot the regression surface
    ax.plot_surface(x0_grid, x1_grid, Y_pred_grid, alpha=0.6, cmap='viridis')

    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Target (Y)')
    ax.set_title(title)

X_train = []
Y_train = []
X_test = []

os.chdir(os.path.dirname(os.path.abspath(__file__)))


try:
    with open('input.csv', 'r') as file:
        # Read the first line to get F and N
        F, N = map(int, file.readline().split())

        # Read the next N lines for training data
        for _ in range(N):
            line = file.readline().split()
            data_row = list(map(float, line))
            X_train.append(data_row[:F])
            Y_train.append(data_row[F])

        T = int(file.readline().strip())
        
        # Read the next T lines for test data
        for _ in range(T):
            test_row = list(map(float, file.readline().split()))
            X_test.append(test_row)

except FileNotFoundError:
    print("The file 'input.csv' was not found.")
    sys.exit(1)
except (ValueError, IndexError) as e:
    print(f"Error processing file content: {e}")
    sys.exit(1)

# --- Verification ---
print("F:", F)
print("N:", N)
print("X_train (first 2):", X_train[:2])
print("Y_train (first 2):", Y_train[:2])

print("\nT:", T)
print("X_test (first 2):", X_test[:2])



pipeline = Pipeline([
    ('poly', PolynomialFeatures(include_bias=False)),
    ('lin_reg', LinearRegression())])

param_grid = {
    'poly__degree': [1, 2, 3, 4, 5]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, Y_train)

best_degree = grid_search.best_params_['poly__degree']
print(f"Best polynomial degree: {best_degree}")


# --- Visualization ---
# Note: This visualization will only work correctly if you have one or two features.
if F == 1:
    # --- 2D Visualization for a single feature ---
    X_train_np = np.array(X_train)
    Y_train_np = np.array(Y_train)

    plt.figure(figsize=(10, 6))
    plt.scatter(X_train_np, Y_train_np, color='blue', label='Training data', s=10)

    X_range = np.linspace(X_train_np.min(), X_train_np.max(), 400).reshape(-1, 1)

    for degree in param_grid['poly__degree']:
        pipeline_plot = Pipeline([
            ('poly', PolynomialFeatures(degree=degree, include_bias=False)),
            ('lin_reg', LinearRegression())
        ])
        pipeline_plot.fit(X_train_np, Y_train_np)
        Y_pred_range = pipeline_plot.predict(X_range)
        plt.plot(X_range, Y_pred_range, label=f'Degree {degree} fit')

    plt.title('Polynomial Regression Fits for Different Degrees')
    plt.xlabel('Feature (X)')
    plt.ylabel('Target (Y)')
    plt.legend()
    plt.grid(True)
    plt.show()

elif F == 2:
    # --- 3D Visualization for two features: Side-by-side comparison ---
    from mpl_toolkits.mplot3d import Axes3D
    X_train_np = np.array(X_train)
    Y_train_np = np.array(Y_train)

    comparison_degree = 2

    # If the best degree is the same as our comparison degree, just show one plot
    if best_degree == comparison_degree:
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        plot_3d_regression_surface(ax, best_degree, f'Best Fit (Degree {best_degree})', X_train_np, Y_train_np)
        print(f"\nThe best degree is {best_degree}, showing a single plot.")
        plt.show()
    else:
        # Create two subplots side-by-side
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8), subplot_kw={'projection': '3d'})
        
        # Plot for the fixed degree (e.g., 2)
        plot_3d_regression_surface(ax1, comparison_degree, f'Fixed Fit (Degree {comparison_degree})', X_train_np, Y_train_np)
        
        # Plot for the best degree found by GridSearchCV
        plot_3d_regression_surface(ax2, best_degree, f'Best Fit (Degree {best_degree})', X_train_np, Y_train_np)
        
        plt.show()

else:
    print("\nVisualization is only available for 1 or 2 features.")


Y_pred = grid_search.predict(X_test)
for pred in Y_pred:
    print(round(pred, 2))