from Network.TCPClient import TCPClient
from UI.UnityObject import UnityObject
from Network.Callback import Callback
from Animation.Animation import Animation
import json

class UnityFigure(object):

    FIGURE_3D = '3D'
    FIGURE_2D = '2D'

    ACTION_INIT = 'Init'
    ACTION_CREATE = 'Create'
    ACTION_ANIMATION = 'Animation'

    OBJECT_3D_PLANE = 0
    OBJECT_3D_CUBE = 1
    OBJECT_3D_SPHERE = 2
    OBJECT_3D_CAPSULE = 3
    OBJECT_3D_CYLINDER = 4
    OBJECT_3D_BOAT = 5
    OBJECT_3D_SUBMARINE = 6
    OBJECT_3D_GALLEON = 7

    COLOR_RED = "RED"
    COLOR_GREEN = "GREEN"
    COLOR_BLUE = "BLUE"
    COLOR_YELLOW = "YELLOW"
    COLOR_CYAN = "CYAN"
    COLOR_MAGENTA = "MAGENTA"
    COLOR_GREY = "GREY"
    COLOR_BLACK = "BLACK"
    COLOR_WHITE = "WHITE"

    def __init__(self, typeFig, dimX=50, dimY=50, dimZ=50):
        self.tcpClient = TCPClient(self.onMessageReceived)  # port
        self.tcpClient.connect()  ##192.168.1.25
        self.msgId = 0
        self.objId = 0
        self.msgCallbacks = {}
        self.init(typeFig, dimX, dimY, dimZ)

    def init(self, typeFig, dimX, dimY, dimZ):
        fig = {
            'typeFig': typeFig,
            'dimX': dimX,
            'dimY': dimY,
            'dimZ': dimZ
        }
        self.sendAction(self.ACTION_INIT, fig, self.onCreated)

    def create(self, type, coordX, coordY, coordZ, rotX=0, rotY=0, rotZ=0, dimX=1, dimY=1, dimZ=1, color=""):
        self.objId += 1
        obj = {
            'type': type,
            'coordX': coordX,
            'coordY': coordY,
            'coordZ': coordZ,
            'rotX': rotX,
            'rotY': rotY,
            'rotZ': rotZ,
            'dimX': dimX,
            'dimY': dimY,
            'dimZ': dimZ,
            'color': color,
            'id': self.objId
        }
        newObj = UnityObject(self, self.objId, obj)
        callback = Callback(self.onCreated, self.ACTION_CREATE, newObj)
        self.sendAction(self.ACTION_CREATE, obj, callback)
        return newObj

    def onCreated(self, id, obj):
        obj.id = id
        print(str(obj.type) + " " + str(obj.id) + " created")

    def sendAction(self, action, content, callback = None):
        obj = {
            'action': action,
            'content': str(content).replace("'", "\""),
            'msgId': self.msgId
        }
        json_str = json.dumps(obj)
        self.tcpClient.sendMessage(json_str)
        if callback is not None:
            self.msgCallbacks[self.msgId] = callback
        self.msgId += 1

    def onMessageReceived(self, message):
        message = message.decode("ascii").replace("\\", "").replace("(Object3D)", "")
        msg = json.loads(message)
        try:
            self.tcpClient.messageID = msg['msgId']
            msgId = self.tcpClient.messageID
            idObject = msg['objId']
            msgAction = msg['action']

            if msgId in self.msgCallbacks.keys():
                callback = self.msgCallbacks[msgId]
                callback.object.type = msg['type']
                if msgAction == 'Get':
                    msgContentObj = msg['contentObj']
                    callback.function(callback.object, msgContentObj)
                elif msgAction == 'Create':
                    callback.function(idObject, callback.object)
                else:
                    callback.function(callback.object)
        except Exception as e:
           pass

    def createAnimation(self, dt):
        return Animation(dt)

    def animate(self, animation):
        self.sendAction(self.ACTION_ANIMATION, animation.dictObject)

