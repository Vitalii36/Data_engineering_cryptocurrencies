import pandas as pd
import numpy as np
import json
import requests

response = requests.get('https://poloniex.com/public?command=returnTicker')
df = pd.DataFrame(response.json())
df.to_csv('~/Documents/app/csv/polonixinfo.csv')