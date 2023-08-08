
import pygame

WIDTH = 800
HEIGHT = 800

WHITE = (255, 255, 255),

BLACK = (0, 0, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life Game")
clock = pygame.time.Clock()


running = True
setting = True


x_boxes = 30
y_boxes = 30

box_width = WIDTH / x_boxes
box_height = HEIGHT / y_boxes

boxes = []

clicked = [[-1 for _ in range(x_boxes)] for _ in range(y_boxes)]


def check_rule(clicked):
    cells_to_die = []
    cells_to_born = []
    for i in range(len(clicked)):
        for j in range(len(clicked[i])):
            if clicked[i][j] == -1:
                live_cell_count = 0

                rows = [i-1, i, i+1]
                cols = [j-1, j, j+1]
                try:
                    for row in rows:
                        for col in cols:

                            if (row == i) and (col == j):
                                pass
                            else:
                                if clicked[row][col] == 1:
                                    live_cell_count += 1

                    if live_cell_count == 3:
                        cells_to_born.append((i, j))
                except IndexError:
                    pass

            else:
                live_cell_count = 0

                rows = [i-1, i, i+1]
                cols = [j-1, j, j+1]
                try:
                    for row in rows:
                        for col in cols:
                            if (row == i) and (col == j):
                                pass
                            else:
                                if clicked[row][col] == 1:
                                    live_cell_count += 1
                    if (live_cell_count > 3) or (live_cell_count <2):

                        cells_to_die.append((i, j))

                except IndexError:
                    pass

    for i in cells_to_die:

        clicked[i[0]][i[1]] = -1

    for j in cells_to_born:
        clicked[j[0]][j[1]] = 1

    return clicked


def draw_grid(clicked):

    for i in range(x_boxes):
        for j in range(y_boxes):
            if clicked[i][j] == 1:
                color = WHITE
            else:
                color = BLACK
            box = pygame.draw.rect(
                screen,
                color,
                (
                    i*box_width,
                    j*box_height,
                    box_width,
                    box_height,
                )
            )

            boxes.append((box, (i, j)))

    for i in range(1,x_boxes):
        pygame.draw.line(
            screen,
            WHITE,
            ((i*box_width), 0),
            ((i*box_width), HEIGHT),

        )

    for j in range(1,y_boxes):
        pygame.draw.line(
            screen,
            WHITE,
            (0, (j*box_height)),
            (WIDTH, (j*box_height)),

        )

    return boxes


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                setting = not(setting)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if setting:
                for box in boxes:
                    if box[0].collidepoint(pygame.mouse.get_pos()):
                        clicked[box[1][0]][box[1][1]] *= -1

    screen.fill(BLACK)
    if setting:
        pass
    else:
        clicked = check_rule(clicked)

    boxes = draw_grid(clicked)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
