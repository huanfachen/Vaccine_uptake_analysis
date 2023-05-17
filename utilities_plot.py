import matplotlib.pyplot as plt
from matplotlib import colors

def plot_car_income_access_imd_coef(gdf_gwr_result):
    f,ax=plt.subplots(2,2,figsize=(12,6), subplot_kw=dict(aspect='equal'))
    # Flatten them
    ax = ax.flatten()
    # Define the title of our plots and the variables to plot
    titles = ['pct_hh_car', 'average_household_income', 'accessibility_vaccine', 'msoa_quintile']
    labels = ['(a) %households owning cars', '(b) Average household income', '(c) Accessiblity score to vaccine', '(d) IMD quintile (1-5)']

    # Here, we are creating loop for our parameter estimates 
    # grey means coef of 0
    for i,(var,label) in enumerate(zip(titles, labels)):
        # We want to plot all the non-significant estimates in grey
        ct_temp = gdf_gwr_result.assign(toplot=gdf_gwr_result[var])
        (ct_temp.query('toplot==0')
         .sort_values('toplot')
         .plot(color='grey',ax=ax[i],alpha=.2))
        # and assign colours only to the significant estimates
        (ct_temp.query('toplot!=0')
         .sort_values('toplot')
         .plot('toplot',
               cmap='plasma',
               ax=ax[i],
               legend=True, 
    #            title=label
              )
        )

        ax[i].set_title(label, fontsize=16)

        ax[i].set_xticklabels([])
        ax[i].set_yticklabels([])
        ax[i].set_xticks([])
        ax[i].set_yticks([])

    f.tight_layout()

def plot_age_group_coef(gdf_gwr_result, b_same_value_range = True):
    f,ax=plt.subplots(2,3,figsize=(12,6), subplot_kw=dict(aspect='equal'))
    # Flatten them
    ax = ax.flatten()
    # Define the title of our plots and the variables to plot
    titles = ['pct_pop_18_29', 'pct_pop_40_49','pct_pop_50_59', 'pct_pop_60_69', 'pct_pop_70_80', 'pct_pop_80_over']
    labels = ['(a) % 18-29', '(b) % 40-49','(c) % 50-59', '(d) % 60-69', '(e) % 70-80', '(f) % 80-over']

    # set both vmin and vmax as None.
    vmin_global, vmax_global = None, None

    # if b_same_value_range is True, then calculate the global min and max
    if b_same_value_range is True:
        vmin_global = gdf_gwr_result[titles].min().min()
        vmax_global = gdf_gwr_result[titles].max().max()
        if (vmin_global * vmax_global) < 0:
            divnorm=colors.TwoSlopeNorm(vmin=vmin_global, vcenter=0, vmax=vmax_global)
        else:
            divnorm=colors.TwoSlopeNorm(vmin=vmin_global, vmax=vmax_global, vcenter = (vmin_global+vmax_global)/2.0)
    else:
        divnorm = None
        
    print(vmin_global)
    print(vmax_global)
        
    # Here, we are creating loop for our parameter estimates 
    for i,(var,label) in enumerate(zip(titles, labels)):
        # We want to plot all the non-significant estimates in grey
        ct_temp = gdf_gwr_result.assign(toplot=gdf_gwr_result[var])
        (ct_temp.query('toplot==0')
         .sort_values('toplot')
         .plot(color='grey',ax=ax[i],alpha=.2))
        # and assign colours only to the significant estimates
        (ct_temp.query('toplot!=0')
         .sort_values('toplot')
         .plot('toplot',
#                cmap='plasma',
               cmap='bwr', 
               norm=divnorm,
               ax=ax[i],
#                vmin = vmin_global,
#                vmax = vmax_global,
               legend=True,
              )
        )

        ax[i].set_title(label, fontsize=16)

        ax[i].set_xticklabels([])
        ax[i].set_yticklabels([])
        ax[i].set_xticks([])
        ax[i].set_yticks([])

    f.tight_layout()
    # plt.show()
    # plt.savefig('../Images/GWR_coef_ethnic_mixed_asian_black_other.png', bbox_inches='tight')
    
def plot_ethnic_coef(gdf_gwr_result, b_same_value_range = True):
    f,ax=plt.subplots(2,2,figsize=(12,6), subplot_kw=dict(aspect='equal'))
    # Flatten them
    ax = ax.flatten()
    # Define the title of our plots
    titles = [
    #     'pct_hh_car',
     'pct_Mixed',
     'pct_Asian',
     'pct_black',
     'pct_other']

    labels = [
    #     'pct_hh_car',
     '% Mixed',
     '% Asian',
     '% Black',
     '% Other']

    # set both vmin and vmax as None.
    vmin_global, vmax_global = None, None

    # if b_same_value_range is True, then calculate the global min and max
    if b_same_value_range is True:
        vmin_global = gdf_gwr_result[titles].min().min()
        vmax_global = gdf_gwr_result[titles].max().max()
    #     list_min = []
    #     list_max = []
    #     # get vmin and vmax
    #     for var in titles:
    #         list_min.append(np.min(gdf_gwr_result[var]))
    #         list_max.append(np.max(gdf_gwr_result[var]))

    #     vmin_global = np.min(list_min)
    #     vmax_global = np.max(list_max)

    print(vmin_global)
    print(vmax_global)

    # Here, we are creating loop for our parameter estimates 
    for i,(var,label) in enumerate(zip(titles, labels)):
        # We want to plot all the non-significant estimates in grey
        ct_temp = gdf_gwr_result.assign(toplot=gdf_gwr_result[var])
        (ct_temp.query('toplot==0')
         .sort_values('toplot')
         .plot(color='grey',ax=ax[i],alpha=.2))
        # and assign colours only to the significant estimates
        (ct_temp.query('toplot!=0')
         .sort_values('toplot')
         .plot('toplot',
               cmap='plasma',
               ax=ax[i],
               vmin = vmin_global,
               vmax = vmax_global,
               legend=True,
              )
        )

        ax[i].set_title(label, fontsize=16)

        ax[i].set_xticklabels([])
        ax[i].set_yticklabels([])
        ax[i].set_xticks([])
        ax[i].set_yticks([])

    f.tight_layout()
    # plt.show()
    # plt.savefig('../Images/GWR_coef_ethnic_mixed_asian_black_other.png', bbox_inches='tight')