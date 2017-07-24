import pygame

def main():
    pygame.init()
    eval=True
    WIDTH=600
    HEIGHT=600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    while(eval):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_RIGHT]):
            rightArrow()
        if (keys[pygame.K_LEFT]):
            leftArrow()
        if (keys[pygame.K_UP]):
            upArrow()
        if (keys[pygame.K_DOWN]):
            downArrow()
        pygame.event.pump()

def leftArrow():
    print("left")

def rightArrow():
    print("right")

def upArrow():
    print("up")

def downArrow():
    print("down")

if __name__ == "__main__":
    main()