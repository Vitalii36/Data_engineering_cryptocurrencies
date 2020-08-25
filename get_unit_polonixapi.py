import pandas as pd
import numpy as np
import json
import requests

response = requests.get('https://poloniex.com/public?command=returnTicker')
df = pd.DataFrame(response.json())
df.to_csv('~/Documents/DataScience/My_Project/Project_v3_data_engineering/app/csv/polonixinfo.csv')