import time

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

    # 加载僵尸移动图片
    walk_frame = []
    for i in range(31):
        if i < 10:
            i = f"0{i}"
        zombie_frame = pygame.image.load(f"./resource/images/zombies/idle/idle_{i}.png").convert_alpha()
        walk_frame.append(zombie_frame)

    # 僵尸角色位置，速度
    zombie_speed = 3
    zombie_x = WIDTH / 2
    zombie_y = HEIGHT / 5

    # 动画参数设置
    WALK_FRAME_RATE = 31    # 每一秒播放15帧
    current_frame = 0
    last_frame_update = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fill the screen with a color to wipe away anything from last frame
        screen.blit(background, bg_rect)

        # 更新动画
        current_time = pygame.time.get_ticks()
        print("-----", current_time)
        time_since_last_update = current_time - last_frame_update
        if time_since_last_update >= 1000 // WALK_FRAME_RATE:    # 判断是否到达切换帧的时间
            current_frame = (current_time + 1) % len(walk_frame)
            last_frame_update = current_frame
            pygame.time.wait(148)

        zombie_x -= zombie_speed

        screen.blit(walk_frame[current_frame], (zombie_x, zombie_y))

        if zombie_x <= 0:
            zombie_x = WIDTH

        # 更新屏幕
        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
