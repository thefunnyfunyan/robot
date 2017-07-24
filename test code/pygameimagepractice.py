import pygame
import time

pygame.init()
surface = pygame.display.set_mode((0, 0))
surface.fill((0,0,0))

img = pygame.image.load('space.jpg').convert()
size = img.get_size()
byte_image = pygame.image.tostring(img, 'RGB')
test_string = 'test'.encode()
print(byte_image.decode('utf-8'))
print(type(test_string))
print(b'test')
print(str(b'test'))
print(b'test'.decode('utf-8'))

#print(type(byte_image))
#print(type(str(byte_image)))
#print(bytes((str(byte_image).encode()).decode()))










#img2 = pygame.image.load('planes.jpg').convert()
#strimg = pygame.image.tostring(img, 'RGB')
#newimg = pygame.image.fromstring(strimg, size, 'RGB')
#index = 1
#while(True):
#    if(index == 1):
#        image.blit(newimg, (0, 0))
#        index = 2
#    else:
#        image.blit(img2, (0,0))
#        index = 1
#
#    print('here')
#    time.sleep(1)
#    pygame.display.update()