#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[33]:
       
        
def city_salary_imputer(X):
    X["City"]= X["City"].fillna("0")
    X["Salary_Account"] = X["Salary_Account"].fillna(0)
    return X
        
        
def tenure_amount_imputer(X):
        
    X["Loan_Tenure_Submitted"] = X["Loan_Tenure_Submitted"].fillna(X['Loan_Tenure_Applied'])
    X["Loan_Amount_Submitted"] = X["Loan_Amount_Submitted"].fillna(X['Loan_Amount_Applied'])
    return X
    
        


# In[ ]:





# In[ ]:




