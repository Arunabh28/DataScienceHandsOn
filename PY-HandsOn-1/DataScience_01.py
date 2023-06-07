import pandas as pd
import numpy as np

def DemoPandaDataFrame():
    d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
    df = pd.DataFrame(data=d)
    print(df)

def DemoNumPyMean():
    Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
    Average_calorie_burnage = np.mean(Calorie_burnage)
    print(Average_calorie_burnage)

def DemoPandaReadCSV(filePath:str):
    health_data = pd.read_csv(filePath, header=0, sep=",")
    print(health_data)

def DemoPandaReadCSVTopN(filePath:str,topN:int):
    health_data = pd.read_csv(filePath, header=0, sep=",")
    print(health_data.head(topN))

def DemoPandaCleanseCSV(filePath:str):
    health_data = pd.read_csv(filePath, header=0, sep=",")
    #Clean NAN records
    health_data.dropna(axis=0,inplace=True)

    print (health_data)
    #Display info of the columns
    print(health_data.info())
    #Describe the CSV Data
    print(health_data.describe())

# DemoPandaDataFrame()
# DemoNumPyMean()
# DemoPandaReadCSV("D:\Arunabh\Code\PY-HandsOn-1\Data\SampleData1.csv")
# DemoPandaReadCSVTopN("D:\Arunabh\Code\PY-HandsOn-1\Data\SampleData1.csv",5)
DemoPandaCleanseCSV("D:\Arunabh\Code\PY-HandsOn-1\Data\SampleData1.csv")