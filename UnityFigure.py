from Network.TCPClient import TCPClient
from UI.UnityObject import UnityObject
from Network.Callback import Callback
from UI.Color import Color
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
    OBJECT_3D_DEATHSTAR = 7

    COLOR_RED = Color(255, 0, 0, 255)
    COLOR_GREEN = Color(0, 255, 0, 255)
    COLOR_BLUE = Color(0, 0, 255, 255)
    COLOR_YELLOW = Color(255, 255, 0, 255)
    COLOR_CYAN = Color(0, 255, 255, 255)
    COLOR_PINK = Color(255, 0, 255, 255)
    COLOR_ORANGE = Color(255, 100, 0, 255)
    COLOR_PURPLE = Color(67, 13, 83, 255)
    COLOR_BLACK = Color(0, 0, 0, 255)
    COLOR_WHITE = Color(255, 255, 255, 255)

    def __init__(self, typeFig, background='plane', color='green', dimX=50, dimY=50, dimZ=50):
        self.tcpClient = TCPClient(self.onMessageReceived)  # port
        self.tcpClient.connect()  ##192.168.1.25
        self.msgId = 0
        self.objId = 0
        self.msgCallbacks = {}
        self.init(typeFig, background, color, dimX, dimY, dimZ)

    def init(self, typeFig, background, color, dimX, dimY, dimZ):
        fig = {
            'typeFig': typeFig,
            'background': background,
            'color': color,
            'dimX': dimX,
            'dimY': dimY,
            'dimZ': dimZ
        }
        self.sendAction(self.ACTION_INIT, fig, self.onCreated)

    def create(self, type, coordX, coordY, coordZ, rotX=0, rotY=0, rotZ=0, dimX=1, dimY=1, dimZ=1, color=None):
        if color is None:
            color = [0, 0, 255, 255]
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
            'color': str(color),
            'id': self.objId
        }
        newObj = UnityObject(self, self.objId, obj)
        callback = Callback(self.onCreated, self.ACTION_CREATE, newObj)
        self.sendAction(self.ACTION_CREATE, obj, callback)
        return newObj

    def onCreated(self, id, obj):
        print("Objet créé")
        obj.id = id

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
        self.tcpClient.messageID = message[0]
        try:
            message = message[1].decode("ascii").replace("\\", "")
            print("Received: ", message)
            msg = json.loads(message)

            idObject = msg['content']['id']
            msgId = msg['msgId']
            msgContent = msg['content']
            msgAction = msg['action']
            if msgId in self.msgCallbacks.keys():
                callback = self.msgCallbacks[msgId]
                if msgAction == 'Get':
                    callback.function(msgContent)
                elif msgAction == 'Create':
                    callback.function(idObject, callback.object)
                else:
                    callback.function()
        except Exception as e:
            pass

    def createAnimation(self, dt):
        return Animation(dt)

    def animate(self, animation):
        self.sendAction(self.ACTION_ANIMATION, animation.dictObject)

