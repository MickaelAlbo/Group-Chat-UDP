import socket
import sys

# list_clients = [(address, (name, list_of_messages))]
list_clients = {}
list_of_messages = []


def get_all_users_names():
    all_names = []
    for client_address in list_clients:
        all_names.append(list_clients[client_address][0])
    all_names_reverse = all_names
    all_names_reverse.reverse()
    names = ', '.join(all_names_reverse)
    return names


def join_chat(name, address):
    # Add the message to all users
    for client_address in list_clients:
        list_clients[client_address][1].append(name + " has joined")
    all_names = get_all_users_names()
    # Add the new user
    list_clients[address] = (name, [all_names])


def add_message(message, address):
    # Add message to all users except sender
    for client_address in list_clients:
        if address != client_address:
            list_clients[client_address][1].append(message)


def change_name(new_name, address):
    # Update the new_name of the client
    name = ""
    for client_address in list_clients:
        if address == client_address:
            name = list_clients[address][0]
            list_clients[address] = (new_name, list_clients[address][1])
            break
    # Update the new_name to all other clients
    add_message(name + " changed his name to " + new_name, address)


def left_group(address):
    name = list_clients[address][0]
    list_clients.pop(address)
    add_message(name + " has left the group", address)
    s.sendto(''.encode(), address)


def add_new_message(message, address):
    name = list_clients[address][0]
    add_message(name + ": " + message, address)


def send_all_waiting_messages(address):
    all_messages = '\n'.join(list_clients[address][1])
    list_clients[address][1].clear()
    s.sendto(all_messages.encode(), address)


def is_user_exist(address):
    val = list_clients.get(address)
    return val is not None


def illegal_request():
    s.sendto('Illegal request'.encode(), addr)


port = sys.argv[1]
# Check if port is not correct
if port.isdigit() is False or int(port) <= 0 or int(port) > 65536:
    sys.exit()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', int(port)))

while True:
    data, addr = s.recvfrom(1024)
    data = data.decode()
    # Split the string only by first space
    split_data = data.split(" ", 1)
    request = ""
    # Save 2nd arg if exist
    if len(split_data) > 1:
        request = split_data[1]
    request_type = split_data[0]
    # Options of request types
    # 1 - Join the chat
    if request_type == '1':
        if not is_user_exist(addr):
            join_chat(request, addr)
            send_all_waiting_messages(addr)
        else:
            illegal_request()
    # 2 - Send new message
    elif request_type == '2':
        if is_user_exist(addr) and request != '':
            add_new_message(request, addr)
            send_all_waiting_messages(addr)
        else:
            illegal_request()
    # 3 - Change name
    elif request_type == '3':
        if is_user_exist(addr):
            change_name(request, addr)
            send_all_waiting_messages(addr)
        else:
            illegal_request()
    # 4 - Leave the group
    elif request_type == '4':
        if is_user_exist(addr) and len(split_data) == 1:
            left_group(addr)
        else:
            illegal_request()
    # 5 - Get all messages
    elif request_type == '5':
        if is_user_exist(addr) and len(split_data) == 1:
            send_all_waiting_messages(addr)
        else:
            illegal_request()
    else:
        illegal_request()

