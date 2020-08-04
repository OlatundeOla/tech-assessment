# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:02:46 2020

@author: OlatundeOla
"""

# importing pandas as pd 
import pandas as pd 
import os

script_dir = os.getcwd()
input_bucket = script_dir + "\\input_dir\\Loan.csv"
output_bucket = script_dir + "\\output_dir\\Output.csv"


def mth_year(s):
   substr = s.str.slice(3,)
   return substr

# Read the CSV file into a dataframe  
df_csv = pd.read_csv(input_bucket, quotechar="'") 

print(df_csv)

# Transform the date into the format Mon-Year for aggregation pivot  
# and convert Amount into float for summation base on requirement
df_csv.Amount = df_csv.Amount.astype(float)
df_csv['Month'] = mth_year(df_csv.Date)


# perform aggregation - count on turple and sum on amount based on 
# Network, Product and Month 
df_csv_agg = df_csv.groupby(['Network', 'Product','Month'])['Amount'].agg(['count','sum'])
print(df_csv_agg)

# send the output to a file - Output.csv
df_csv_agg.to_csv(output_bucket)
