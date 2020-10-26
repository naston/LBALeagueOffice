import socket
import pickle

class Network(object):
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = '10.147.62.245'
        self.port = 5555
        self.addr = (self.server,self.port)
        self.team = self.connect()

    def getTeam(self):
        return self.team

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            #self.client.send(str.encode(data))
            msg=pickle.dumps(data)
            self.client.send(msg)
            return self.client.recv(2048)
        except socket.error as e:
            print(e)