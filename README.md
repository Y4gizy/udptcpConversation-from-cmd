# udptcpConversation-from-cmd

A software system that allows communication from a computer terminal to devices connected to the same network.
Understanding UDP and TCP Communication Protocols

In computer networking, UDP (User Datagram Protocol) and TCP (Transmission Control Protocol) are two fundamental communication protocols used to transmit data over the Internet or other networks. Both protocols operate on top of the Internet Protocol (IP), but they function in different ways and serve different purposes depending on the needs of the application.

1. Transmission Control Protocol (TCP)
TCP is a connection-oriented protocol, which means that it establishes a connection between the sender and receiver before any data is transferred. It ensures reliable and ordered delivery of data, making it suitable for applications where accuracy and data integrity are crucial.

Key Features of TCP:
Reliable data transfer (guarantees delivery)

Error checking and correction

Data is received in the same order it was sent

Flow control and congestion control

Establishes a connection using a 3-way handshake (SYN, SYN-ACK, ACK)

Common Use Cases:
Web browsing (HTTP, HTTPS)

Email (SMTP, IMAP, POP3)

File transfers (FTP)

Remote access (SSH, Telnet)

2. User Datagram Protocol (UDP)
UDP is a connectionless protocol. It sends data as individual packets, called datagrams, without establishing a connection first. It offers faster transmission but does not guarantee delivery, order, or error checking beyond basic checksums.

Key Features of UDP:
No connection setup (lower overhead)

Faster transmission speed

No guarantee of delivery or order

Minimal error recovery

Common Use Cases:
Video and audio streaming

Online gaming

Voice over IP (VoIP)

DNS queries
