import socket
from threading import Thread


class TCPClient(Thread):

    def __init__(self, onMessageReceived):
        super(TCPClient, self).__init__()
        self.port = 29200
        self.started = False
        self.onMessageReceived = onMessageReceived
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    def connect(self, ip="localhost"):
        try:
            self.socket.connect((ip, self.port))
            self.started = True
            self.start()
        except Exception as e:
            print(e)
            raise Exception("Unable to connect to Unity, please make sure that the viewer is started.")

    def end(self):
        self.started = False
        self.socket.close()

    def sendMessage(self, message):
        self.socket.sendall((message + "\n").encode())

    def run(self):
        while self.started:
            try:
                message = self.socket.recv(511)
                if message != b'':
                    self.onMessageReceived(message)
            except Exception as e:
                print("Error receiving message: ", e)
                self.end()



