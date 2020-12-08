#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:46:09 2020

@author: ivana
"""
import pandas as pd
#Exercise 3 ------------------------------------------------------------------
#For a given GOterm calculated Chi square statistics


def calculateChiStat(GOterm, tables_dict):
    #Calculates the Chi-squared vals. based on the ABCD values from tables_dict
    values = tables_dict[GOterm]
    nAB = values[0] + values[1] #marginal A+B
    nCD = values[2] + values[3] #marginal C+D
    nAC = values[0] + values[2] #marginal A+C
    nBD = values[1] + values[3] #marginal B+D
    total = values[0]+values[1]+values[2]+values[3]
    expA = (nAB*nAC)/total
    expB = (nAB*nBD)/total
    expC = (nCD*nAC)/total
    expD = (nCD*nBD)/total
    expected = [expA, expB, expC, expD]
    chi_stat = 0
    for i in range(0,3):
        chi_stat += ((values[i] - expected[i])**2)/expected[i]
    return chi_stat
    

def makeChiDf(go_dict, tables_dict, names_dict):
    #Calls calculateChiStat and makes a data frame of Chi-squared vals.
    chi_list = []  
    for go in go_dict.keys():
        chi = calculateChiStat(go, tables_dict)
        chi_list.append(
            {'GO name': names_dict[go],
             'GO term': go,
             'Chi Statistic': chi,
                }
            )
    chi_df = pd.DataFrame(chi_list)
    chi_df = chi_df.sort_values(by =['Chi Statistic'], ascending=False)
    return chi_df

