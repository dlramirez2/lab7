#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:03:42 2018

@author: Diana Ramirez
Professor: Diego Aguirre
TA: Anindita Nath
TR 1:30PM
"""
def edit_distance(st1,st2):
    l1 = len(st1)
    l2 = len(st2)
    mat = []
    for i in range(l2+1):
        mat.append([0]*(l1+1))
        
    for i in range(l1+1):
        mat[0][i] = i
    for i in range(l2+1):
        mat[i][0]= i
        
    for row in range(1,l2+1):
        for col in range(1,l1+1):
            if st1[row-1] == st2[col-1]:
                mat[row][col] = mat[row -1][col-1]
            else:
                 mat[row][col] = 1 + min(mat[row-1][col-1],mat[row][col-1],mat[row-1][col])
    return mat

##testing my method edit_distance by reading the first two lines in a file
g = open("words.txt")
word_list = g.readlines()

for ln in word_list:
    ln = ln.replace('\n','')
st1 = word_list[1]
st2 = word_list[2]
print(edit_distance(st1,st2))