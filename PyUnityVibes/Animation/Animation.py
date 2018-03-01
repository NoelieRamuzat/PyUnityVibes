import numpy as np


class Animation(object):

    def __init__(self, dt):
        self.dt = dt
        self.dictObject = dict()

    def getAnimationDict(self):
        animationDict = dict()
        for key in self.dictObject.keys():
            animationDict[key] = self.dictObject[key].T.tolist()
        return { "dt": self.dt, "frames": animationDict }

    def addObject(self, unityObject, position = np.array([[],[],[]]), rotation = np.array([[],[],[]])):
        assert position.shape[0] == 3 and rotation.shape[0] == 3, "Wrong size of translation and/or rotation array. Must be (3, n)"
        self.dictObject[unityObject.id] = np.vstack((position, rotation))

    def appendFrame(self, unityObject, x=0, y=0, z=0, rx=0, ry=0, rz=0):
        addedCol = np.hstack((np.array([x, y, z]), np.array([rx, ry, rz])))
        previousMovement = self.dictObject[unityObject.id]
        self.dictObject[unityObject.id] = np.hstack((previousMovement, addedCol.reshape(6, 1)))

    def setTrajectory(self, unityObject, position = np.array([[],[],[]]), rotation = np.array([[],[],[]])):
        assert position.shape[0] == 3 and rotation.shape[0] == 3, "Wrong size of translation and/or rotation array. Must be (3, n)"
        position, rotation = self.zeroPadding(position, rotation)
        self.dictObject[unityObject.id] = np.vstack((position, rotation))

    @staticmethod
    def zeroPadding(array1, array2):
        if array1.shape[1] < array2.shape[1]:
            minSize = array1.shape[1]
            maxSize = array2.shape[1]
            zeros = np.zeros((3, maxSize - minSize))
            array1 = np.hstack((array1, zeros))
        elif array1.shape[1] > array2.shape[1]:
            minSize = array2.shape[1]
            maxSize = array1.shape[1]
            zeros = np.zeros((3, maxSize - minSize))
            array2 = np.hstack((array2, zeros))
        return array1, array2
