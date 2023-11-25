# -*- coding: utf-8 -*-
"""
@author: BOJIN LIU - 2023
@email: helloe341@gmail.com
"""

from json import JSONDecodeError
import ssl
import requests
import pandas as pd

base_url="https://quickstats.nass.usda.gov/api/"

API_KEY = None

def Key_init(api_key):
    try:
        global API_KEY
        API_KEY = api_key
        response = requests.get(base_url+"api_GET",params={"key":API_KEY,"format":"JSON"})
        if response.json()['error'][0]=="exceeds limit=50000":
            print("API Key initialized successfully")
        else:
            print("API Key initialization failed,Please check if the API KEY is correct")
    except JSONDecodeError:
    # When JSON parsing fails, execute this code
        print("Unable to parse JSON response.")
        print("Response content:", response.text)
    except requests.exceptions.RequestException as e:
    # Catch exceptions related to other requests
        print("Request error：", e)



def get_data(params):
    # Get specific data by placing query items in the params dictionary
    # and return the type is dataframe
    if API_KEY==None:
        print("Please initialize the API Key first:Key_init('your api key')")
        return
    url=base_url+"api_GET"
    params["key"]=API_KEY
    params["format"]="JSON"
    try:
        response = requests.get(url,params=params)
    except ssl.SSLError as e:
        print("The request is too frequent, please try again later.")
    if response.ok:
        res=response.json() #dict类型
        res_df=pd.DataFrame(res["data"])
        
        # Rename some columns to match the names used in the website's filtering parameters
        columes_rename = {
            "source_desc":"Program",
            "sector_desc":"Sector",
            "group_desc":"Group",
            "commodity_desc":"Commodity",
            "statisticcat_desc":"Category",
            "short_desc":"Data Item",
            "domain_desc":"Domain",
            "domaincat_desc":"Domain Category",
            "agg_level_desc":"Geographic Level",
            "state_name":"State",
            "asd_desc":"Ag District",
            "county_name":"County",
            "region_desc":"Region",
            "zip_5":"Zip Code",
            "watershed_desc":"Watershed",
            "freq_desc":"Period Type",
            "reference_period_desc":"Period"
        }
        res_df.rename(columns=columes_rename,inplace=True)
        
        # Sort the columns in the desired order
        columes_order = [
        'Program', 'year', 'Period', 'Period Type', 'week_ending', 
        'country_name', 'country_code',  # Country
        'state_ansi', 'state_fips_code', 'state_alpha', 'State',  # State/Province
        'Region', 'asd_code', 'Ag District', 'Geographic Level',  # Area/Region
        'county_ansi', 'county_code', 'County',  # County
        'Sector','prodn_practice_desc', 'unit_desc', 'Domain Category',
        'Watershed', 'location_desc', 'Commodity', 'Domain', 'Category', 
        'util_practice_desc', 'watershed_code', 
        'Group', 'Data Item', 'Zip Code', 
        'class_desc', 'Value', 'CV (%)', "begin_code", "load_time",
        "end_code", "congr_district_code"]

        res_df=res_df[columes_order]
        
        return res_df
    else:
        status = response.status_code
        status_str='Response code ' + str(status) + ': ' + response.json()['error'][0]
        print(status_str)
        return pd.DataFrame()
    


def get_par(par):
    # Enter column or header name, and what items are available under it
    if API_KEY==None:
        print("Please initialize the API Key first:Key_init('your api key')")
        return
    url=base_url+"get_param_values"
    param={"param":par}
    param["key"]=API_KEY
    param["format"]="JSON"
    response = requests.get(url,params=param)
    if response.ok:
        res=response.json() # dict type
        return pd.DataFrame(res)
    else:
        status = response.status_code
        status_str='Response code ' + str(status) + ': ' + response.json()[par][0]
        print(status_str)
        return pd.DataFrame()
    

def get_counts(params):
    # Get the number of rows in the queried data
    if API_KEY==None:
        print("Please initialize the API Key first:Key_init('your api key')")
        return
    url=base_url+"get_counts"
    params["key"]=API_KEY
    params["format"]="JSON"
    response = requests.get(url,params=params)
    if response.ok:
        res=response.json() # dict type
        return res["count"]
    else:
        status = response.status_code
        status_str='Response code ' + str(status) + ': ' + response.json()['error'][0]
        print(status_str)
        return status_str