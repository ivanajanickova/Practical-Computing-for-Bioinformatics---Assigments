#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:05:10 2020

@author: ivana
"""
import pandas as pd
import re
#Exercise 2-------------------------------------------------------------------

def parseFiles(GOannotations, IDs):
    #from given files extracts the relevant information and returns them stored in Hashmaps & sets 
    GO = open(GOannotations, 'r')
    IDs = open(IDs, 'r') #List of differentially expressed genes       
    GO = GO.readlines()[1:] #first line contain header
    go_dict = {}  #creates a HashMap with GOterms as keys and a set of belonging geneIDs as values
    names_dict = {} #HashMap of GOterm (key) & GOName (vlaue) - made for the output of the final data frame
    gene_set = set() #creting a set of genes for which there are GO terms
    for line in GO:
        splitted = re.split(r'\t+', line)
        if(splitted[1] not in go_dict.keys()):
            go_dict[splitted[1]] = set()
            go_dict[splitted[1]].add(splitted[0])
            gene_set.add(splitted[0])  #adds gene to gene_set
            names_dict[splitted[1]] = splitted[2]
        else:
            go_dict[splitted[1]].add(splitted[0]) 
            gene_set.add(splitted[0])    
            names_dict[splitted[1]] = splitted[2]
    #stores all differentially expressed genes in a set
    selected = set()
    for line in IDs.readlines():
        selected.add(line)       
    selected = {x.rstrip() for x in selected} #removes white spaces       
    unselected = {x for x in (gene_set - gene_set.intersection(selected))} #creates a set of genes with no diffrential expression
    return go_dict, gene_set, selected, unselected, names_dict
    
def makeTableDict(go_dict, selected, unselected):       
    #creates HashMap of go term (key) & list cotingecy table values [A, B, C, D]
    tables_dict = {}
    for key in go_dict.keys():
        A,B,C,D = 0,0,0,0
        A = len(selected.intersection(go_dict[key]))
        B = len(unselected.intersection(go_dict[key]))
        C = len(selected) - A
        D = len(unselected) - B
        tables_dict[key] = [A, B, C, D]
    return tables_dict


def makeTable(GOterm, tables_dict):
    #function that returns a data frame corresponding to the contingency table of given GOterm
    values = tables_dict[GOterm]
    col_names = ['Sel', '¬Sel', 'marginal']
    row_names = ['GO', '¬GO', 'marginal']
    df = pd.DataFrame([[values[0], values[1], values[0]+values[1]], 
                       [values[2], values[3], values[2]+values[3]],
                      [values[0]+values[2], values[1]+values[3],
                      values[0]+values[1]+values[2]+values[3]]], col_names, row_names)
    return df

  


 
            
            
            
            
            
            
        
    
        
        
        



    
    






