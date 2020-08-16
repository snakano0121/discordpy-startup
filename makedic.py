# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 01:00:17 2020

@author: User
"""

filename = r"C:\Users\User\Documents\GitHub\discordpy-startup\words.txt"
def read_pn_di():

    dic_pn = {}

    f = open(r"words.txt",encoding="utf-8")
    lines = f.readlines() # 1行を文字列として読み込む(改行文字も含まれる)
    
    for line in lines:
        #フォーマット
        #見出し語:読み(ひらがな):品詞:感情極性実数値
        columns = line.split(':')
        dic_pn[columns[0]] = float(columns[3])
    f.close

    return dic_pn

out = read_pn_di()

with open("dic.txt", mode='w') as f:
    f.write(str(out))
