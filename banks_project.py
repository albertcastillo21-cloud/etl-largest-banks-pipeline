"""This project is a systemn for generating
information that can be run every quarte"""

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime


def log_progress(message):
    """ This function logs the mentioned message at a given
    stage of the code execution to a log file. Function returns nothing """
    
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('code_log.txt',"a") as f:
        f.write(timestamp + ',' + message + '\n')

def extract(URL, table_attribs):
    """This function aims to extract the required 
    information from web site  and save it to dataframe.
    The function returns the dataframe for further processing."""
    
    pag = requests.get(URL).text
    data = BeautifulSoup(pag, 'html.parser')
    df = pd.DataFrame(columns= table_attribs)
    table = data.find_all("tbody")
    rows = table[0].find_all('tr')
    
    for row in rows:
        col = row.find_all('td')
        if len(col) == 3 and col[1].text.strip() != '':
            data_dict = {'Name': col[1].text.strip(), 
                        'MC_USD_Billion': col[2].text.strip()}
            df1 = pd.DataFrame([data_dict])
            df = pd.concat([df, df1], ignore_index=True)
    
    return df

def transform(df):
    """ This function converts the GBP information from currency
    format to float value.
    The function returns the transformed dataframe"""
    
    exchange_rate = pd.read_csv('exchange_rate.csv')
    exchange_rate = exchange_rate.set_index('Currency').to_dict()['Rate']
    
    df['MC_USD_Billion'] = df['MC_USD_Billion'].astype(float)
    
    df['MC_GBP_Billion'] = np.round(df['MC_USD_Billion'] * exchange_rate['GBP'], 2)
    df['MC_EUR_Billion'] = np.round(df['MC_USD_Billion'] * exchange_rate['EUR'], 2)
    df['MC_INR_Billion'] = np.round(df['MC_USD_Billion'] * exchange_rate['INR'], 2)

    return df

def load_to_csv(df, csv_path):
    """This function saves the final dataframe as CSV file
    in the provided path. Function returns nothing"""
    
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, name_table):
    """ This function saves the final dataframe as database
    table with the provided name. Function returns nothing"""
    
    df.to_sql(name_table, sql_connection, if_exists = 'replace', index=False )
    
    
def run_query(query_statement, sql_connection):
    """ This function runs the stated query on the database table and
    print the output  on the terminal. Function retuns nothing"""
    
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
    