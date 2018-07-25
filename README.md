# pinger

A small Ping-Tool for TCP and UDP.
Receiver and Sender in one Python Application.

## How to start:
1. Start the Receiver with an IP and/or a Port. Default TCP is used.<br/>
  1a. The Receiver will show the IP/Port. This means the Receiver is listening.<br/>
2. Start the Sender with the IP and Port from the Receiver. Default TCP is used.<br/>
  2a. The Sender will try to get an answer from the Receiver<br/>


## Parameter list:
  ```-r               Initializes the the Receiver.<br/>
  -udp             Set the transport protocol to either TCP or UDP.<br/>
  -ip<IP>          Insert the IP-Address for the Sender or Receiver.<br/>
  -cip              (Receiver Only) Prints a List of all available/choosable IP-Addresses.<br/>
  -port<port>      Insert the Port from the Receiver.<br/>
  -t<number>       (Sender Only) Sets the Amount of Requests the Client will send.<br/>
                      Empty Argument to send one Request every second until end.<br/>
                      No Argument to send 4 Requests. (Default)<br/>
  -re<repeats>     (Sender Only) Set the Number of Packets send every Second.<br/>
                      No Argument to send 1 Requests every Second. (Default)<br/>
                      > 5 could take longer as a second.<br/>

Quick start:
  <ip>:<port>      Initializes the Sender/Receiver for a TCP connection.<br/>
  <ip>:<port>u     Initializes the Sender/Receiver for a UDP connection.<br/>
  -t<number>       Can also be used with the Quick Start.<br/>
  -re<repeats>     Can also be used with the Quick Start.<br/>
  -r               Starts the Receiver.<br/>
                       No Argument to start the Sender. (Default)<br/>
```
Parameters don't need to be in a particular order.
