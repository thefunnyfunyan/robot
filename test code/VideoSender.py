##create socket client, send images

import datetime
import pygame
import socket
import time

HOST = '127.0.0.1'
PORT = 5000

socket_connection = socket.socket()
socket_connection.connect((HOST, PORT))


pygame.init()
image = pygame.display.set_mode((1, 1))


image = pygame.image.load('space.jpg').convert()
image_string = pygame.image.tostring(image, 'RGB')
print(image_string)
print(image_string.__sizeof__())

socket_connection.send(image_string)


