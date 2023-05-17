# the code to run the OLS model
# Note that this function relies on the code from OSL_GWR.ipynb

import pysal
import pandas as pd
import numpy as np

# OLS regression
def run_OLS (g_X, g_y, wq, list_x_var):
    ols = pysal.model.spreg.OLS(g_y, g_X, w = wq, 
                            spat_diag=True,
                            moran=True,
                            name_y='vaccine_uptake',
                            name_x=list_x_var,
                            name_ds='England', 
                            white_test=True)

    # summary of OLS
    df_ols_summary = pd.DataFrame({'AIC':[ols.aic], 'Adj_R2':[ols.ar2], 'RSS':[ols.utu], 'Log-likelihood':[ols.logll]})
    display(df_ols_summary)

    df_ols_result =pd.DataFrame({'Variable': ols.name_x, 'Coefficient' : ols.betas.flatten(),'Std.Error':ols.std_err.flatten(), 't-Statistic':[x[0] for x in ols.t_stat], 
                               'p-value':[x[1] for x in ols.t_stat]})
    # vif
    vif_ols = pysal.model.spreg.vif(ols)
    vif_ols[0] = (np.nan, np.nan)
    df_ols_result['VIF'] = [x[0] for x in vif_ols]
    display(df_ols_result)
    return ols

def model_summary (model):
    # summary of OLS/GWR/MGWR
    return pd.DataFrame({'AIC':[model.aic], 'Adj_R2':[model.ar2], 'RSS':[model.utu], 'Log-likelihood':[model.logll]})

    