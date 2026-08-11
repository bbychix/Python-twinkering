import pygame

# Setting up the Display/(800, 800)
Screen_Title = 'Cross Ahead'
Screen_Width = 800
Screen_Height = 800
# Colors according to RGB renders & fps visual
White_colour = (255, 255, 255)
Black_colour = (0, 0, 0)
# Game Events update and frames
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


class Game:

    Tick_rate = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        # Creating window size with background colour:)
        self.game_window = pygame.display.set_mode((width, height))
        self.game_window.fill(White_colour)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('PlayerPoke.png', 375, 700, 50, 50)
        enemy_character = EnemyCharacter('enemyPoke.png', 20, 600, 70, 70)
        enemy_character.SPEED *= level_speed

        enemy_character2 = EnemyCharacter('enemyPoke.png', self.width - 40, 400, 70, 70)
        enemy_character2.SPEED *= level_speed

        enemy_character3 = EnemyCharacter('enemyPoke.png', 20, 200, 70, 70)
        enemy_character3.SPEED *= level_speed

        treasure = GameObject('treasureCenter.png', 375, 50, 70, 70)

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            self.game_window.fill(White_colour)
            self.game_window.blit(self.image, (0, 0))

            treasure.draw(self.game_window)

            player_character.move(direction, self.height)
            player_character.draw(self.game_window)

            enemy_character.move(self.width)
            enemy_character.draw(self.game_window)

            if level_speed > 2:
                enemy_character2.move(self.width)
                enemy_character2.draw(self.game_window)
            if level_speed > 4:
                enemy_character3.move(self.width)
                enemy_character3.draw(self.game_window)

            if player_character.detect_collision(enemy_character):
                is_game_over = True
                did_win = False
                text = font.render('You Lose!', True, Black_colour)
                self.game_window.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(enemy_character2):
                is_game_over = True
                did_win = False
                text = font.render('You Lose!', True, Black_colour)
                self.game_window.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
            elif player_character.detect_collision(enemy_character3):
                is_game_over = True
                did_win = False
                text = font.render('You Lose!', True, Black_colour)
                self.game_window.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render("You Win!", True, Black_colour)
                self.game_window.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break
            # Game.blit should be (375, 375)
            # Game graphics Update

            pygame.display.update()
            clock.tick(self.Tick_rate)
        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class PlayerCharacter(GameObject):

    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False

        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True


class EnemyCharacter(GameObject):

    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


pygame.init()

new_game = Game('BackgroundPoke.png', Screen_Title, Screen_Width, Screen_Height)
new_game.run_game_loop(1)
pygame.quit()
quit()
