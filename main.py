from constants import *
import pygame
import bubble



clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()




bubbles = pygame.sprite.Group()
bubble_dispenser = []

for i in range(COL_WIDTH):
    bubble_dispenser.append(bubble.Bubble(i * GRID_SIZE, -200))

for b in bubble_dispenser:
    bubbles.add(b)






def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    bubbles.draw(surface)
    pygame.display.flip()



def update():
    for b in bubble_dispenser:
        if b.is_past_dispenser:
            bub = bubble.Bubble(b.rect.x, -200)
            bubbles.add(bub)
            bubble_dispenser.remove(b)
            bubble_dispenser.append(bub)

    bubbles.update(bubbles)



if __name__ == "__main__":
    main()
