import pygame
import os
import sys
import random
import datetime

from pygame.locals import * 

SEC = 1000


def load_image(name, colorkey=None):
    if not os.path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(cKey)
    else:
        image = image.convert_alpha()
    return image


def exit():
    pygame.quit()
    sys.exit()


def start_play():
    starting_play_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    run = True
    first_text = ['         Choose']
    text_coord2 = 13
    start_text = ['выбери персонажа:', "", "", "", '              Ок']
    font = pygame.font.Font(None, 100)
    text_coord = 75
    pet = 0
    lines = []
    for line in first_text:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord2 += 13
        intro_rect.top = text_coord2
        intro_rect.x = 70
        text_coord2 += intro_rect.height
        lines.append((string_rendered, intro_rect))
    for line in start_text:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 13
        intro_rect.top = text_coord
        intro_rect.x = 70
        text_coord += intro_rect.height
        lines.append((string_rendered, intro_rect))
    clock = pygame.time.Clock()
    menu_hero = pygame.sprite.Group()
    one = pygame.sprite.Sprite()
    one.image = load_image("big_cat.png")
    one.rect = one.image.get_rect()
    one.rect.x = 100
    one.rect.y = 200
    menu_hero.add(one)
    mam = pygame.sprite.Sprite()
    mam.image = load_image("big_dog.png")
    mam.rect = mam.image.get_rect()
    mam.rect.x = 300
    mam.rect.y = 215
    menu_hero.add(mam)
    rabbit = pygame.sprite.Sprite()
    rabbit.image = load_image("big_rabbit.png")
    rabbit.rect = rabbit.image.get_rect()
    rabbit.rect.x = 500
    rabbit.rect.y = 215
    menu_hero.add(rabbit)
    menu_hero.draw(screen)
    while run:
        for event in pygame.event.get():
            screen.blit(starting_play_bg, (0, 0))
            menu_hero.draw(screen)
            for line in lines:
                screen.blit(line[0], line[1])
            pygame.mouse.set_visible(True)

            pygame.display.flip()
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coor_in_start_play = event.pos
                if 100 < coor_in_start_play[0] < 298 and 200 < coor_in_start_play[1] < 415:
                    one.image = load_image('big_cat.png')
                    mam.image = load_image("big_dog.png")
                    rabbit.image = load_image("big_rabbit.png")
                    pet = 1
                elif 330 < coor_in_start_play[0] < 475 and 215 < coor_in_start_play[1] < 398:
                    mam.image = load_image("big_dog.png")
                    one.image = load_image("big_cat.png")
                    rabbit.image = load_image("big_rabbit.png")
                    pet = 2
                elif 510 < coor_in_start_play[0] < 665 and 220 < coor_in_start_play[1] < 400:
                    rabbit.image = load_image("big_rabbit.png")
                    mam.image = load_image("big_dog.png")
                    one.image = load_image("big_cat.png")
                    pet = 3
                menu_hero.draw(screen)
                if pet != 0:
                    return pet
        pygame.display.flip()
        clock.tick(FPS)


def happy_ending(pet):
    text_win = ['Вы отлично ухаживали за питомцем,', 'он вырос здоровым и счастливым!']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    text_coord = 110
    run = True

    lines = []
    for line in text_win:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        lines.append((string_rendered, intro_rect))

    while run:
        for event in pygame.event.get():
            screen.blit(menu_bg, (0, 0))
            if pet == 1:
                image = load_image('leave_cat.png')
                screen.blit(image, (100, 250))
            elif pet == 2:
                image = load_image('leave_dog.png')
                screen.blit(image, (50, 200))
            elif pet == 3:
                image = load_image('leave_rabbit.png')
                screen.blit(image, (0, 150))

            pygame.mouse.set_visible(True)
            for line in lines:
                screen.blit(line[0], line[1])
            pygame.display.flip()

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
        pygame.display.flip()
        clock.tick(FPS)


def sad_ending(pet):
    text_win = ['К сожалению, вы плохо ухаживали', 'за питомцем, и он ушел.']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    text_coord = 110
    run = True

    lines = []
    for line in text_win:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        lines.append((string_rendered, intro_rect))

    while run:
        for event in pygame.event.get():
            screen.blit(menu_bg, (0, 0))
            if pet == 1:
                image = load_image('leave_cat_sad.png')
                screen.blit(image, (100, 250))
            elif pet == 2:
                image = load_image('leave_dog_sad.png')
                screen.blit(image, (50, 200))
            elif pet == 3:
                image = load_image('leave_rabbit_sad.png')
                screen.blit(image, (0, 150))

            pygame.mouse.set_visible(True)
            for line in lines:
                screen.blit(line[0], line[1])
            pygame.display.flip()

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
        pygame.display.flip()
        clock.tick(FPS)


def start_menu():
    FPS = 60
    menu_text = ['Главное меню','Играть']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(menu_bg, (0, 0))
    run = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 100)
    text_coord = 110
    lines = []
    for line in menu_text:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        lines.append((string_rendered, intro_rect))
    while run:
        for event in pygame.event.get():
            screen.blit(menu_bg, (0, 0))
            for line in lines:
                screen.blit(line[0], line[1])
            pygame.mouse.set_visible(True)

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coor_in_menu = event.pos
                if 270 < coor_in_menu[1] < 350:
                    return 'Игра'
        pygame.display.flip()
        clock.tick(FPS)


