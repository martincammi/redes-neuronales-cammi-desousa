﻿import sys
import numpy as np
import math
from DataSetCreator import DataSetCreator
from pprint import pprint
import time
from HebbianLearning import HebbianLearning
from conditions.EpochAmountCondition import EpochAmountCondition
from MatrixVisualizer import MatrixVisualizer
import time
from SelfOrganizedMap import SelfOrganizedMap

def main():
    '''
    epochs = 1
    alphaEtta = 1
    alphaSigma = 1
    n = 1
    m1 = 4
    m2 = 5

    map = SelfOrganizedMap(epochs,alphaEtta,alphaSigma,n,m1,m2)
    #map.matrix = np.matrix('1.0 2.0; 3.0 4.0; 5.0 6.0')
    vector = [2,2,2]
    map.activate(vector)
    '''

    '''
    map = SelfOrganizedMap(1,1,1,1,10,7)
    gaussMatrix = map.proxy((4,4))
    visualizer = MatrixVisualizer(10,7)
    visualizer.visualize(gaussMatrix)
    '''

    '''
    #Algorithm parameters
    n = 6
    m = 4
    #etta = 0.00017 --> funciono para sanger
    etta = 0.017
    amountOfRandomSets = 50
    endCondition = EpochAmountCondition()

    dataSetCreator = DataSetCreator(n)
    dataSet = dataSetCreator.getRandomDataSet(amountOfRandomSets)
    pprint(dataSet)
    pprint('boundVector')
    pprint(dataSetCreator.boundVector)

    hebbianLearning = HebbianLearning(n , m, etta, endCondition )
    dataSet = DataSetCreator(n).getRandomDataSet(amountOfRandomSets)
    #time.sleep(2)

    #runHebb(hebbianLearning, dataSet)
    #runOja1(hebbianLearning, dataSet)
    runOjaM(hebbianLearning, dataSet)
    #runSanger(hebbianLearning, dataSet)
    '''

def runHebb(hebbianLearning, dataSet):
    pprint('---Hebb---')
    hebbianLearning.algorithm(dataSet, hebbRule)

def runOja1(hebbianLearning, dataSet):
    pprint('---Oja1---')
    hebbianLearning.algorithm(dataSet, oja1Rule)

def runOjaM(hebbianLearning, dataSet):
    pprint('---runOjaM---')
    hebbianLearning.algorithm(dataSet, ojaMRule)

def runSanger(hebbianLearning, dataSet):
    pprint('---runSanger---')
    hebbianLearning.algorithm(dataSet, sangerRule)

def hebbRule(j, m):
    return 0

def oja1Rule(j, m):
    return 1

def ojaMRule(j, m):
    return m

def sangerRule(j, m):
    return j+1


if __name__ == "__main__":
    main()
