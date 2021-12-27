import sys
# TODO: import socket libraries
from socket import *


NUM_TRANSMISSIONS=200
if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a relay socket to listen on relay_port for new connections
relay_sock = socket(AF_INET, SOCK_STREAM)

# TODO: Bind the relay's socket to relay_port
relay_sock.bind(("127.0.0.1", relay_port))

# TODO: Put relay's socket in LISTEN mode
relay_sock.listen()

# TODO: Accept a connection first from sender.py (accept1)
(send_sock, addr1) = relay_sock.accept()

# TODO: Then, accept a connection from receiver.py (accept2)
(recv_sock, addr2) = relay_sock.accept()

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive data from sender socket (the return value of accept1)
  # Be careful with the length of data you receive
  send_data = send_sock.recv(200).decode()

  # TODO: Check for any bad words and replace them with the good words
  # Replace 'virus' with 'groot'
  # Replace 'worm' with 'hulk'
  # Replace 'malware' with 'ironman'
  send_data = send_data.replace("virus", "groot")
  send_data = send_data.replace("worm", "hulk")
  send_data = send_data.replace("malware", "ironman")

  # TODO: and forward the new string to the receiver socket (the return value of accept2)
  recv_sock.send(send_data.encode())

  # TODO: print data that was relayed
  print("relayed: ")
  print(send_data)

# TODO: Close all open sockets
relay_sock.close()
