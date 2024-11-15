import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        x,y=(0,0)
        running = True
        while running:
            screen.fill("light green")
            for i in range(0, 641, 32):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 512))
            for i in range(0, 513, 32):
                pygame.draw.line(screen, (0, 0, 0), (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x2,y2=event.pos
                    if x<=x2<=x+32 and y<=y2<=y+32:
                        x,y=(random.randrange(0,640),random.randrange(0,512))
                        x=x-(x%32)
                        y=y-(y%32)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()