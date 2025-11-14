import pandas as pd

def load_data(path):
    """Load raw dataset."""
    return pd.read_csv(path)

def clean_data(df):
    """Handle missing values and clean dataset."""
    # Fill missing minutes_watched with 0
    df['minutes_watched'] = df['minutes_watched'].fillna(0)
    return df

def encode_data(df):
    """Encode categorical features using dummies."""
    df = pd.get_dummies(df, columns=['region', 'channel'], prefix=['region', 'channel'])
    return df

def save_processed(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = load_data("data/raw/customer_segmentation_data.csv")
    df = clean_data(df)
    df = encode_data(df)
    save_processed(df, "data/processed/processed_data.csv")
