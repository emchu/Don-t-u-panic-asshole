import pygame
import pygame.freetype

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)


class Controls:
    def __init__(self, game, exit_screen):
        self.game = game
        self.size = self.game.screen.get_size()
        self.menu = pygame.freetype.SysFont('Arial', 50)
        self.title = pygame.freetype.SysFont('Arial', 70)
        self.text = pygame.freetype.SysFont('Arial', 50)
        self.exit_screen = exit_screen

    def draw(self):

        self.game.screen.fill(white)
        self.title.render_to(self.game.screen, (100, self.size[1] / 8), "Controls", black)

        # WSAD

        self.text.render_to(self.game.screen, (self.size[0] / 4 - 65, self.size[1] / 3 + 160), "Move", black)
        pygame.draw.rect(self.game.screen, black, (self.size[0] / 4 - 80, self.size[1] / 3, 230, 150), 2)

        # Equipment I

        self.text.render_to(self.game.screen, (self.size[0] / 2 - 100, self.size[1] / 3 + 160), "Equipment", black)
        pygame.draw.rect(self.game.screen, black, (self.size[0] / 2 - 40, self.size[1] / 3 + 70, 70, 70), 2)

        # Use E

        self.text.render_to(self.game.screen, (self.size[0] * (3 / 4) - 170, self.size[1] / 3 + 160), "Use", black)
        pygame.draw.rect(self.game.screen, black, (self.size[0] * (3/4) - 170, self.size[1] / 3 + 70, 70, 70), 2)

        # Escape

        self.text.render_to(self.game.screen, (self.size[0] * (3 / 4) + 15, self.size[1] / 3 + 160), "Menu", black)
        pygame.draw.rect(self.game.screen, black, (self.size[0] * (3 / 4) + 15, self.size[1] / 3 + 70, 70, 70), 2)

        # Quick access

        self.text.render_to(self.game.screen, (self.size[0] / 4 - 90, self.size[1] * (3/4) + 80), "Quick access", black)
        pygame.draw.rect(self.game.screen, black, (self.size[0] / 4 - 160, self.size[1] * (3/4), 390, 70), 2)

        # LPM + mouse

        self.text.render_to(self.game.screen, (self.size[0] / 2 + 30, self.size[1] * (3/4) + 80), "Atack", black)
        pygame.draw.rect(self.game.screen, black, (self.size[0] / 2, self.size[1] * (3/4) - 70, 140, 140), 2)

        self.text.render_to(self.game.screen, (self.size[0] * (3 / 4) - 100, self.size[1] * (3 / 4) + 80), "Aim", black)
        pygame.draw.rect(self.game.screen, black, (self.size[0] * (3 / 4) - 80, self.size[1] * (3 / 4) - 70, 140, 140), 2)

        # Exit

        exit_x = self.size[0] * (5/6)
        exit_y = self.size[1] / 8 + 10
        exit_x_length = 100
        exit_y_length = 40

        # Button

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if exit_x + exit_x_length > mouse[0] > exit_x and exit_y + exit_y_length > mouse[1] > exit_y:
            self.menu.render_to(self.game.screen, (exit_x, exit_y), "Back" , green)
            pygame.draw.rect(self.game.screen, green, (exit_x, exit_y, exit_x_length, exit_y_length), 2)
            if click[0]:
                self.game.current_screen = self.exit_screen
        else:
            self.menu.render_to(self.game.screen, (exit_x, exit_y), "Back", black)
            pygame.draw.rect(self.game.screen, black, (exit_x, exit_y, exit_x_length, exit_y_length), 2)
