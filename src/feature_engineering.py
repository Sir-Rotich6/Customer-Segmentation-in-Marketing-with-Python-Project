import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale_features(df):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    return scaled, scaler
