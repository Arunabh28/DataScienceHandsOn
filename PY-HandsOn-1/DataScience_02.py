# DS Math Hands On
# Libraries:
#   >> Pandas: Read CSV and perform basic aggregation
#   >> MatPlotLib: Plot graphs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def DemoLineGraph(filePath:str):
    health_data = pd.read_csv(filePath, header=0, sep=",")
    health_data.dropna(axis=0,inplace=True)
    health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line'),
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)

    plt.show()

def DemoSlopeIntercept(filePath:str):
    health_data = pd.read_csv(filePath, header=0, sep=",")
    health_data.dropna(axis=0,inplace=True)
    x = health_data["Average_Pulse"].astype(float)
    y = health_data["Calorie_Burnage"]
    slope_intercept = np.polyfit(x,y,1)
    print(slope_intercept)
    #plt.show()   

# DemoLineGraph("D:\Arunabh\Code\PY-HandsOn-1\Data\SampleData1.csv")
DemoSlopeIntercept("D:\Arunabh\Code\PY-HandsOn-1\Data\SampleData1.csv")