import pygame


WIDTH, HEIGHT = 1280, 720


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # 加载背景图片
    background = pygame.image.load('./resource/images/background1.jpg').convert()
    # 截取一部分背景图片
    sub_surface = background.subsurface(pygame.Rect(120, 0, 900, 600))
    # 如果背景图片尺寸与窗口大小不匹配，可以对其进行缩放适应窗口大小
    background = pygame.transform.scale(sub_surface, (WIDTH, HEIGHT))
    bg_rect = background.get_rect()
    clock = pygame.time.Clock()

    # 加载僵尸图片
    zombie_img = pygame.image.load("./resource/images/zombies/idle/idle_00.png").convert_alpha()
    zombie = pygame.sprite.Sprite()
    zombie.image = zombie_img
    zombie.rect = zombie_img.get_rect(center=(WIDTH, HEIGHT/2))
    # 僵尸的移动速度
    zombie_speed = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fill the screen with a color to wipe away anything from last frame
        # screen.blit(sub_surface, ((WIDTH-900)//2, (HEIGHT-600)//2))
        screen.blit(background, bg_rect)

        # 绘制僵尸
        screen.blit(zombie.image, zombie.rect)

        # RENDER YOUR GAME HERE
        zombie.rect.x -= zombie_speed

        if zombie.rect.right <= 0:
            zombie.rect.right = WIDTH

        # 更新屏幕
        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
