import numpy as np
import random
import math
from utils.Utils import Utils

class SelfOrganizedMap:

    def __init__(self, epochs, alphaEtta, alphaSigma, n, m1, m2):
        self.epochs = epochs
        self.alphaEtta = alphaEtta
        self.alphaSigma = alphaSigma
        self.etta = 1 #es correcto inicializarlo con frula?
        self.sigma = 2 #es correcto inicializarlo con frula?
        self.n = n
        self.m1 = m1
        self.m2 = m2
        self.matrix = Utils().createRandomMatrix(n, (m1*m2))

    def algorithm(self, dataSet):
        runningEpoch = 1

        while runningEpoch < self.epochs:
            self.updateEtta(runningEpoch)
            self.updateSigma(runningEpoch)

            for x in dataSet:
                self.correctWeightMatrix(x)

            runningEpoch += 1

    def updateEtta(self, epoch):
        self.etta = pow(epoch, -(self.alphaEtta))

    def updateSigma(self, epoch):
        self.sigma = pow(epoch, -(self.alphaSigma))

    def correctWeightMatrix(self, x):
        y = self.activate(x)
        point = self.winner(y)
        D = self.proxy(point, self.sigma)
        deltaMatrix = self.etta * (x.transpose - w). flatten(D) #se supone que tiene que dar una matrix
        self.matrix += deltaMatrix

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
        gaussMatrix[winnerPoint[0]][winnerPoint[1]] = 1

        for columnIndex in range(0, gaussMatrix.shape[1]):
            for rowIndex in range(0, gaussMatrix.shape[0]):
                gaussMatrix[columnIndex][rowIndex] = self.gaussianFormula((columnIndex, rowIndex), winnerPoint)
        return gaussMatrix

    def gaussianFormula(self, point, winnerPoint):
        pointDifference = np.subtract(point, winnerPoint)
        squaredNorm = self.sumSquaredNorm(pointDifference)
        squaredSigma = math.pow(self.sigma, 2)
        coefficient = (-squaredNorm)/squaredSigma
        return math.pow(math.e, coefficient)

    # y: 1,m1 x m2
    def winner(self, y):
        for j in range(0, self.m1):
            for i in range(0, self.m2):
                if y[(self.m2*j)+i] == 1:
                    return (i, j)
    '''
    def winnerOriginal(self, y):
        for j in range(0, self.m2):
            for i in range(0, self.m1):
                if y[(self.m1*j)+i] == 1:
                    return (i, j)
    '''


