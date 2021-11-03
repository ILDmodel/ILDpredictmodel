# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:27:14 2021

@author: PC
"""
import re
# In[]
def outcome(model,input_from_gui,data_used):
    input_used=str(input_from_gui).split(",")
    age = int(input_used[0])
    m = re.search(input_used[1],"F",re.IGNORECASE)
    if bool(m)==True:
        gender=2
    else:
        gender=1
    data_used.iloc[0,0]=gender
    data_used.iloc[0,1]=float(input_used[3])
    data_used.iloc[0,2]=float(input_used[4])
    data_used.iloc[0,3]=float(input_used[2])
    if age<65:
        data_used.iloc[0,4]=0
        data_used.iloc[0,5]=0
    elif age<75:
        data_used.iloc[0,4]=1
        data_used.iloc[0,5]=1
    else:
        data_used.iloc[0,4]=0
        data_used.iloc[0,5]=1
#    print(data_used)
    predict_outcome = model.predict_proba(data_used)[:,1]
    if predict_outcome<0.245:
        print("Congratulation, you might not have ILD.")
    else:
        print("Sorry, you might have ILD.")