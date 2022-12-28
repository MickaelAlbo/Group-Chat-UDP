# Server Chat

## Table of contents
1. [ Background. ](#back)
2. [How to run the chat?](#run)
3. [Addendum](#add)

<a name="back"></a>
## Background
Here is implement a simple chat that behaves in a similar way to a WhatsApp group, where each of the contacts can write, and every message someone write is sent to all members of the group. When someone sends a message to the group - the message is sent to all members of the group. However, the server will send the appropriate messages to the clients only when they contact the server.

<a name="run"></a>
## How to run the chat?
For running the server and the client, you should firstly run the server in the terminal like:  ```[python command of interpreter] [name of the server file] [port]```.
For example ```python3 server.py 12345```.
After that you need to run the client like: ```[python command of the interpreter] [name of the client file] [ip]] [port]```.
For example: ```python3 client.py 127.0.0.1 12345```.
Note: It is possible to run in Windows, in a virtual machine or in wsl.

<a name="add"></a>
## Addendum
