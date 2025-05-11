from pygame import *


win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('Maze')
background = transform.scale(image.load('fon.png'), (win_width, win_height))

font.init()
font = font.Font(None, 70)
win = font.render('You win!', True, (255, 216, 0))
lose = font.render('You lose!', True, (180, 0, 0))

mixer.init()
mixer.music.load('Fantasy.mp3')
mixer.music.play()

clock = time.Clock()
FPS = 120

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(self.image.load(player_image), (70, 70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x > win_width - 70:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_height = wall_height
        self.wall_width = wall_width

        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = Player('player.jpg', 40, 370, 2)
monster = Enemy('teleport.png', win_width - 70, 270, 2)
scarb = GameSprite('Fantasygun.png', win_width - 70, 370, 0)

wall1 = Wall(150, 23, 203, 1, 1, 698, 8)#
wall2 = Wall(150, 23, 203, 691, 1, 8, 498)#
wall3 = Wall(150, 23, 203, 1, 491, 698, 8)#
wall4 = Wall(150, 23, 203, 1, 5, 8, 498)#
wall5 = Wall(150, 23, 203, 120, 100, 8, 398)#
wall6 = Wall(150, 23, 203, 220, 1, 8, 398)#
wall7 = Wall(150, 23, 203, 320, 100, 8, 398)#
wall8 = Wall(150, 23, 203, 420, 1, 8, 398)#
wall9 = Wall(150, 23, 203, 520, 200, 8, 296)#

game = True

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        scarb.reset()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7) or sprite.collide_rect(player, wall8) or sprite.collide_rect(player, wall9):
            finish = True
            window.blit(lose, (200, 200))

        if sprite.collide_rect(player, scarb):
            finish = True
            window.blit(win, (200, 200))

    display.update()
    clock.tick(FPS)