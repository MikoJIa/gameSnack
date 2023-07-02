import pygame, sys, time, random


frame_size_x = 720
frame_size_y = 480


pygame.init() #  инициализируем все необходимые модули pygame
pygame.display.set_caption('Snack')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))  # используем для
# отображения окна нужного нам размера


white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)

fps_controller = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10,
            random.randrange(1, (frame_size_y//10)) * 10]

food_spawn = True
direction = 'RIGHT'
change_to = direction

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'

    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score = score + 1
        food_pos = [random.randrange(1, (frame_size_x // 10)) * 10,
                    random.randrange(1, (frame_size_y // 10)) * 10]
    else:
        snake_body.pop()

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0],
                                                     food_pos[1],
                                                     10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x:
        pygame.quit()
        sys.exit()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y:
        pygame.quit()
        sys.exit()

    for block in snake_body[2:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps_controller.tick(20)

