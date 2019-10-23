
# coding: utf-8

# In[10]:


import requests
import pandas as pd
import sys
from dotenv import load_dotenv
load_dotenv()
import os

api_key = os.getenv("AIRTABLE_API_KEY")
base_id = os.getenv("AIRTABLE_BASE")
table_name = "column_map"

def get_url(offset=None):
    url = "https://api.airtable.com/v0/" + base_id + "/" + table_name + "?maxRecords=1000"
    if offset:
        url += "&offset=" + offset
    url += "&api_key=" + api_key
    return url

def json2df(response):
    field_list = []
    for record in response.json()['records']:
        obj = record['fields']
        obj['id'] = record['id']
        field_list.append(obj)
   
    return pd.DataFrame.from_dict(field_list)

def call_api_get_df(offset):
    response = requests.get(get_url(offset=offset))
    df = json2df(response)
    return response.json(), df

def get_df():
    list_of_dfs = []
    offset = None
    response_json = ["offset"]
    while 'offset' in response_json:
        response_json, temp = call_api_get_df(offset)
        offset = None if "offset" not in response_json else response_json["offset"]
        list_of_dfs.append(temp)
    if sys.version_info[0] == 2:
        df = pd.concat(list_of_dfs)
    else:
        df = pd.concat(list_of_dfs, sort=True)
    df.index = range(len(df))
    return df

