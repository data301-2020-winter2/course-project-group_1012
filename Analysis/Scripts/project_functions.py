def load_and_process(url_or_path_to_csv_file):
    # Method Chain 1 (Load data, deal with missing data, and making data readable)
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns ={"LOCAL_DATE":"DATE"})
        .sort_values("DATE", ascending=False)
        .dropna()
        .reset_index(drop = True)
         )
    return df1

#Method Chain 2 (Creating new columns for different regions of Canada)
def group_columns(df):
    df2 = (
        df
        #convert Date to Datetime 
        .assign(DATE = pd.to_datetime(df1['DATE']))
        #create new columns that take mean temperature and percipitation from Atlantic Provinces 
        .assign(TEMPERATURE_ATLANTIC = (df.iloc[:, [5, 7, 17]].mean(axis=1)).round(decimals=1))
        .assign(PERCIPITATION_ATLANTIC = (df.iloc[:, [6, 8, 18]].mean(axis=1)).round(decimals=1))
        
        #create new columns that take mean temperature and percipitation from Prairie provinces 
        .assign(TEMPERATURE_PRAIRIES = (df.iloc[:, [1, 3, 15, 25]].mean(axis=1)).round(decimals=1))
        .assign(PERCIPITATION_PRAIRIES = (df.iloc[:, [2, 4, 16, 26]].mean(axis=1)).round(decimals=1))
        
        #create new columns that take mean temperature and percipitation from cities in Ontario and merge into single column
        .assign(TEMPERATURE_ONTARIO = (df.iloc[:, [11, 19]].mean(axis=1)).round(decimals=1))
        .assign(PERCIPITATION_ONTARIO = (df.iloc[:, [12, 20]].mean(axis=1)).round(decimals=1))
        
         #create new columns that take mean temperature and percipitation from cities in Quebec and merge into single column
        .assign(TEMPERATURE_QUEBEC = (df.iloc[:, [9, 13]].mean(axis=1)).round(decimals=1))
        .assign(PERCIPITATION_QUEBEC = (df.iloc[:, [10, 14]].mean(axis=1)).round(decimals=1))
        
        #dropping columns that were amalgimated into the means
        .drop(columns = ['MEAN_TEMPERATURE_CALGARY', 'TOTAL_PRECIPITATION_CALGARY', 'MEAN_TEMPERATURE_EDMONTON', 'TOTAL_PRECIPITATION_EDMONTON', 
                         'MEAN_TEMPERATURE_HALIFAX', 'TOTAL_PRECIPITATION_HALIFAX', 'MEAN_TEMPERATURE_MONCTON', 'TOTAL_PRECIPITATION_MONCTON',
                        'MEAN_TEMPERATURE_SASKATOON', 'TOTAL_PRECIPITATION_SASKATOON', 'MEAN_TEMPERATURE_STJOHNS', 'TOTAL_PRECIPITATION_STJOHNS',
                        'MEAN_TEMPERATURE_WINNIPEG', 'TOTAL_PRECIPITATION_WINNIPEG', 'MEAN_TEMPERATURE_OTTAWA', 'TOTAL_PRECIPITATION_OTTAWA',
                        'MEAN_TEMPERATURE_TORONTO', 'TOTAL_PRECIPITATION_TORONTO', 'MEAN_TEMPERATURE_MONTREAL', 'TOTAL_PRECIPITATION_MONTREAL',
                        'MEAN_TEMPERATURE_QUEBEC', 'TOTAL_PRECIPITATION_QUEBEC'])
        
        #renaming columns to meet new location based naming
        .rename(columns ={"MEAN_TEMPERATURE_VANCOUVER":"TEMPERATURE_BRITISH_COLUMBIA"})
        .rename(columns ={"TOTAL_PRECIPITATION_VANCOUVER":"PRECIPITATION_BRITISH_COLUMBIA"})
        .rename(columns ={"MEAN_TEMPERATURE_WHITEHORSE":"TEMPERATURE_NORTHERN"})
        .rename(columns ={"TOTAL_PRECIPITATION_WHITEHORSE":"PRECIPITATION_NORTHERN"})
    )
        
    return df2