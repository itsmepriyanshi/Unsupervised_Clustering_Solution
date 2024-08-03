import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def describe_data(df):
    """Return basic statistics of the dataset."""
    return df.describe()

def check_shape(df):
    """Return the shape of the dataset."""
    return df.shape