import socket
# Prints help information.
def sendHelpInformation(version):
    print("")
    print(" parameters don't need to be in a particular order!")
    print(" pinger by Lucas Knorbien")
    print(" version:", version)
    print("")

    print(" parameter list:")
    print("    -r               Initializes the the Receiver.")
    print("    -udp             Set the transport protocol to UDP (Default: TCP).")
    print("    -ip<IP>          Insert the IP-Address for the Sender or Receiver.")
    print("    -cip              (Receiver Only) Prints a List of all available/choosable IP-Addresses.")
    print("    -port<port>      Insert the Port from the Receiver.")
    print("    -t<number>       (Sender Only) Sets the Amount of Requests the Client will send.")
    print("                        Empty Argument to send one Request every second until end.")
    print("                        No Argument to send 4 Requests. (Default)")
    print("    -re<repeats>     (Sender Only) Set the Number of Packets send every Second.")
    print("                        No Argument to send 1 Requests every Second. (Default)")
    print("                        > 5 could take longer as a second.")
    print("    -l<size>          Change the Packet-Size (Default: 16 Bytes [Data]) ")
    print("                        > 1024 and the Receiver will answer with a 1024 Byte Packet. ")
    print("")
    print(" Quick start:")
    print("    <ip>:<port>      Initializes the Sender/Receiver for a TCP connection.")
    print("    <ip>:<port>u     Initializes the Sender/Receiver for a UDP connection.")
    print("    -t<number>       Can also be used with the Quick Start.")
    print("    -re<repeats>     ")
    print("    -l<size>         ")
    print("    -r               Starts the Receiver.")
    print("                        No Argument to start the Sender. (Default)")

def printIPs():
    def getMultipleIPAdresses():
        sockIP = socket.gethostbyname_ex(socket.gethostname())
        ipList = []
        for ip in enumerate(sockIP[2]):
            ipList.append(ip[1])
        return ipList

    print("Available IP's:")
    ipList = getMultipleIPAdresses()
    for item in enumerate(ipList):
        print(item[1])

