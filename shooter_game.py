import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()
FPS = 60
max_bullets = 5

bullets_left = max_bullets
reload_time = 3000 
last_reload = 0
reloading = False
background = pygame.image.load("galaxy.jpg").convert()
lives = 3
green = (0, 255, 0)
pygame.mixer.music.load("backrooms.ogg")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

fire_sound = pygame.mixer.Sound("fire.ogg")
fire_sound.set_volume(0.7)

font = pygame.font.Font(None, 36)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, speed=0):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(player_image).convert_alpha(),
            (w, h)
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def reset(self, surface):
        surface.blit(self.image, self.rect)
class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-150, -40)
            self.rect.x = random.randint(0, WIDTH - self.rect.width)

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def fire(self):
        global bullets_left, reloading, last_reload
        if bullets_left > 0 and not reloading:
            bullet = Bullet("bullet.png", self.rect.centerx - 7, self.rect.top, 14, 24, 10)
            bullets.add(bullet)
            fire_sound.play()
            bullets_left -= 1

            if bullets_left == 0:
                reloading = True
                last_reload = pygame.time.get_ticks()

class Enemy(GameSprite):
    def update(self):
        global missed
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            missed += 1
            global lives
            lives -= 1
            self.rect.y = random.randint(-150, -40)
            self.rect.x = random.randint(0, WIDTH - self.rect.width)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

ship = Player("rocket.png", 310, 380, 80, 100, 6)

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

for i in range(5):
    if i == 0:
        a = Asteroid(
            "asteroid.png", 
            random.randint(0, WIDTH - 80),
            random.randint(-150, -40),
            80, 80,
            1 
        )
        asteroids.add(a)
    else:
        e = Enemy(
            "ufo.png",
            random.randint(0, WIDTH - 80),
            random.randint(-150, -40),
            80, 50,
            random.randint(2, 5)
        )
        enemies.add(e)

score = 0
missed = 0

game_over = False
win = False

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                ship.fire()

    

    if not game_over:
        ship.update()
        enemies.update()
        bullets.update()
        asteroids.update()

        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        if hits:
            score += len(hits)
            for _ in range(len(hits)):
                e = Enemy(
                    "ufo.png",
                    random.randint(0, WIDTH - 80),
                    random.randint(-150, -40),
                    80, 50,
                    random.randint(2, 5)
                )
                enemies.add(e)

        if pygame.sprite.spritecollide(ship, enemies, False):
            game_over = True
            win = False

        if lives <= 0:
            game_over = True
            win = False

        if score >= 10:
            game_over = True
            win = True
    
    if reloading:
        now = pygame.time.get_ticks()
        if now - last_reload >= reload_time:
            bullets_left = max_bullets
            reloading = False

    window.blit(background, (0, 0))

    ship.reset(window)
    enemies.draw(window)
    bullets.draw(window)
    asteroids.draw(window)

    text_lives = font.render(str(lives), True, (0, 255, 0))
    window.blit(text_lives, (WIDTH - text_lives.get_width() - 10, 10))

    text_score = font.render(f"Hit: {score}", True, (255, 255, 255))
    text_missed = font.render(f"Missed: {missed}", True, (255, 255, 255))
    window.blit(text_score, (10, 10))
    window.blit(text_missed, (10, 45))

    if pygame.sprite.spritecollide(ship, asteroids, False):
        game_over = True
        win = False

    if reloading:
        reload_text = font.render("wait... reloading", True, (255, 0, 0))
        window.blit(reload_text, (WIDTH // 2 - reload_text.get_width() // 2, HEIGHT - 40))

    if game_over:
        msg = "YOU WIN!" if win else "YOU LOSE!"
        text_end = font.render(msg, True, (255, 220, 0))
        window.blit(text_end, (WIDTH // 2 - text_end.get_width() // 2, HEIGHT // 2 - 20))

    pygame.display.update()

pygame.quit()