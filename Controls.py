import pygame
import pygame.freetype
from game.lib.colors import *


class Controls:
    def __init__(self, game, exit_screen):
        self.game = game
        self.size = self.game.screen.get_size()
        self.menu = pygame.freetype.SysFont('Arial', 50)
        self.title = pygame.freetype.SysFont('Arial', 70)
        self.text = pygame.freetype.SysFont('Arial', 50)
        self.exit_screen = exit_screen

    def draw(self):

        self.game.screen.fill(WHITE)

        title_x = 100
        title_y = self.size[1] / 8
        self.title.render_to(self.game.screen, (title_x, title_y), "Controls", BLACK)

        first_row_text_y = self.size[1] / 3 + 160
        first_row_icon_y = self.size[1] / 3 + 80
        second_row_text_y = self.size[1] * (3/4) + 80

        wsad_length_x = 230
        wsad_length_y = 150
        wsad_icon_x = self.size[0] / 4 - 80
        wsad_icon_y = self.size[1] / 3
        wsad_text_x = wsad_icon_x + 60

        self.text.render_to(self.game.screen, (wsad_text_x, first_row_text_y), "Move", BLACK)
        pygame.draw.rect(self.game.screen, BLACK, (wsad_icon_x, wsad_icon_y, wsad_length_x, wsad_length_y), 2)

        key_length = 70

        equip_icon_x = self.size[0] / 2 - 40
        equip_text_x = equip_icon_x - 60

        self.text.render_to(self.game.screen, (equip_text_x, first_row_text_y), "Equipment", BLACK)
        pygame.draw.rect(self.game.screen, BLACK, (equip_icon_x, first_row_icon_y, key_length, key_length), 2)

        use_icon_x = self.size[0] * (3/4) - 170

        self.text.render_to(self.game.screen, (use_icon_x, first_row_text_y), "Use", BLACK)
        pygame.draw.rect(self.game.screen, BLACK, (use_icon_x, first_row_icon_y, key_length, key_length), 2)

        escape_icon_x = self.size[0] * (3 / 4) + 30
        escape_text_x = escape_icon_x - 15

        self.text.render_to(self.game.screen, (escape_text_x, first_row_text_y), "Menu", BLACK)
        pygame.draw.rect(self.game.screen, BLACK, (escape_icon_x, first_row_icon_y, key_length, key_length), 2)

        access_x_length = 390
        access_y_length = 70
        access_icon_x = self.size[0] / 4 - 160
        access_icon_y = self.size[1] * (3/4)
        access_text_x = access_icon_x + 70

        self.text.render_to(self.game.screen, (access_text_x, second_row_text_y), "Quick access", BLACK)
        pygame.draw.rect(self.game.screen, BLACK, (access_icon_x, access_icon_y, access_x_length, access_y_length), 2)

        mouse_length = 140
        mouse_icon_y = self.size[1] * (3 / 4) - 70

        attack_icon_x = self.size[0] / 2
        attack_text_x = attack_icon_x + 15

        self.text.render_to(self.game.screen, (attack_text_x, second_row_text_y), "Attack", BLACK)
        pygame.draw.rect(self.game.screen, BLACK, (attack_icon_x, mouse_icon_y, mouse_length, mouse_length), 2)

        move_icon_x = self.size[0] * (3 / 4) - 80
        move_text_x = move_icon_x + 40

        self.text.render_to(self.game.screen, (move_text_x, second_row_text_y), "Aim", BLACK)
        pygame.draw.rect(self.game.screen, BLACK, (move_icon_x, mouse_icon_y, mouse_length, mouse_length), 2)

        exit_x = self.size[0] * (5/6)
        exit_y = self.size[1] / 8 + 10
        exit_x_length = 100
        exit_y_length = 40

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if exit_x + exit_x_length > mouse[0] > exit_x and exit_y + exit_y_length > mouse[1] > exit_y:
            self.menu.render_to(self.game.screen, (exit_x, exit_y), "Back", GREEN)
            pygame.draw.rect(self.game.screen, GREEN, (exit_x, exit_y, exit_x_length, exit_y_length), 2)
            if click[0]:
                self.game.current_screen = self.exit_screen
        else:
            self.menu.render_to(self.game.screen, (exit_x, exit_y), "Back", BLACK)
            pygame.draw.rect(self.game.screen, BLACK, (exit_x, exit_y, exit_x_length, exit_y_length), 2)