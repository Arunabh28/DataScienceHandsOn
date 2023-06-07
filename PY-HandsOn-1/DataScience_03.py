import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def DemoPercentile(filePath:str,columnName:str,percentile:float):
    health_data=pd.read_csv(filePath).dropna()
    if columnName in health_data:
        columnData=health_data[columnName].astype(float)
        print(np.percentile(columnData,percentile))
    else:
        print(str.format("Column Name {} does not exists!!",columnName))

def DemoStandardDeviation(filePath:str):
    health_data=pd.read_csv(filePath).dropna().astype(float)
    print("*** Standard Deviation ***")
    print("=======================")
    print(np.std(health_data))

def DemoCoefficientOfVariance(filePath:str):
    health_data=pd.read_csv(filePath).dropna().astype(float)
    print("*** Coefficient of Variance ***")
    print("=======================")
    print(np.std(health_data)/np.mean(health_data)) 

def DemoVariance(filePath:str):
    health_data=pd.read_csv(filePath).dropna().astype(float)
    print("*** Variance ***")
    print("=======================")
    print(np.var(health_data)) 

def DemoCorrelationMatrix(filePath:str):
    health_data=pd.read_csv(filePath).dropna().astype(float)
    print("*** CorrelationMatrix ***")
    print("=======================")
    correlationMatrix=health_data.corr()
    print(correlationMatrix)  
    DemoHeatMapUsingSeaBorn(correlationMatrix)

def DemoHeatMapUsingSeaBorn(matrixData:any):
    axis_corr = sns.heatmap(
    matrixData,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(0, 500, n=500),
    square=True
    )

    plt.show()

sampleFileName="D:\Arunabh\Code\PY-HandsOn-1\Data\SampleData1.csv"
# DemoPercentile(sampleFileName,"Max_Pulse",10)
# DemoStandardDeviation(sampleFileName)
# DemoCoefficientOfVariance(sampleFileName)
# DemoVariance(sampleFileName)
DemoCorrelationMatrix(sampleFileName)