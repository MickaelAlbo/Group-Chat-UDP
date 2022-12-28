# Server Chat

## Table of contents
1. [ Background ](#back)
2. [How to run the chat?](#run)
3. [Addendum](#add)

<a name="back"></a>
## Background
Here is implement a simple chat that behaves in a similar way to a WhatsApp group, where each of the contacts can write, and every message someone write is sent to all members of the group. When someone sends a message to the group - the message is sent to all members of the group. However, the server will send the appropriate messages to the clients only when they contact the server.  
Here is how client communicates with the server:  
1. <ins>**Join the group:**</ins> To join the group you should send the argument "1" and after that your name.  For example if your name is Alice: ``1 Alice``.
2. <ins>**Send message:**</ins> To send message you should send the argument "2" and that the message you want to send. For example, if you want to send the message 'Hi': ``2 Hi``.
3. <ins>**Change your name:**</ins> If you want to change your name after you have joined you should send the argument "3" and your new name. For example, if you want to change your name to Bob: ``3 Bob``.
4. <ins>**Leave the group:**</ins> If you want to leave the group you should send the argument "4".
5. <ins>**Get an update:**</ins> If you want to get an update from the server (who joined, who left the group, who change his name and the messages sent) you should send the argument "5". 

<a name="run"></a>
## How to run the chat?
For running the server and the client, you should firstly run the server in the terminal like:  ```[python command of interpreter] [name of the server file] [port]```.
For example ```python3 server.py 12345```.
After that you need to run the client like: ```[python command of the interpreter] [name of the client file] [ip]] [port]```.
For example: ```python3 client.py 127.0.0.1 12345```.
Note: It is possible to run in Windows, in a virtual machine or in wsl.

<a name="add"></a>
## Addendum
Here is an example of a chat:  
1. Alice joins
2. Bob joins
3. Bob sends the message: "Hi Alice"
4. Until now:
![image](https://user-images.githubusercontent.com/71727260/209832874-eea8c0ac-f961-46aa-ba94-b6e798548c6f.png)
5. Charlie joins
6. Charlie sends 2 messages: "Hiii", "Whatsupp?"
7. Until now:
![image](https://user-images.githubusercontent.com/71727260/209832972-f2d3e408-30da-4887-a250-6c635a94769f.png)
8. Alice asks for an update
9. Until now:
![image](https://user-images.githubusercontent.com/71727260/209833076-e3b5e263-7580-4396-adb1-95e7890cb109.png)
10. Alice sends the message: "welcome"
11. Alice sends an illegal message ("345ft")
12. Charlie changes his name to "Chari"
13. Charlie sends the message "Yoooo"
14. Until now:
![image](https://user-images.githubusercontent.com/71727260/209833232-c33fd693-59eb-4af2-b425-367762979cb4.png)
15. Charlie leaves the group
16. Bob sends the message: ":)"
17. Alice asks for an update
18. Until now:
![image](https://user-images.githubusercontent.com/71727260/209833410-fc9f621b-921a-4824-8cd1-6b736d42537f.png)


