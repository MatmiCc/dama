import pygame
from dama.promenne import sirka, vyska
from dama.sachovnice import Sachovnice

FPS = 60

policko = pygame.display.set_mode((sirka, vyska))
pygame.display.set_caption('dama')

def main():
    run = True
    clock = pygame.time.Clock()
    sachovnice = Sachovnice()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        sachovnice.vybrana_pole(policko)
        pygame.display.update()

    pygame.quit()

main()