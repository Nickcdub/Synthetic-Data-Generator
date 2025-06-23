from sdmetrics.reports.single_table import QualityReport
import pandas as pd

def main():
    #Define the data sets
    df_real = pd.read_csv("data/raw/fake_data.csv")
    df_synthetic = pd.read_csv("data/synthetic/synthetic_data.csv")

    #Define the metadata
    metadata = {
        "columns": {
            "name": {"sdtype": "categorical"},
            "email": {"sdtype": "categorical"},
            "address": {"sdtype": "categorical"},
            "phone": {"sdtype": "categorical"},
            "company": {"sdtype": "categorical"},
            "job": {"sdtype": "categorical"},
            "city": {"sdtype": "categorical"},
            "state": {"sdtype": "categorical"}
        }
    }

    report = QualityReport()
    report.generate(real_data=df_real, synthetic_data=df_synthetic, metadata=metadata)
    report.get_score()  # Overall quality score
    report.get_details('Column Shapes')
    # Detailed breakdown per column
