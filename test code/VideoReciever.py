##create Socket Server, display image@
##
import datetime
import pygame
import socket
import time

HOST = '127.0.0.1'
PORT = 5000

##################################
#######Socket portion#############
##################################

socket_server = socket.socket()
socket_server.bind((HOST, PORT))
socket_server.listen(1)
socket_connection, connection_address = socket_server.accept()
data = b''
big_enough = False
while(not big_enough):
    data += socket_connection.recv(512)
    if(data.__sizeof__() == 921617): big_enough = True
if not data: print("No Data")
print(data)
print(type(data))

################################

#############################
#######Displaying image######
#############################

pygame.init()
screen = pygame.display.set_mode((0, 0))
screen.fill((0,0,0))
connected_image = pygame.image.fromstring(data,(640, 480), 'RGB')
screen.blit(connected_image, (0,0))
print('test')
while(1):
    pygame.display.update()