class Particle(pygame.sprite.Sprite):

    def __init__(self, pos, dx, dy):
        super().__init__(bub_sprites)
        self.image = random.choice(particles)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = 2

    def update(self):
        screen_rect = (0, 0, 800, 650)
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    particle_count = 30
    numbers = range(-10, 10)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        pet = indicators[3]
        if pet == 1:
            self.image = load_image('cat.png')
            self.image_sleep = load_image('sleep_cat.png')
            self.image_food = load_image('eat_cat.png')
        elif pet == 2:
            self.image = load_image('rabbit.png')
            self.image_sleep = load_image('sleep_rabbit.png')
            self.image_food = load_image('eat_rabbit.png')
        elif pet == 3:
            self.image = load_image('dog.png')
            self.image_sleep = load_image('sleep_dog.png')
            self.image_food = load_image('eat_dog.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 500
        self.speedx = 0
        self.speedy = 0

    def update(self, x1, y1):
        pet = indicators[3]

        if pet == 1:
            self.image = load_image('cat.png')
        elif pet == 3:
            self.image = load_image('rabbit.png')
        elif pet == 2:
            self.image = load_image('dog.png')
        if 110 < x1 < 250 and 250 < y1 < 350:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 250 < x1 < 350 and 225 < y1 < 275:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 220 < x1 < 250 and 250 < y1 < 500:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 250 < x1 < 500 and 450 < y1 < 550:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 350 < x1 < 450 and 400 < y1 < 450:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 350 < x1 < 500 and 550 < y1 < 575:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 500 < x1 < 600 and 500 < y1 < 550:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 175 < x1 < 300 and 175 < y1 < 250 or \
                225 < x1 < 300 and 150 < y1 < 200:
            self.rect.centerx = x1
            self.rect.centery = y1
            self.image = self.image_sleep
        elif 275 < x1 < 350 and 350 < y1 < 450:
            create_particles((x1, y1))
            self.rect.centerx = 800
            self.rect.centery = 800
        elif 450 < x1 < 575 and 400 < y1 < 475:
            self.rect.centerx = x1
            self.rect.centery = y1
            self.image = self.image_food

    
    def random_event(self):
        n = random.randint(0, 32)
        if n == 13:
            indicators[0] += 2
        elif n == 18:
            indicators[0] -= 2
        elif n == 27:
            indicators[1] -= 2
        elif n == 30:
            indicators[1] += 2
        elif n == 4:
            indicators[2] += 2
        elif n == 11:
            indicators[2] -= 2

    def cycle(self):
        self.random_event()
        indicators[0] -= 3
        indicators[1] -= 3
        indicators[2] -= 3
        indicators[4] += 1



def main_play():
    bg = load_image("cub.jpg")
    all_sprites = pygame.sprite.Group()
    player = Hero()
    food_icon = load_image('food_icon.png')
    sleep_icon = load_image('sleep_icon.png')
    soap_icon = load_image('soap_icon.png')
    all_sprites.add(player)

    pygame.time.set_timer(USEREVENT + 1, SEC)
    font = pygame.font.SysFont("jokerman", 40)
    scale_food = font.render("100", True, (255, 255, 255))
    scale_sleep = font.render("100", True, (255, 255, 255))
    scale_soap = font.render("100", True, (255, 255, 255))
    scale_age = font.render("0", True, (255, 255, 255))

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                all_sprites.update(x1, y1)
            elif event.type == pygame.USEREVENT + 1:
                pygame.mouse.set_visible(True)
                x1, y1 = pygame.mouse.get_pos()
             
                is_sleep = False
                is_eat = False
                is_bath = False;
          
                if 175 < x1 < 300 and 175 < y1 < 250 or \
                       225 < x1 < 300 and 150 < y1 < 200:
                    is_sleep = True
                elif 275 < x1 < 350 and 350 < y1 < 450:
                    is_bath = True
                elif 450 < x1 < 575 and 400 < y1 < 475:
                    is_eat = True
          
                if not is_sleep:
                    player.cycle()
                if is_eat:
                    indicators[0] += 5
                if is_sleep:
                    indicators[1] += 5
                    indicators[4] += 1
                if is_bath:
                    indicators[2] += 5
          
                scale_food = font.render(str(indicators[0]), True, (255, 255, 255))
                scale_sleep = font.render(str(indicators[1]), True, (255, 255, 255))
                scale_soap = font.render(str(indicators[2]), True, (255, 255, 255))
                scale_age = font.render(str(indicators[4]), True, (255, 255, 255))
          
                if indicators[0] <= 0 or indicators[1] <= 0 or indicators[2] <= 0:
                    sad_ending(indicators[3]);
          
                if indicators[4] >= 100 and indicators[0] > 0 and indicators[1] > 0 and indicators[2] > 0:
                    happy_ending(indicators[3])
          
        bub_sprites.update()
        bub_sprites.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
        screen.blit(bg, (0, 0))
          
        screen.blit(food_icon, (690, 120))
        screen.blit(sleep_icon, (690, 250))
        screen.blit(soap_icon, (700, 400))
          
        screen.blit(scale_food, (705, 200))
        screen.blit(scale_sleep, (705, 330))
        screen.blit(scale_soap, (705, 475))
        screen.blit(scale_age, (705, 590))

        if indicators[0] <= 0 or indicators[1] <= 0 or indicators[2] <= 0:
            sad_ending(indicators[3]);
          
        if indicators[4] >= 100 and indicators[0] > 0 and indicators[1] > 0 and indicators[2] > 0:
            happy_ending(indicators[3])


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Тамагочи')
    FPS = 60

    particles = [load_image("bubble.png")]
    for scale in (5, 10, 20):
        particles.append(pygame.transform.scale(particles[0], (scale, scale)))
    bub_sprites = pygame.sprite.Group()

    var = start_menu()
    indicators = [100, 100, 100, start_play(), 0]
    if var == 'Игра':
        main_play()
    pygame.quit()
