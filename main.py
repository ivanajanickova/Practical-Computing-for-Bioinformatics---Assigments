#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 22:47:33 2020

@author: ivana
"""



import table 
import chistat
import pandas as pd


#Run the scripts-------------------------------------------------------------------------------------
#For function table.parseFiles() the input arguments are the file names - shoud be located in wd
go_dict, gene_set, selected, unselected, names_dict = table.parseFiles('GOannotations.txt', 'IDS2.txt')
tables_dict = table.makeTableDict(go_dict, selected, unselected)
chi_df = chistat.makeChiDf(go_dict, tables_dict, names_dict)
pd.set_option('display.max_columns', None)
print(chi_df.head()) 

#chi_df.to_csv('chi_df.csv', index = False)





