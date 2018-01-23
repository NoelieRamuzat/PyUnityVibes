import numpy as np

class Animation(object):

    def __init__(self, dt):
        self.dictObject = {}
        self.dt = dt

    def addObject(self, unityObject, translation = np.array([[],[],[]]), rotation = np.array([[],[],[]])):
        self.dictObject[unityObject.id] = np.vstack((translation, rotation))

    def appendPosition(self, unityObject, position = np.array([[],[],[]]), rotation = np.array([[],[],[]])):
        addedCol = np.vstack((position, rotation))
        previousMovement = self.dictObject[unityObject]
        self.dictObject[unityObject.id] = np.hstack((previousMovement, addedCol))

    def setTrajectory(self, unityObject, translation = np.array([[],[],[]]), rotation = np.array([[],[],[]])):
        self.dictObject[unityObject.id] = np.vstack((translation, rotation))

    def zeroPadding(self, array1, array2):
        pass