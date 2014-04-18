import matplotlib.pyplot as plotter
from datetime import datetime
from datetime import time

class Plotter:
    def __init__(self, errorFileName, validationFileName):
        self.errorFileName  = errorFileName
        self.validationFileName = validationFileName

        
    def plotError(self, information):
        fileName = self.errorFileName + ' - ' + self.getNow() + '.png'
        print 'saving on: ' + fileName
        #self.printOnConsole(information)
        
        plotter.plot(information.x, information.y)
        plotter.ylabel(information.yLabel)
        plotter.xlabel(information.xLabel)
        plotter.title(information.title)
        
        plotter.savefig(fileName)
        plotter.show()
    
    def getNow(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")
        '''
        now = datetime.now()
        return str(time(now.hour, now.minute, now.second))
        '''
    
    def printOnConsole(self, information):
        print 'Printing error:'
        print 'X: ' + str(information.x)
        print 'Y: ' + str(information.y)