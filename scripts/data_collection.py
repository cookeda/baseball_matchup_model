# scripts/data_collection.py
from pybaseball import statcast
import pandas as pd
from datetime import datetime, timedelta
import os

end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

data = statcast(start_dt=start_date, end_dt=end_date)

os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

raw_file_path = f'data/raw/statcast_data_{end_date}.csv'
data.to_csv(raw_file_path, index=False)

