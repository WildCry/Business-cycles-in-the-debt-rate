import json
import pandas as pd
import requests
import matplotlib.pyplot as plt
# pyjstat is the package to read JSON-stat, 'pip install pyjstat' 
from pyjstat import pyjstat

def apiToDataframe(postUrl, query):
    
	# postUrl PostUrl where you you want the query posted

	res = requests.post(postUrl, json=query)
	# put the result in variable ds. Here you also have some metadata
	ds = pyjstat.Dataset.read(res.text)
	# write resultatet to 2 dataframes
    # first dataframe with text
	df = ds.write('dataframe')
    # next dataframe with codes
	df_id = ds.write('dataframe', naming='id')
    # returner also ds if one need metadata
	return df, df_id, ds

def plot_ts_group(df, group_name, x, y):
    groups = df.groupby(group_name)
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.plot( group[x], group[y], label=name)
    
    plt.figure(figsize=(10, 4))
    plt.grid(True)
    ax.legend()
    plt.show()