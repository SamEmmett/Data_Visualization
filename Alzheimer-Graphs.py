import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


def setup():
    data = pd.read_csv('https://data.cdc.gov/api/views/hfr9-rurv/rows.csv?accessType=DOWNLOAD', dtype=str, header = None)
    data.columns = ['RowId','YearStart','YearEnd','LocationAbbr','LocationDesc','Datasource','Class','Topic','Question','Response','Data_Value_Unit','DataValueTypeID','Data_Value_Type','Data_Value','Data_Value_Alt','Data_Value_Footnote_Symbol','Data_Value_Footnote','Low_Confidence_Limit','High_Confidence_Limit','Sample_Size','StratificationCategory1','Stratification1','StratificationCategory2','Stratification2','StratificationCategory3','Stratification3','Geolocation','ClassID','TopicID','QuestionID','ResponseID','LocationID','StratificationCategoryID1','StratificationID1','StratificationCategoryID2','StratificationID2','StratificationCategoryID3','StratificationID3','Report']
    data = data.drop(labels=0, axis=0) #drops row 0 since that is just the header row
    data = data.drop(labels='RowId', axis=1) #Drop RowID since all are NaN
    data = data.loc[(data['Class'] == 'Cognitive Decline')] #Trunkates the dataframe to only contain data that is relavent to us

    return data

def support(data):
    dataMod = list(data["LocationDesc"].apply(lambda x:x.split(",") ))
    a = TransactionEncoder()
    a_data = a.fit(dataMod).transform(dataMod)
    df = pd.DataFrame(a_data,columns=a.columns_)
    df = apriori(df, min_support = 0.02, use_colnames = True, verbose = 1)
    df_ar = association_rules(df, metric = "confidence", min_threshold = 0.000000001)
    print(df)
    print(df_ar)

def visualizeAge(data): #visualizes age groups
    splitdata = data.copy()
    fig, ax = plt.subplots()
    splitdata['Stratification1'].value_counts().plot(ax=ax, kind = 'bar')
    plt.ylim([6000, 6700])
    plt.show()


def startToVal(data):
    xVal = list(data['YearEnd'])
    yVal = list(data['Data_Value'])
    
    subFrame = {'YearEnd': xVal, 'Data_Value': yVal}
    df = pd.DataFrame(subFrame)
    df = df.dropna()
    df['YearEnd'] = df['YearEnd'].astype(int)
    df['Data_Value'] = df['Data_Value'].astype(float)
    df = df.sample(frac=0.01, replace=False, random_state=1)
    df = df.sort_values(by = ['YearEnd'])
    df.plot.scatter(x='YearEnd', y='Data_Value', color = 'red')
    plt.show()

def startToVal2(data):
    xVal = list(data['YearEnd'])
    yVal = list(data['Data_Value'])
    
    subFrame = {'YearEnd': xVal, 'Data_Value': yVal}
    df = pd.DataFrame(subFrame)
    df = df.dropna()
    df['YearEnd'] = df['YearEnd'].astype(int)
    df['Data_Value'] = df['Data_Value'].astype(float)
    df = df.sample(frac=0.02, replace=False, random_state=1)
    df = df.sort_values(by = ['YearEnd'])
    df.plot.scatter(x='YearEnd', y='Data_Value', color = 'red')
    plt.show()
if __name__ == '__main__': 
    
    #Recommend and line chart for start time on X and Data Value for Y

    data = setup()
    
    visualizeAge(data)
    startToVal(data)
    startToVal2(data)
