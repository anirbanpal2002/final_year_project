import pandas as pd
import numpy as np

# Load the uploaded CSV file
file_path = 'test.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data
data.head(), data.shape


# Function to generate augmented data
def generate_augmented_data(original_data, num_samples=1000):
    augmented_data = original_data.sample(n=num_samples, replace=True).reset_index(drop=True)
    
    # Add slight modifications to the numeric columns
    numeric_cols = original_data.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        noise = np.random.normal(0, 0.1, size=augmented_data[col].shape)
        augmented_data[col] += noise
        augmented_data[col] = augmented_data[col].clip(lower=original_data[col].min(), upper=original_data[col].max())
    
    # Ensure the values in integer columns are integers
    integer_cols = original_data.select_dtypes(include=[np.int64]).columns
    for col in integer_cols:
        augmented_data[col] = augmented_data[col].round().astype(int)
    
    return augmented_data

# Generate 1,000 augmented data points
augmented_data = generate_augmented_data(data, num_samples=1000)

# Combine the original and augmented data
combined_data = pd.concat([data, augmented_data], ignore_index=True)

# Save the augmented data to a new CSV file
output_file_path = 'augmented_test.csv'
combined_data.to_csv(output_file_path, index=False)

# Display the first few rows of the combined data and its shape
combined_data.head(), combined_data.shape


# Function to generate augmented data
def generate_augmented_data(original_data, num_samples=1000):
    augmented_data = original_data.sample(n=num_samples, replace=True).reset_index(drop=True)
    
    # Add slight modifications to the numeric columns
    numeric_cols = original_data.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        noise = np.random.normal(0, 0.1, size=augmented_data[col].shape)
        augmented_data[col] += noise
        augmented_data[col] = augmented_data[col].clip(lower=original_data[col].min(), upper=original_data[col].max())
    
    # Ensure the values in integer columns are integers
    integer_cols = original_data.select_dtypes(include=[np.int64]).columns
    for col in integer_cols:
        augmented_data[col] = augmented_data[col].round().astype(int)
    
    return augmented_data

# Generate 1,000 augmented data points
augmented_data = generate_augmented_data(data, num_samples=1000)

# Combine the original and augmented data
combined_data = pd.concat([data, augmented_data], ignore_index=True)

# Save the augmented data to a new CSV file
output_file_path = 'augmented_test.csv'
combined_data.to_csv(output_file_path, index=False)

# Display the first few rows of the combined data and its shape
combined_data.head(), combined_data.shape

