from Pencil import Pencil
import random


class DrawScene:

    @staticmethod
    def draw_scene(screen, bg, start_draw_map_pos, scale, area_config):
        text_color = (230, 230, 230)

        screen.blit(bg, start_draw_map_pos)
        Pencil.draw_alpha_rect(screen, [0, int(400 * scale), int(300 * scale), int(680 * scale)], alpha=0.5)

        # Defense area
        Pencil.write_text(screen, "Defense State", [int(10 * scale), int(420 * scale)], font_size=18, color=text_color)
        Pencil.draw_rect(screen, [int(10 * scale), int(460 * scale), int(270 * scale), int(260 * scale)],
                         color=text_color, width=1)
        Pencil.draw_rect(screen, [int(20 * scale), int(470 * scale), int(60 * scale), int(30 * scale)],
                         color=(150, 0, 0), width=0)
        Pencil.write_text(screen, "RED   Defender" + " %d" % area_config.site_list[1].red_defender_num,
                          [int(100 * scale), int(475 * scale)], font_size=19, color=(250, 0, 0))
        Pencil.draw_rect(screen, [int(20 * scale), int(510 * scale), int(60 * scale), int(30 * scale)],
                         color=(0, 150, 0), width=0)
        Pencil.write_text(screen, "GREEN Defender" + " %d" % area_config.site_list[1].green_defender_num,
                          [int(100 * scale), int(515 * scale)], font_size=19, color=(0, 250, 0))
        Pencil.draw_rect(screen, [int(20 * scale), int(550 * scale), int(60 * scale), int(30 * scale)],
                         color=(0, 0, 150), width=0)
        Pencil.write_text(screen, "BLUE  Defender" + " %d" % area_config.site_list[1].blue_defender_num,
                          [int(100 * scale), int(555 * scale)], font_size=19, color=(0, 0, 250))

        # Attacker area
        Pencil.write_text(screen, "Attacker State", [int(10 * scale), int(750 * scale)], font_size=18, color=text_color)
        Pencil.draw_rect(screen, [int(10 * scale), int(790 * scale), int(270 * scale), int(260 * scale)],
                         color=text_color, width=1)
        for i in range(len(area_config.site_list[0].hacker_list)):
            if area_config.site_list[0].hacker_list[i].duration == [-1, -1]:
                duration = "--:--"
            else:
                duration = "%02d:%02d" % (area_config.site_list[0].hacker_list[i].duration[0], area_config.site_list[0].hacker_list[i].duration[1])
            Pencil.write_text(screen,
                              "Hacker%2d:   " % (i + 1) + area_config.site_list[0].hacker_list[i].state + "   " + duration,
                              [int(22 * scale), int(800 + 20 * i * scale)], font_size=18, color=area_config.site_list[0].hacker_list[i].color)
        Pencil.write_text(screen, "Max Duration:     %05d" % area_config.site_list[0].max_duration, [int(22 * scale), int(800 + 20 * len(area_config.site_list[0].hacker_list * scale))],
                          font_size=18, color=(230, 230, 230))

        # Sites & Hackers
        for site in area_config.site_list:
            screen.blit(site.image, [start_draw_map_pos[0] + site.pos[0], start_draw_map_pos[1] + site.pos[1]])
            Pencil.write_text(screen, site.name, [start_draw_map_pos[0] + site.pos[0],
                                                  start_draw_map_pos[1] + site.pos[1] - 25 * scale], 25 * scale,
                              site.color)

        for hacker in area_config.site_list[0].hacker_list:
            if hacker.target:
                Pencil.draw_line(screen,
                                 [start_draw_map_pos[0] + hacker.pos[0], start_draw_map_pos[1] + hacker.pos[1]],
                                 [start_draw_map_pos[0] + hacker.target.center[0],
                                  start_draw_map_pos[1] + hacker.target.center[1]], hacker.color, width=2)

        for defender in area_config.site_list[1].defender_list:
            screen.blit(defender.image, [start_draw_map_pos[0] + defender.pos[0], start_draw_map_pos[1] + defender.pos[1]])
