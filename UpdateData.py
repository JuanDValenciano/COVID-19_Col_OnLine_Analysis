#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:33:53 2020

@author: juanval
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
from datetime import date
import os
import json

############  Data Colombia   #################################################
# tomado de : https://e.infogram.com/01266038-4580-4cf0-baab-a532bd968d0c?parent_url=https%3A%2F%2Fwww.ins.gov.co%2FNoticias%2FPaginas%2FCoronavirus.aspx&src=embed#
url_dataCol = 'https://e.infogram.com/api/live/flex/a2e70c7d-0e70-46ca-a79a-f7e5a243828a/dfee1a5c-5cc8-4e90-8efb-d5bdf2803bf6'

my_path=os.getcwd()
os.system('mkdir Data')
os.system('curl -XGET '+url_dataCol+' -o Data/DataCol.txt')
workfile_json = my_path+'/Data/DataCol.txt'

# extracción de datos
with open(workfile_json) as f:
    json_data = json.load(f)

listDataCol = json_data["data"]
#Cantidad de datos

header = listDataCol[0][0]
DataCol = listDataCol[0]

DataCol.remove(DataCol[0])

DataCol = pd.DataFrame(DataCol, columns=header) 

print("Summary ")
print("lenDataCol ", len(DataCol))

############  Data World   ####################################################

url_data_world = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
url_confirmed  = 'time_series_19-covid-Confirmed.csv'
url_deaths     = 'time_series_19-covid-Deaths.csv'
url_recoverd   = 'time_series_19-covid-Recovered.csv'

os.system('curl -XGET '+url_data_world+url_confirmed+' -o Data/'+url_confirmed)
os.system('curl -XGET '+url_data_world+url_deaths+' -o Data/'+url_deaths)
os.system('curl -XGET '+url_data_world+url_recoverd+' -o Data/'+url_recoverd)

Confirmed   = pd.read_csv( 'Data/'+url_confirmed)  
deaths      = pd.read_csv( 'Data/'+url_deaths)  
recoveerd   = pd.read_csv( 'Data/'+url_recoverd)  










