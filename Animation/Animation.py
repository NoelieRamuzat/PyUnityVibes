import numpy as np

class Animation(object):

    def __init__(self, dt):
        self.dictObject = {}
        self.dictObject[dt] = dt

    def addObject(self, unityObject, position = np.array([[],[],[]]), rotation = np.array([[],[],[]])):
        assert position.shape[0] == 3 and rotation.shape[0] == 3, "Wrong size of translation and/or rotation array. Must be (3, n)"
        self.dictObject[unityObject.id] = np.vstack((position, rotation))

    def appendPosition(self, unityObject, position = np.array([[],[],[]]), rotation = np.array([[],[],[]])):
        assert position.shape[0] == 3 and rotation.shape[0] == 3, "Wrong size of translation and/or rotation array. Must be (3, n)"
        addedCol = np.vstack((position, rotation))
        previousMovement = self.dictObject[unityObject]
        self.dictObject[unityObject.id] = np.hstack((previousMovement, addedCol))

    def setTrajectory(self, unityObject, position = np.array([[],[],[]]), rotation = np.array([[],[],[]])):
        assert position.shape[0] == 3 and rotation.shape[0] == 3, "Wrong size of translation and/or rotation array. Must be (3, n)"
        self.dictObject[unityObject.id] = np.vstack((position, rotation))

    def zeroPadding(self, array1, array2):
        if(array1.shape[1] < array2.shape[1]):
            minSize = array1.shape[1]
            maxSize = array2.shape[1]
            zeros   = np.zeros((3, maxSize - minSize))
            array1  = np.hstack((array1, zeros))
        elif(array1.shape[1] > array2.shape[1]):
            minSize = array2.shape[1]
            maxSize = array1.shape[1]
            zeros   = np.zeros((3, maxSize - minSize))
            array2  = np.hstack((array2, zeros))
            
        return array1, array2