import pygame
import sys

pygame.init()

map_image = pygame.image.load(("map.png"))
map_rect = map_image.get_rect()

screen = pygame.display.set_mode((map_rect.width, map_rect.height))
pygame.display.set_caption("Map Viewer")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(map_image,(0,0))
    pygame.display.flip()        
    
pygame.quit()
sys.exit()