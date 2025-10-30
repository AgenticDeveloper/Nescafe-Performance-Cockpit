import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_data():
    sites = pd.read_csv(DATA_DIR / "sites.csv")
    machines = pd.read_csv(DATA_DIR / "machines.csv")
    deployments = pd.read_csv(DATA_DIR / "deployments.csv")
    return sites, machines, deployments
