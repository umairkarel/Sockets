# Sockets
A socket is an endpoint of a two-way communication link between two programs that you can name and address in a network.
```mermaid
graph LR
A --> S1((socket))
A[PC 1] -.- B[PC 2] 
B --> S2((socket))
```

## Local Network
```mermaid
graph LR
A[Modem <br> public IP] -.- B[Router] 
B --> C1[C1 <br> private IP]
B --> C2[C2 <br> private IP]
B --> C3[C3 <br> private IP]
```

## Client-Server Architecture
```mermaid
graph LR
C1[PC 1] -- Hi --> A[Server <br> 192.168.0.15]
C3[Phone] --> A
A --> C4[PS4]
A -- Hi --> C2[PC 2]
```

## TCP vs UDP
|       TCP                       |      HTML                 |                    
|---------------------------------|---------------------------|
| Reliable -> detects packet loss | Sends one Datagram        |
| Connection-based                | No order                  |
| Sequential                      | No Guarantee              |
| Byte Stream                     | Real-Time, Faster         |
| Keeps up connection             | Less Network and PC stress|

Ex. Skype uses UDP for calls and TCP for chats/messages. 