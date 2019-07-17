#!/usr/bin/env python3

portNumber = []
while True:
    print("Enter the Ethernet Port Number " + str(len(portNumber) + 1) +
        ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    portNumber = portNumber + [name]
print('The port number is / are :')
for name in portNumber:
    print('' + name)
