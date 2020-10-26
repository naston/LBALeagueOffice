import socket
from _thread import *
import sys
import pickle
from Message import testMessageOn

currentPlayer=0
server = '10.147.62.245'
port = 5555

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)

s.listen(2)
print('Server Started')

def createMessage(pageType,bg):
    return str(pageType)+','+bg

def onConnect(pageType):
    return str(pageType)

def readMessage(message):
    #message = message.split(',')
    #return message[0],message[1]
    msg=pickle.loads(message)
    return msg

change=False
page=[0,2]
color = ['white']
def threaded_client(conn,player):
    #print(player)
    conn.send(str.encode(onConnect(page[player])))
    #reply = ''
    while True:
        try:
            #change=False
            data = readMessage(conn.recv(2048))
            #print('recieved message')
            pageType=data.getPage()
            bg=data.getColor()
            if pageType==1:
                page[player]=pageType
            #print(pageType)

            if not data:
                print('Disconnected')
                currentPlayer-=1
                break
            else:
                if pageType==0:
                    pass
                    #if bg != color[0]:
                        #change=True
                    
                if page[player]==1:
                    color[0]=bg
                    page[player]=2
                    if player+1>=len(page):
                        page[0]=0
                    else:
                        #print('hit')
                        page[player+1]=0
                

                
                
            #reply = createMessage(page[player],color[0])
            data.setPage(page[player])
            data.setColor(color[0])
            reply=pickle.dumps(data)

            #print('Received: ',bg)
            #print('Sending: ',reply)

            conn.sendall(reply)
        except:
            break
    print('lost connection')
    conn.close()


while True:
    conn, addr=s.accept()
    print('connected to:',addr)

    start_new_thread(threaded_client,(conn,currentPlayer))
    currentPlayer+=1

#can set player+1 to 0 and have an if player+1=len(page)
#Look back through video for subtracting player out to make debug easier pls