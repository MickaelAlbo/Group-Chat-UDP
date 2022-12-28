import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if len(sys.argv) < 2 or sys.argv[2].isdigit() is False or int(sys.argv[2]) <= 0 or int(sys.argv[2]) > 65536:
    sys.exit()
ip, port = sys.argv[1], int(sys.argv[2])

while True:
    message = input()
    s.sendto(message.encode(), (ip, port))
    data, address = s.recvfrom(1024)
    new_data = data.decode()
    if message == '4' and new_data != 'Illegal request':
        break
    if new_data != '':
        print(str(new_data))

s.close()
