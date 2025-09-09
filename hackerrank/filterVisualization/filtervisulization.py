import cv2
import numpy as np
import matplotlib.pyplot as plt
import os  # Add this import for path handling

# Define the six kernels
kernels = {
    "1: Identity": np.array([[0,0,0],[0,1,0],[0,0,0]]),
    "2: Laplacian (all edges)": np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]),
    "3: Sharpen": np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]),
    "4: Blur": np.array([[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]]),
    "5: Sobel X (vertical edges)": np.array([[-1,0,1],[-2,0,2],[-1,0,1]]),
    "6: Sobel Y (horizontal edges)": np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
}

# Load a grayscale test image (change path to your own if needed)
# img = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
img_path = os.path.join(os.path.dirname(__file__), "lena.png")
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Add a check to ensure the image loaded successfully
if img is None:
    raise ValueError(f"Could not load image from {img_path}. Check if the file exists and is a valid image.")

# Apply each filter
results = {}
for name, k in kernels.items():
    filtered = cv2.filter2D(img, -1, k)
    results[name] = filtered

# Plot the results
plt.figure(figsize=(15, 10))
plt.subplot(2, 4, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

for i, (name, filtered) in enumerate(results.items(), start=2):
    plt.subplot(2, 4, i)
    plt.imshow(filtered, cmap="gray")
    plt.title(name)
    plt.axis("off")

plt.tight_layout()
plt.show()