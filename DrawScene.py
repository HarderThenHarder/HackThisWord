from Pencil import Pencil


class DrawScene:

    @staticmethod
    def draw_scene(screen, bg, start_draw_map_pos, scale):
        text_color = (230, 230, 230)

        screen.blit(bg, start_draw_map_pos)
        Pencil.draw_alpha_rect(screen, [0, int(400 * scale), int(300 * scale), int(680 * scale)], alpha=0.5)
        Pencil.write_text(screen, "Defense Weapon", [int(10 * scale), int(420 * scale)], font_size=18, color=text_color)
        Pencil.draw_rect(screen, [int(10 * scale), int(460 * scale), int(270 * scale), int(260 * scale)],
                         color=text_color, width=1)
        Pencil.write_text(screen, "Word State", [int(10 * scale), int(750 * scale)], font_size=18, color=text_color)
        Pencil.draw_rect(screen, [int(10 * scale), int(790 * scale), int(270 * scale), int(260 * scale)],
                         color=text_color, width=1)
