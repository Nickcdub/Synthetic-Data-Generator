import pandas as pd
from ctgan import CTGAN


def main():

    # Step 1: Load dataset
    df = pd.read_csv("data/raw/fake_data.csv")  # Adjust path as needed

    # Step 2: Optional – preprocess or encode your data
    # For CTGAN, you typically need to identify discrete columns
    discrete_columns = ["name","email","address","phone","company","job","city","state"]


    # Step 3: Train the CTGAN model
    ctgan = CTGAN(batch_size=20,epochs=50, verbose=True)
    ctgan.fit(df, discrete_columns=discrete_columns)

    # Step 4: Generate synthetic samples
    synthetic_df = ctgan.sample(1000)
    synthetic_df.to_csv('data/synthetic/synthetic_data.csv', index=False)
