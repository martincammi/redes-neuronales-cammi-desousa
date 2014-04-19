import sys
import numpy as np
import math
import random
from TrainingInformation import *

class SimplePerceptron: 

    def __init__(self, parameters):
        self.parameters = parameters
        m = parameters.getMDimension()
        n = parameters.getNDimension()
        print 'n: ' + str(n)
        print 'm: ' + str(m)
        self.matrix = self.createRandomMatrix(n,m)
        print 'whole learning matrix: ' + str(self.matrix)
        self.errorInformation = ErrorInformation([],[], self.parameters.objective, parameters.etta)
        self.counter = 0
        
    def createRandomMatrix(self, n, m):
        matrix = np.zeros((n,m)) 
        COLUMN = 0
        ROW = 1
        for columnIndex in range(0, matrix.shape[COLUMN]):
            for rowIndex in range(0, matrix.shape[ROW]):
                matrix[columnIndex][rowIndex] = random.uniform(-0.1, 0.1)
        return matrix
        
    def train(self):
        epsilonOnIteration = 1000
        iteratedEpochs = 0
        
        while epsilonOnIteration > self.parameters.epsilon and iteratedEpochs < self.parameters.epochs:
            shuffledLearningDatas = self.parameters.getShuffledData() #ver si no nos conviene hacer las prueba sin el shuffle
            
            iterationErrors = []
            for learningData in shuffledLearningDatas:
                evaluationVector = self.applySignFunction(learningData.input, self.matrix)
                iterationError = np.subtract(learningData.expectedOutput, evaluationVector)
                iterationErrors.append(iterationError)
                
                #---> Line below does: 
                #---- etta * ( learninData.input.transpose() x iterationerror ) *gprima /en nuestro caso no va xq la derivada es 1
                transposeInput = np.matrix(learningData.input).transpose()
                iterationErrorMatrix = np.matrix(iterationError)
                deltaMatrix = np.dot(self.parameters.etta, np.dot(transposeInput, iterationErrorMatrix)) 
                self.matrix = np.add(self.matrix,deltaMatrix) #algoritmo incremental
            
            '''
            print 'iteration errors on epoch: ' + str(iteratedEpochs)
            print iterationErrors
            '''
            epsilonOnIteration = self.sumSquaredNorms(iterationErrors)
            self.saveIterationError(iteratedEpochs, epsilonOnIteration)
            iteratedEpochs += 1
            
    def saveIterationError(self, epochs, epsilon):
        self.errorInformation.add(epochs, epsilon)
        #print en pantalla de lo que esta pasando
        self.testWhatWasLearnt(epochs, epsilon)
            
    def getTrainingInformation(self):
        validationInformation = ValidationInformation(None, None, 'Completar') #completar
        return TrainingInformation(self.errorInformation, validationInformation)
        
    def sumSquaredNorms(self, errors):
        return sum([self.squaredNorm(e) for e in errors]) / 2
        
    def squaredNorm(self, vector):
        potVector = [math.pow(v,2) for v in vector]
        return sum(potVector)
        
    def applySignFunction(self, vector, matrix): 
        #el vector se lo multiplica por cada vector columna de la matrix 
        #y luego se le aplica la funcion signo
        
        columnsAsRows = matrix.transpose() #es un truquito para poder agarrar rapido las columnas, no se si se puede hacer de otra forma mas eficiente
        vectorDotMatrix = []

        for columnIndex in range(0, columnsAsRows.shape[0]):
            matrixVector = columnsAsRows[columnIndex].transpose()
            vectorialProduct = np.dot(vector, matrixVector)
            vectorDotMatrix.append(vectorialProduct.flat[0])

        return [self.identity(acum) for acum in vectorDotMatrix] #cambiar dsp!
        #return [self.sign(acum) for acum in vectorDotMatrix]
    
    def identity(self, value):
        return value
    
    def sign(self, value):
        if value >= 0:
            return 1.0
        return -1.0
        
    def testWhatWasLearnt(self, iteratedEpochs, iterationEpsilon):
        print '--------------'
        #''' Used for debugging
        print 'Epoch: ' + str(iteratedEpochs)
        print 'Epsilon: '+ str(iterationEpsilon)
        for learningData in self.parameters.learningSet:
            obtainedVector = np.dot(learningData.input, self.matrix)
            print 'input: ' + str(learningData.input)
            print str(learningData.expectedOutput) + ' --> expected'
            print str(obtainedVector) + ' --> obtained'
            print '--------------'
        #'''    
        
    def showEvolution(self):
        print 'matrix evolution, counter: ' + str(self.counter)
        print self.matrix
        self.counter+=1        
