# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 18:39:59 2020

@author: nakano
"""

import pandas as pd
import re

filetxt = r"C:\Users\nakano\Documents\GitHub\Datasets\chatlogs\from_jojo_0025.txt"

chatlog = []
Date = None

with open(filetxt,'r',encoding='utf-8') as f:
    for row in f:
        logs = []
        pattern = r'[12]\d{3}[/\-年](0?[1-9]|1[0-2])[/\-月](0?[1-9]|[12][0-9]|3[01])日?$'
        prog = re.compile(pattern)
        row_p = prog.match(row)
        # print(row)
        if row_p != None:
            Date = row_p.group()
        else:
            pass
        print(Date)

        LOG = [Date]
        if "Sawayaka393:" in row:
            row_re = re.sub(r'[,.、\n ]',"",row)
            Chatli = row_re.split("Sawayaka393:")
            LOG+=Chatli
            
            chatlog.append(LOG)
        
df = pd.DataFrame(chatlog,columns=["Date","time","chatlog"])
df.to_csv(r"../data/ChatLog.csv",index=False)