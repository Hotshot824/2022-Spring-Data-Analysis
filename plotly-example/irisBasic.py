## Basic iris method

import plotly.express as px

from operator import index
from os import sep

df = px.data.iris()

def saveData(data):
    outputpath = "./iris.cvs"
    data.to_csv(outputpath, sep=',')

def BaseScatter():
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig.show()

def trendlines():
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin", marginal_x="box", trendline="ols", template="simple_white")
    fig.show()