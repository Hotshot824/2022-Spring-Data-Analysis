## Basic iris method

from operator import index
from os import sep


def saveData(data):
    # fp = open("iris.txt", "w")
    outputpath = "./iris.cvs"
    data.to_csv(outputpath, sep=',')
    # fp.close()