import pandas as pd
import numpy as np
nfl_data = pd.read_csv('nfl_data.csv')


missing_values_count = nfl_data.isnull().sum()
missing_values_count[0:10]