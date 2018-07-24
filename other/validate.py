import re
NOT_SET = -1

# Checks if a given IP-Address (IPv4) is valid.
def isIPValid(ip):
    reg = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if reg.match(ip):
        return True
    else:
        return False

# Checks if a given Port is valid.
# Number has to be a digit.
# Number between 1 - 65536
def isPortValid(port):
    try:
        checkValue = int(port)
    except ValueError:
        return False

    if checkValue > 1 and checkValue < 65536:
        return True
    else:
        return False

# Checks if a given ConnectionType Input (TCP or UDP) is valid.
def isConnectionTypeValid(connectionType):
    connectionType.lower()

    if connectionType == "tcp" or connectionType == "udp":
        return True
    else:
        return False

# Checks if a the Number of repeats is Valid.
# The Input has to be a digit.
def isNumberOfRepeatsValid(repeats):
    if repeats.isdigit():
        return True
    else:
        return False


# Checks if all Information are given.
# Repeats, ConnectionType, Port, IP-Address
def allInformationGiven(connectionType, port, ip ):
    if connectionType != NOT_SET and port != NOT_SET and ip != NOT_SET:
        return True
    else:
        return False


def findMissingInformation(connectionType, port, ip):
    if connectionType == NOT_SET:
        return "connectionType"
    if port == NOT_SET:
        return "port"
    if ip == NOT_SET:
        return "IP-Address"