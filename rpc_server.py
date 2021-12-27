#TODO: import socket library
from socket import *

import sys
NUM_TRANSMISSIONS=10
if(len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port = int(sys.argv[1])

# TODO: Create a socket for the server
rpc_server = socket(AF_INET, SOCK_DGRAM) 

# TODO: Bind it to server_port 
rpc_server.bind(("127.0.0.1", server_port))

def isPrime(n):
    # Corner case
    if (n <= 1):
        return "No"
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return "No"
 
    return "Yes"

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive RPC request from client
  data, addr = rpc_server.recvfrom(10)

  # TODO: Turn byte array that you received from client into a string variable called rpc_data
  rpc_data = data.decode('utf8')

  # TODO: Parse rpc_data to get the argument to the RPC.
  # Remember that the RPC request string is of the form prime(NUMBER)
  numbers = []
  for letter in rpc_data:
   if letter.isdigit():
      numbers.append(int(letter))
  strings = [str(integer) for integer in numbers]
  a_string = "".join(strings)
  an_integer = int(a_string)

  # TODO: Print out the argument for debugging
  print("argument is " + str(an_integer))

  # TODO: Compute if the number is prime (return a 'yes' or a 'no' string)
  isPrime(an_integer)

  # TODO: Send the result of primality check back to the client who sent the RPC request
  rpc_server.sendto(bytes(isPrime(an_integer), encoding='utf8'), addr)

# TODO: Close server's socket
rpc_server.close()