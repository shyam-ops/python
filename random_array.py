import numpy as np

# Create a 1D array of 50 random integers between 100 and 1000
random_array = np.random.randint(100, 1001, size=50)

print("1D Array of 50 random integers between 100 and 1000:")
print(random_array)
print(f"\nArray shape: {random_array.shape}")
print(f"Array length: {len(random_array)}")
print(f"Minimum value: {random_array.min()}")
print(f"Maximum value: {random_array.max()}")
print(f"Mean value: {random_array.mean():.2f}") 