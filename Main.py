import pygame
from pygame.locals import *

from AreaConfig import AreaConfig
from Country import Country
from DrawScene import DrawScene


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # whole map size is [2560, 1376]
    scale = 1
    map_scale = 1
    SCREEN_WIDTH_HEIGHT = [int(1920 * scale), int(1080 * scale)]
    whole_map_size = [int(2560 * scale * map_scale), int(1376 * scale * map_scale)]

    screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT, RESIZABLE, 32)
    pygame.display.set_caption("Hack This Word v1.0")

    bg = pygame.image.load("img/word_bg.jpg")
    bg = pygame.transform.scale(bg, whole_map_size)
    start_draw_map_pos = [-400 * scale, -100 * scale]
    map_moving = False
    last_mouse_pos = []

    # Create Country
    area_config = AreaConfig(scale)

    while True:
        clock.tick(30)

        # scale the map_size
        whole_map_size = [int(2560 * scale * map_scale), int(1376 * scale * map_scale)]
        bg = pygame.transform.scale(bg, whole_map_size)

        # Draw Scene
        DrawScene.draw_scene(screen, bg, start_draw_map_pos, scale, area_config)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    map_moving = True
                    last_mouse_pos = event.pos
                # elif event.button == 4:
                #     map_scale = 1.1
                # elif event.button == 5:
                #     map_scale = 1

            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    map_moving = False

            if event.type == VIDEORESIZE:
                SCREEN_WIDTH_HEIGHT = event.size
                screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT, RESIZABLE, 32)

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
