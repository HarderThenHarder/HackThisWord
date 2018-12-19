import pygame
from pygame.locals import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # whole map size is [2560, 1376]
    scale = 0.8
    SCREEN_WIDTH_HEIGHT = [int(1920 * scale), int(1080 * scale)]
    whole_map_size = [int(2560 * scale), int(1376 * scale)]

    screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT)
    pygame.display.set_caption("Hack This Word v1.0")

    bg = pygame.image.load("img/word_bg.jpg")
    bg = pygame.transform.scale(bg, whole_map_size)
    start_draw_map_pos = [-100, -100]
    map_moving = False
    last_mouse_pos = []

    while True:
        clock.tick(30)

        screen.blit(bg, start_draw_map_pos)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    map_moving = True
                    last_mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    map_moving = False

        if map_moving:
            x_offset = pygame.mouse.get_pos()[0] - last_mouse_pos[0]
            y_offset = pygame.mouse.get_pos()[1] - last_mouse_pos[1]
            last_mouse_pos = pygame.mouse.get_pos()
            if SCREEN_WIDTH_HEIGHT[0] - whole_map_size[0] <= start_draw_map_pos[0] + x_offset <= 0:
                start_draw_map_pos[0] += x_offset
            if SCREEN_WIDTH_HEIGHT[1] - whole_map_size[1] <= start_draw_map_pos[1] + y_offset <= 0:
                start_draw_map_pos[1] += y_offset

        pygame.display.update()


if __name__ == "__main__":
    main()
