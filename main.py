import pygame
from Grid import *

"""Move class to different file"""


def play_grid(name):
    g = grid()
    # loading grid from storage
    g.load(name)
    s = create_grid("temp", g.size, goal=g)
    print g.body == s.body


# lets the user create a grid (with gui using pygame) and return it. n is the size (n*n) of the grid, name is name.
def create_grid(name, n, goal=None):
    # create grid object to base game window on
    g = grid(name, n, 1)

    # Setting some constants for the game window.
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)
    WIDTH = 20
    HEIGHT = 20
    MARGIN = 5
    FRAME = g.size * 8

    # initialize the pygame module.
    pygame.init()
    # set the size of the window according to the size of the grid.
    size = int(g.size * 25.5)
    WINDOW_SIZE = [size + FRAME, size + FRAME]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Griddlers maker")

    done = False

    clock = pygame.time.Clock()
    # choose font for hint numbers
    font = pygame.font.SysFont("arial", 15)

    # set the describing line according to the goal parameter
    gd = g if goal is None else goal

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = (pos[0] - FRAME) // (WIDTH + MARGIN)
                row = (pos[1] - FRAME) // (HEIGHT + MARGIN)
                print("Click ", pos, "Grid coordinates: ", row, column)
                if event.button == 1:
                    g.fill(row, column)
                elif event.button == 3:
                    g.erase(row, column)

        screen.fill(BLACK)
        """add line description in right places"""

        # render and paint the horizontal and vertical text hints

        for i in range(g.size):
            line = desc_line(gd.row(i))
            text = font.render("  ".join(line), True, WHITE)
            screen.blit(text, (FRAME - len(line) * 12, FRAME + i * (HEIGHT + MARGIN) + 7))
            line = desc_line(gd.col(i))
            # no easy way to blit text with multiple lines in pygame, so i have to do it one num at a time
            for j in range(len(line)):
                text = font.render(line[j], True, WHITE)
                screen.blit(text, (FRAME + i * (HEIGHT + MARGIN) + 7, FRAME - (len(line) - j) * 15))

        # paint grid
        for row in range(g.size):
            for column in range(g.size):
                color = GREY if g[row][column] else WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN + FRAME,
                                  (MARGIN + HEIGHT) * row + MARGIN + FRAME,
                                  WIDTH,
                                  HEIGHT])

        clock.tick(60)

        pygame.display.flip()
    pygame.quit()
    return g

g = grid("test",5,0)
g.save()
g.draw()
play_grid(g.name)
