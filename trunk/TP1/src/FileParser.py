#from LearningData import LearningData
from LearningDataSet import LearningDataSet
import sys

class FileParser:

    def __init__(self, inputFileName, outputFileName):
        self.inputFileName  = inputFileName
        self.outputFileName = outputFileName
 
    def parseInputFile(self):
        inputFile = open(self.inputFileName, 'r')

        firstLine = inputFile.readline()
        objectiveDescription = firstLine.lstrip("name=").strip()
        print "objective description: " + objectiveDescription
        
        secondLine = inputFile.readline()
        etta = secondLine.lstrip("etta=").strip()
        print "etta: " + etta
        
        thirdLine = inputFile.readline()
        epsilon = thirdLine.lstrip("epsilon=").strip()
        print "epsilon: " + epsilon
        
        fourthLine = inputFile.readline()
        epochs = fourthLine.lstrip("epochs=").strip()
        print "epochs: " + epochs
 
        learningDataSet = LearningDataSet(objectiveDescription, int(epochs), float(epsilon), float(etta))
        
        for line in inputFile.readlines():
            setLine = line.lstrip("set").strip()
            splittedSetLine = setLine.split("=")
            
            input = splittedSetLine[0].strip()
            expectedOutput = splittedSetLine[1].strip()
            
            learningDataSet.addLearningData(input, expectedOutput)
        
        inputFile.close()
        return learningDataSet
   
    def save(self, learningInformation):
        print 'this should be implemented'