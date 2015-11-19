#!/usr/bin/python3
from subprocess import call
from time import sleep
import socket

HashFileName = "hash.bin"
SleepSeconds = 120
HOST = 'localhost'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096

while True:
	call(["make", "daemon"])	
	hashFile = open(HashFileName,'rb')

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)
	byte = hashFile.read(1)
	hashInDec = []
	while len(byte) != 0:
		num = 0
		for i in range(4):
			if len(byte) != 0:
				num = num*256 + ord(byte)
				byte = hashFile.read(1)
		hashInDec.append(num)
	client.send(('\n'.join(str(x) for x in hashInDec)).encode())
	print('File Sent')	
	client.close()
	sleep(SleepSeconds)
