from other import validate
import socket
import sys
NOT_SET = -1
class ReceiverClient(object):

    # Initializes the Receiver Object
    def __init__(self, connectionType, ip, port):
        self.connectionType = connectionType
        self.port = port
        self.ip = ip
        self.startReceiver()

    # Checks if all important Information are given and tries to start the TCP or UDP receiver.
    def startReceiver(self):
        if self.ip == NOT_SET:
            self.ip = self.getIPaddress()
        if validate.allInformationGiven(self.connectionType, self.port, self.ip):
            if self.connectionType == 1:
                print("TCP Receiver successfully started.")
                print("IP-Address: ", self.ip)
                print("Port      : ", self.port)
                self.doTCPReceiver()
            elif self.connectionType == 2:
                print("UDP Receiver successfully started.")
                print("IP-Address: ", self.ip)
                print("Port      : ", self.port)
                self.doUDPReceiver()
        else:
            print("Missing Information:", validate.findMissingInformation(self.connectionType, self.port, self.ip))
            print("Start with 'help' to print a help Page.")
            sys.exit(1)

    # Reads the Systems IP-Address.
    def getIPaddress(self):
        return socket.gethostbyname(socket.gethostname())

    # Starts the UDP receiver.
    def doUDPReceiver(self):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_address = (self.ip, int(self.port))
            try:
                serverSocket.bind(server_address)
            except:
                print("Something went wrong. Try again")
            while True:
                try:
                    message, address = serverSocket.recvfrom(1024)
                    if message:
                        print("UDP Connection from:{}:{}".format(address[0], self.port))
                    message = message.upper()
                    serverSocket.sendto(message, address)
                except KeyboardInterrupt:
                    sys.exit(1)
                except:
                    print("Something went wrong")
                    break
        except KeyboardInterrupt:
            sys.exit(2)

    # Starts the TCP receiver.
    def doTCPReceiver(self):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (self.ip, int(self.port))
            try:
                serverSocket.bind(server_address)
            except:
                print("Can't bind Socket / Wrong IP")
                sys.exit()

            while True:
                try:
                    serverSocket.listen(1)
                    conn, addr = serverSocket.accept()
                    print('TCP Connection from: {}:{}'.format(addr[0], self.port))

                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(b'test')
                except:
                    print("Something went wrong")
                    break
            conn.close()
        except KeyboardInterrupt:
            sys.exit(2)