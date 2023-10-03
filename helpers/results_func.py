#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.metrics import (
    precision_score, 
    recall_score, 
    f1_score, 
    fbeta_score, 
    roc_auc_score)
import pandas as pd


# In[4]:


def results_printer(X_test, y_test, optimizer, results):
    y_pred = optimizer.best_estimator_.predict(X_test)
    
    clf_name = optimizer.best_estimator_.named_steps.model.__class__.__name__
    f1_test = f1_score(y_test, y_pred)
    recall_test = recall_score(y_test, y_pred)
    precision_test = precision_score(y_test, y_pred)
    y_proba = optimizer.best_estimator_.predict_proba(X_test)[:,1]
    roc_auc_test = roc_auc_score(y_test, y_proba)
    results.append([clf_name, f1_test, recall_test, precision_test, roc_auc_test])
    results_df = pd.DataFrame(results, columns=['best clf name', 'Test F1', 'Test Recall', 'Test Precision', 'Test ROC AUC'])
    return y_proba, roc_auc_test, results_df


# In[ ]:


