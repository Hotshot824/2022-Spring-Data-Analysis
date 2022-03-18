## Basic iris method

from operator import index
from os import sep


def saveData(data):
    # fp = open("iris.txt", "w")
    outputpath = "./iris.txt"
    data.to_csv(outputpath, sep='\t')
    # fp.close()