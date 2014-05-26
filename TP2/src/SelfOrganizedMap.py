import numpy as np
import random
import math
from utils.Utils import Utils
from MatrixVisualizer import MatrixVisualizer
import time
from copy import copy, deepcopy

class SelfOrganizedMap:

    def __init__(self, epochs, alphaEtta, alphaSigma, n, m1, m2):
        self.epochs = epochs
        self.alphaEtta = alphaEtta
        self.alphaSigma = alphaSigma
        self.etta = 0.001 #es correcto inicializarlo con frula?
        self.sigma = 0.01 #es correcto inicializarlo con frula?
        self.n = n
        self.m1 = m1
        self.m2 = m2
        self.matrix = Utils().createRandomMatrix(n, (m1*m2))

    def algorithm(self, dataSet):
        vTest = MatrixVisualizer(self.n, self.m1*self.m2)
        runningEpoch = 1

        while runningEpoch < self.epochs:
            self.updateEtta(runningEpoch)
            self.updateSigma(runningEpoch)

            counter = 0
            for x in dataSet:
                #print counter
                print 'Etta :' + str(self.etta)
                print 'Sigma:' + str(self.sigma)
                counter = counter+1
                visualMatrix  = deepcopy(self.matrix)
                print "learning matrix: " + str(visualMatrix.shape)
                print str(visualMatrix)
                #vTest.visualize(visualMatrix.reshape((self.n,self.m1*self.m2,)))
                vTest.visualize(visualMatrix)

                self.correctWeightMatrix(x)




                time.sleep(0.5)


            runningEpoch += 1

    def updateEtta(self, epoch):
        self.etta = pow(epoch, -(self.alphaEtta))

    def updateSigma(self, epoch):
        self.sigma = pow(epoch, -(self.alphaSigma))

    def correctWeightMatrix(self, x):

        print 'x vector: ' + str(x)
        y = self.activate(x)
        print 'y vector: ' + str(y)
        point = self.winner(y)
        print 'winner: ' + str(point)
        propagationMatrix = self.proxy(point)
        print 'propagationMatrix: ' + str(propagationMatrix.shape)
        print propagationMatrix

        #matrixDifference = Utils().subtractVectorToEachColumnOf(self.matrix, x)
        matrixDifference = Utils().subtractMatrixFromVector(self.matrix, x)


        #flattenPropagationMatrix = propagationMatrix.flatten()
        print 'reshaping propagation matrix to (' + str(self.m1) + '*' + str(self.m2) + ',' + str(1) + ')'
        flattenPropagationMatrix = propagationMatrix.reshape((self.m1*self.m2,1)) # es 1 porque es el vector de propagacion que ira multiplicando a cada fila de la matrix (cada una de las n matrices de m1.m2)
        #flattenPropagationMatrix = propagationMatrix.reshape((self.n, self.m1*self.m2))

        print 'matrixDifference: ' + str(matrixDifference.shape)
        print matrixDifference

        #print 'flattenPropagationMatrix: ' + str(flattenPropagationMatrix.shape)
        #print flattenPropagationMatrix

        deltaMatrix = Utils().multiplyVectorAndMatrix(self.etta * matrixDifference, flattenPropagationMatrix)
        #matrixDifference * flattenPropagationMatrix
        self.matrix = self.matrix + deltaMatrix

        #print self.matrix

    #Devuelve  y (1, m1.m2)
    def activate(self, x):

        matrixDifference = Utils().subtractVectorToEachColumnOf(self.matrix, x)
        #print 'MatrixDifference: ' + str(matrixDifference)
        vectorOfNorms = Utils().applyNormToEachColumn(matrixDifference)
        #print 'vectorOfNorms: ' + str(vectorOfNorms)

        maskedVector = Utils().applyMaskForMinimumOn(vectorOfNorms)
        #print 'maskedVector: ' + str(maskedVector)

        return maskedVector

    def proxy(self, winnerPoint): #TODO: correct/check positions!

        gaussMatrix = np.zeros((self.m1, self.m2))
        #print gaussMatrix.shape
        #print 'winnerPoint[0]: ' + str(winnerPoint[0])
        #print 'winnerPoint[1]: ' + str(winnerPoint[1])

        gaussMatrix[winnerPoint[0]][winnerPoint[1]] = 1

        for columnIndex in range(0, gaussMatrix.shape[1]):
            for rowIndex in range(0, gaussMatrix.shape[0]):
                gaussMatrix[rowIndex][columnIndex] = self.gaussianFormula((rowIndex,columnIndex), winnerPoint)
        return gaussMatrix

    def gaussianFormula(self, point, winnerPoint):
        pointDifference = np.subtract(point, winnerPoint)
        squaredNorm = Utils().sumSquaredNorm(pointDifference)
        squaredSigma = math.pow(self.sigma, 2)
        coefficient = (-squaredNorm)/squaredSigma
        return math.pow(math.e, coefficient)


    # y: 1,m1 x m2
    def winner(self, y):
        for j in range(0, self.m2):
            for i in range(0, self.m1):
                if y[(self.m1*j)+i] == 1:
                    return (i, j)


    def winnerINverted(self, y):
        for j in range(0, self.m1):
            for i in range(0, self.m2):
                if y[(self.m2*j)+i] == 1:
                    return (i, j)



