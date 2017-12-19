from Network.Callback import Callback

class UnityObject(object):

    ACTION_DELETE = 'Delete'
    ACTION_UPDATE = 'Update'
    ACTION_GET = 'Get'
    ACTION_TRACKING = 'CameraTracking'

    def __init__(self, figure, id, data):
        self.id = id
        self.figure = figure
        self.data = data
        self.exists = True

    def delete(self):
        self.exists = False
        obj = {
            'id': self.id
        }
        callback = Callback(self.onDeleted, self.ACTION_DELETE, self)
        self.figure.sendAction(self.ACTION_DELETE, obj, callback)

    @staticmethod
    def onDeleted():
        print("Objet supprimé")

    def updatePosition(self, coordX, coordY, coordZ):
        self.data['coordX'] = coordX
        self.data['coordY'] = coordY
        self.data['coordZ'] = coordZ
        callback = Callback(self.onUpdated, self.ACTION_UPDATE, self)
        self.figure.sendAction(self.ACTION_UPDATE, self.data, callback)

    def updateRotation(self, rotX, rotY, rotZ):
        self.data['rotX'] = rotX
        self.data['rotY'] = rotY
        self.data['rotZ'] = rotZ
        callback = Callback(self.onUpdated, self.ACTION_UPDATE, self)
        self.figure.sendAction(self.ACTION_UPDATE, self.data, callback)

    def updateSize(self, dimX, dimY, dimZ):
        self.data['dimX'] = dimX
        self.data['dimY'] = dimY
        self.data['dimZ'] = dimZ
        callback = Callback(self.onUpdated, self.ACTION_UPDATE, self)
        self.figure.sendAction(self.ACTION_UPDATE, self.data, callback)

    def updateColor(self, objectColor):
        self.data['color'] = objectColor.toSting()
        callback = Callback(self.onUpdated, self.ACTION_UPDATE, self)
        self.figure.sendAction(self.ACTION_UPDATE, self.data, callback)

    @staticmethod
    def onUpdated():
        print("Objet mis à jour")

    def getInfo(self):
        obj = {
            'id': self.id
        }
        callback = Callback(self.onGet, self.ACTION_GET, self)
        self.figure.sendAction(self.ACTION_GET, obj, callback)
        return self.data

    def onGet(self, newData):
        print("Informations de l'Objet récupérées")
        self.data = newData

    def track(self):
        obj = {
            'id': self.id
        }
        callback = Callback(self.onTracked, self.ACTION_TRACKING, obj)
        self.figure.sendAction(self.ACTION_TRACKING, obj, callback)

    @staticmethod
    def onTracked():
        print("Objet suivi")
