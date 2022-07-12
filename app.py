#!python3.9

from importlib.resources import path
import os
from unittest.mock import patch
import connection
import pandas as pd
import numpy as np

if __name__ == "__main__":

    #listpath
    path = os.getcwd()
    path_query = path + '/sql/'

    #list filename
    file_query = 'dml_query_1.sql'

    #connection
    conn = connection.db_connect()
    cur = conn.cursor()

    #read data
    with open (path_query + file_query,'r') as file:
        query = file.read()
    cur.execute(query)
    data = cur.fetchall()
    df =  pd.DataFrame(data, columns=['order','customer','city','date'])
    
    #transformation
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['date'].dt.year == 2016]
    df['date'] = df['date'].dt.strftime('%y-%m-%d')
    
    df \
        .groupby(['city','date']) \
        .agg({'order':'count'}) \
        .unstack() \
        .to_excel('report_order.xlsx')

    df \
        .groupby(['city','date']) \
        .agg({'customer':'nunique'}) \
        .unstack() \
        .to_excel('report_customer.xlsx')    