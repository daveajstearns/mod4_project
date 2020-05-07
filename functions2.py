def clean_drop(data):
    """Provide data frame in parenthesis and this function will
        drop nulls permanently, and reset the index."""
    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)
    return data

def reset_index(data):
    """Provide data frame in parenthesis and this function will
        reset your index."""
    data.reset_index(drop=True, inplace=True)
    return data

def make_value_chart(data, column, x_label, y_label, title, color='PRGn'):
    """Must fill out all arguments EXCEPT color. Color has a default setting."""
    fig, ax = plt.subplots(figsize=(14,8))
    ax = sns.barplot(x=list(data[column].value_counts().keys()),
     y=data[column].value_counts(), palette=color)    
    ax.set_xticklabels(ax.get_xticklabels(),
                      rotation=45, horizontalalignment='right')
    plt.xlabel(x_label, size=20)
    plt.ylabel(y_label, size=20)
    plt.title(title, size=26)
    return plt.show()

def rename_column(data, column, new_name):
    """Quickly renames columns"""
    data.rename(columns={column: new_name}, inplace=True)
    return data

def drop(data, columns=[]):
    """Quickly drops columns"""
    data.drop(columns=columns, inplace=True)
    return data

def dummy_up(data, column, prefix):
    """Quickly makes dummies for the selected column"""
    new = pd.get_dummies(data[column], prefix=prefix, drop_first=True)
    return new

def factorize(data, column):
    """Factorizes categorical columns to prepare for RandomForestClassifier.  

    Must apply to each column individually."""
    new = pd.factorize(data[column])[0] + 1
    return new

def makeMarker(coordinates, mapp):
    for i in coordinates:
        mark = folium.Marker(i)
        mark.add_to(mapp)

def dftest(data):
    test = adfuller(data['value'])
    test_output = pd.Series(test[0:4], index=['Test Stat', 'P-Value', '# Lags', '# Observations'])
    for key, value in test[4].items():
        test_output['Critical Value (%s)' %key]=value
    return(test_output)

def auto_corrs(data, metro):
    fig, ax = plt.subplots(figsize=(16,3))
    acf = plot_acf(data, ax=ax, lags=48, title=metro+' ACF')
    fig, ax = plt.subplots(figsize=(16,3))
    pacf = plot_pacf(data, ax=ax, lags=48, title=metro+' PACF')
    return acf, pacf

def arima_search(data, ps, ds, qs):
    aic_scores = {}
    rmse_scores ={}
    for p in ps:
        for d in ds:
            for q in qs:
                model = ARIMA(data['1997':'2013'], order=(p,d,q))
                fit = model.fit(disp=0)
                aic_scores[p,d,q] = fit.aic
                avg_vals = []
                for line in list(fit.forecast(52)[2]):
                    avg_vals.append((line[1]+line[0])/2)
                mse = mean_squared_error(data['2014':'2018-04-01'], avg_vals)
                rmse_scores[p,d,q] = math.sqrt(mse)
    return ('Best ARIMA Parameters for AIC: ', min(aic_scores, key=aic_scores.get)), ('Best ARIMA Parameters for RMSE: ', min(rmse_scores, key=rmse_scores.get))

def arima(data, order, metro):
    model = ARIMA(data['1997':'2013'], order)
    fit = model.fit(disp=0)
    print('ARIMA for',metro)
    print(fit.summary())
    residuals = pd.DataFrame(fit.resid)
    residuals.plot(kind='kde', title=metro)
    fit.plot_predict(end='2018-04-01')
    avg_vals = []
    for line in list(fit.forecast(52)[2]):
        avg_vals.append((line[1]+line[0])/2)
    mse = mean_squared_error(data['2014':'2018-04-01'], avg_vals)
    rmse = math.sqrt(mse)
    print('This model can predict the remaining 52 data points with an RMSE of ',rmse)
    print('The following results are predicting values post-data set')
    print('These predictions can only be confirmed with new data')
    avg_2019 = ((fit.forecast(64)[2][-1][1]+fit.forecast(64)[2][-1][0])/2)
    one_year = ((avg_2019-data['value']['2010-04-01'])/data['value']['2010-04-01'])*100
    print('Percent change from 2010-04-1 to 2019-04-01: ',one_year)
    fit.plot_predict(end='2019-04-01')
    avg_2020 = ((fit.forecast(76)[2][-1][1]+fit.forecast(76)[2][-1][0])/2)
    two_year = ((avg_2020-data['value']['2010-04-01'])/data['value']['2010-04-01'])*100
    print('Percent change from 2010-04-1 to 2020-04-01: ',two_year)
    fit.plot_predict(end='2020-04-01')
    avg_2021 = ((fit.forecast(88)[2][-1][1]+fit.forecast(88)[2][-1][0])/2)
    three_year = ((avg_2021-data['value']['2010-04-01'])/data['value']['2010-04-01'])*100
    print('Percent change from 2010-04-1 to 2021-04-01: ',three_year)
    fit.plot_predict(end='2021-04-01')
    avg_2022 = ((fit.forecast(100)[2][-1][1]+fit.forecast(100)[2][-1][0])/2)
    four_year = ((avg_2022-data['value']['2010-04-01'])/data['value']['2010-04-01'])*100
    print('Percent change from 2010-04-1 to 2022-04-01: ',four_year)
    fit.plot_predict(end='2022-04-01')