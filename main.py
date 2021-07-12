import usocket
from web_page import *
from signal_definitions import *
from ir_tx import *
import machine

print('go')

irPin = machine.Pin(23, machine.Pin.OUT)

ledState = False

sender = Player(irPin)

def handle_request(path):
    global ledState
    path = path.split('GET ')[1].split('HTTP/')[0].strip()[1:]
    path =  path.split('/')
    
    try:
        if path[0] == 'led':
            if path[1] == 'on':
                sendIR(dataOn, 'on')
                ledState = True
            elif path[1] == 'off':
                sendIR(dataOff, 'off')
                ledState = False
            elif path[1] == 'toggle':
                if not ledState:
                    sendIR(dataOn, 'on')
                    ledState = True
                else:
                    sendIR(dataOff, 'off')
                    ledState = False
            elif path[1] == 'status':
                return '{}'.format(ledState)
            elif path[1] == 'red':
                sendIR(dataRed, 'red')
            elif path[1] == 'green':
                sendIR(dataGreen, 'green')
            elif path[1] == 'blue':
                sendIR(dataBlue, 'blue')
            elif path[1] == 'white':
                sendIR(dataWhite, 'white')
            elif path[1] == 'orange':
                sendIR(dataOrange, 'orange')
            elif path[1] == 'teal':
                sendIR(dataTeal, 'teal')
            elif path[1] == 'purple':
                sendIR(dataPurple, 'purple')
            elif path[1] == 'yellow':
                sendIR(dataYellow, 'yellow')
            elif path[1] == 'lightblue':
                sendIR(dataLightblue, 'lightblue')
            elif path[1] == 'hotpink':
                sendIR(dataHotpink, 'hotpink')
            elif path[1] == 'party':
                sendIR(dataParty, 'party woop woop')
            elif path[1] == 'smooth':
                sendIR(dataSmooth, 'smooth')
            elif path[1] == 'smoothrgb':
                sendIR(dataSmoothrgb, 'smooth but less cool')
        if path[0] == 'dbg':
            sendIR(dataOff, 'dbg')
    except IndexError:
        print('index error')
    
    return web_page()

def sendIR(timings, dbgOutput = ''):
    print(dbgOutput)
    sender.play(timings)

s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  response = handle_request(request.decode('utf-8').split('\n')[0])
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  #conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

