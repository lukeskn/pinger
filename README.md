# pinger

A small Ping-Tool for TCP and UDP.
Receiver and Sender in one Python Application.

## How to start:
1. Start the Receiver with an IP and/or a Port. Default TCP is used.<br>
  1a. The Receiver will show the IP/Port. This means the Receiver is listening.
2. Start the Sender with the IP and Port from the Receiver. Default TCP is used.<br>
  2a. The Sender will try to get an answer from the Receiver


## Parameter list:
  ```-r               Initializes the the Receiver.
   -udp             Set the transport protocol to UDP (Default: TCP).
   -ip<IP>          Insert the IP-Address for the Sender or Receiver.
   -cip              (Receiver Only) Prints a List of all available/choosable IP-Addresses.
   -port<port>      Insert the Port from the Receiver.
   -t<number>       (Sender Only) Sets the Amount of Requests the Client will send.
                       Empty Argument to send one Request every second until end.
                       No Argument to send 4 Requests. (Default)
   -re<repeats>     (Sender Only) Set the Number of Packets send every Second.
                       No Argument to send 1 Requests every Second. (Default)
                       > 5 could take longer as a second.
   -l<size>          Change the Packet-Size (Default: 16 Bytes [Data])
                       > 1024 and the Receiver will answer with a 1024 Byte Packet.
   -$a"message"    Send a custom message to the Receiver.
                       > 1024 and the Receiver will answer with a 1024 Byte Packet.
   -$f"file"       Send a custom message from a file.
                       One Line = one Packet
                       > 1024 a Line and the Receiver will answer with a 1024 Byte Packet.

Quick start:
   <ip>:<port>      Initializes the Sender/Receiver for a TCP connection.
   <ip>:<port>u     Initializes the Sender/Receiver for a UDP connection.
   -t<number>       Can also be used with the Quick Start.
   -re<repeats>
   -l<size>
   -$a"message"
   -$f"file"
   -r               Starts the Receiver.
                       No Argument to start the Sender. (Default)
```
Parameters don't need to be in a particular order.
