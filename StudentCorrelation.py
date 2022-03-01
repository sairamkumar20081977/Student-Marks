import numpy as np
import csv
import plotly.express as px

def plotFigure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Marks",y="Days")
        fig.show() 

def getDataSource(data_path):
    Marks_In_Percentage=[]
    Days_Present=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks"]))
            Days_Present.append(float(row["Days"]))
    return{"x":Marks_In_Percentage,"y":Days_Present}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("correlation value is:",correlation[0,1])
    
def setup():
    data_path="./StudentMarks.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()