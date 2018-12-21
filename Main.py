import pygame
from pygame.locals import *
import time
from AreaConfig import AreaConfig
from DataBase import DataBase
from DrawScene import DrawScene
from LinearRegression import LinearRegression
from Pencil import Pencil
from Timer import Timer
from Trigger import Trigger


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # whole map size is [2560, 1376]
    scale = 1
    map_scale = 1
    SCREEN_WIDTH_HEIGHT = [int(1920 * scale), int(1080 * scale)]
    whole_map_size = [int(2560 * scale * map_scale), int(1376 * scale * map_scale)]

    # Create background
    screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT, RESIZABLE, 32)
    pygame.display.set_caption("Hack This Word v1.0")
    bg = pygame.image.load("img/word_bg.jpg")
    bg = pygame.transform.scale(bg, whole_map_size)
    start_draw_map_pos = [-400 * scale, -100 * scale]
    map_moving = False
    last_mouse_pos = []

    # Create DataBase and Learning Model
    data_base = DataBase([0, 0, 0], [0])
    lin_reg = LinearRegression()

    # Create constant value
    timer = Timer()
    timer.set_time(0, 0, 0)
    tick_elapsed = 0
    ticks = 0
    interval = 0
    interval_speed = 3

    # Create Site
    area_config = AreaConfig(scale, timer, lin_reg)

    # Create Trigger
    trigger = Trigger(timer, area_config)

    while True:
        clock.tick(30)
        since = time.time()

        # scale the map_size
        whole_map_size = [int(2560 * scale * map_scale), int(1376 * scale * map_scale)]
        bg = pygame.transform.scale(bg, whole_map_size)

        # Draw Scene
        DrawScene.draw_scene(screen, bg, start_draw_map_pos, scale, area_config)
        time_size = int(38 * scale)
        Pencil.write_text(screen, "%02d:%02d:%02d" % (timer.get_hour(), timer.get_minute(), timer.get_second()),
                          [(SCREEN_WIDTH_HEIGHT[0] - time_size * 5) * scale, 20 * scale], font_size=time_size,
                          color=(230, 230, 230))

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

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    pass

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

        tick_elapsed += time.time() - since
        if tick_elapsed >= 1:
            timer.elapse_one_second()
            tick_elapsed = 0

        ticks += 1
        if ticks % interval_speed == 0:
            interval += 1
            ticks %= 1000
            interval %= 100

        trigger.update(interval)
        pygame.display.update()


if __name__ == "__main__":
    main()
