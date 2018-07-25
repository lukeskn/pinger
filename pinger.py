import sys
from connection import sender as sender, receiver as receiver
import re
from other import generalInformation

VERSION = 2.1

TCP = 1
UDP = 2
SENDER = 1
RECEIVER = 2
NOT_SET = -1
DEFAULT_REPEATS = 4

repeatsSecond = NOT_SET
connectionType = TCP
clientType = SENDER
port = NOT_SET
ip = NOT_SET
repeat = DEFAULT_REPEATS

# If no Start Parameters are given, this Method will ask for the ClientType.
def noParamAtStart():
    generalInformation.sendHelpInformation(VERSION)

# Initializes the Sender.
def startSender():
    snd = sender.SenderClient(connectionType, port, ip, repeat, repeatsSecond)

# Initializes the Receiver.
def startReceiver():
    rec = receiver.ReceiverClient(connectionType, ip, port)

# Validates a given parameter.
# removes the '-'. / Make the String lowercase.
def validateParam(param):
    param = param.lower()
    if param[0] == "-":
        param = param[1:]
    return param

# Initializes QuickStart.
def initQuickStart():
    for i in range(1, len(sys.argv)):
        param = validateParam(sys.argv[i])
        if ":" in param:
            splitedParam = splitParam(param)
            ip = splitedParam[0]
            try:
                port = int(splitedParam[1])
                connectionType = TCP
            except ValueError:
                port = removeCharacterFromString(splitedParam[1])
                port = int(port[0])
                connectionType = UDP
            return connectionType, ip, port

# Checks if Quickstart parameters are given.
def isQuickStart():
    for i in range(1, len(sys.argv)):
        param = validateParam(sys.argv[i])
        if ":" in param:
            return True
    return False

# Splits a given String by ':'.
def splitParam(param):
    return param.split(":")

# Removes all characters from a String.
# Returns all digits from a given String.
def removeCharacterFromString(string):
    return re.findall('\d+', string)
try:
    # Read Start Parameter
    if len(sys.argv) > 1:
        if isQuickStart():
            connectionType, ip, port = initQuickStart()
        lastParam = ""
        for i in range(1,len(sys.argv)):
            param = validateParam(sys.argv[i])
            if param == "help" or param == "\?" or param == "?" or param == "/?":
                generalInformation.sendHelpInformation(VERSION)
                sys.exit(0)
            if param == "tcp":
                connectionType = TCP
            elif param == "udp":
                connectionType = UDP
            elif param == "cip":
                generalInformation.printIPs()
                sys.exit(0)
            elif param[:2] == "re":
                try:
                    repeatsSecond = removeCharacterFromString(sys.argv[i])
                    repeatsSecond = int(repeatsSecond[0])
                    print(repeatsSecond)
                except IndexError:
                    repeatsSecond = NOT_SET
            elif param[0] == "port" or param[0] == "p":
                try:
                    port = removeCharacterFromString(sys.argv[i])
                    port = int(port[0])
                except IndexError:
                    port = NOT_SET
            elif param[0] == "ip":
                try:
                    ip = removeCharacterFromString(sys.argv[i])
                    ip = int(ip[0])
                except IndexError:
                    ip = NOT_SET
            elif param[0] == "t":
                try:
                    repeat = removeCharacterFromString(sys.argv[i])
                    repeat = int(repeat[0])
                except IndexError:
                    repeat = NOT_SET
            elif param == "r" or param == "receiver":
                clientType = RECEIVER
        if clientType != NOT_SET:
            if(clientType == 1):
                startSender()
            else:
                startReceiver()
    else:
        noParamAtStart()
except KeyboardInterrupt:
    sys.exit(0)