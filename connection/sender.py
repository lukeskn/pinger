from other import validate
import socket
import time
import sys
NOT_SET = -1
SECOND = 1
DEFAULT_SPEED = 1

class SenderClient(object):

    # Initializes the Sender Object
    def __init__(self, connectionType, port, ip, repeat, repeatsSecond):
        self.connectionType = connectionType
        self.port = port
        self.ip = ip
        self.repeat = repeat
        self.repeatsSecond = repeatsSecond
        self.startSender()

    # Checks if all important Information are given and tries to start the TCP or UDP sender.
    def startSender(self):

        if validate.allInformationGiven(self.connectionType, self.ip, self.port):
            if self.connectionType == 1:
                print("TCP Sender successfully started.")
                print("IP-Address: ", self.ip)
                print("Port      : ", self.port)
                self.doTCPSender()
            elif self.connectionType == 2:
                print("UDP Sender successfully started.")
                print("IP-Address: ", self.ip)
                print("Port      : ", self.port)
                self.doUDPSender()
        else:
            print("Missing Information:", validate.findMissingInformation(self.connectionType, self.ip, self.port))
            print("Start with 'help' to print a help Page.")
            sys.exit(1)
    def getSleeptimefromRepeats(self):
        if self.repeatsSecond == NOT_SET:
            return DEFAULT_SPEED
        sleepTime = SECOND / self.repeatsSecond
        return sleepTime
    # Starts the UDP sender.
    def doUDPSender(self):

        def doUDPConnection():
            time.sleep(self.getSleeptimefromRepeats())
            start = time.time()
            sock.sendto(message.encode(), addr)
            try:
                data, server = sock.recvfrom(1024)
                if data:
                    end = time.time()
                    print("UDP answer from:", server[0], "TIME:", int((end-start)*1000), "ms")
            except KeyboardInterrupt:
                    sys.exit(0)
            except:
                print('REQUEST TIMED OUT')

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        sock.settimeout(1)
        message = 'test'
        addr = (self.ip, int(self.port))

        if self.repeat == NOT_SET:
            while True:
                doUDPConnection()
        else:
            for counter in range(int(self.repeat)):
                doUDPConnection()

    # Starts the TCP sender.
    def doTCPSender(self):
        def doTCPConnection():
            try:
                time.sleep(self.getSleeptimefromRepeats())
                sock = socket.socket(socket.AF_INET)
                sock.settimeout(1)

                sock.connect((self.ip, int(self.port)))
                start = time.time()
                sock.sendall(b'-1')
                data = sock.recv(1024)
                end = time.time()
                sock.close()
                print("TCP answer from:", self.ip, "TIME:", int((end-start)*1000), "ms")
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                print('REQUEST TIMED OUT')

        if self.repeat == NOT_SET:
            while True:
                doTCPConnection()
        else:
            for counter in range(int(self.repeat)):
                doTCPConnection()
