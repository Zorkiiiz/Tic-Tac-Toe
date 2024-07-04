import pygame
from pygame.locals import *

pygame.init()

leaderboard_p1 = 0
leaderboard_p2 = 0

screen = pygame.display.set_mode((300, 300), HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption("Tic Tac Dawgs")

# Define colors
green = (0,255,0)
red = (255,0,0)
blue = (0, 0,255)
# Define font
font = pygame.font.SysFont('None', 40)
smlfont = pygame.font.SysFont('None', 30)

# Variables
line_width = 9
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    square_width = screen.get_width() // 3
    square_height = screen.get_height() // 3
    for i in range(3):
        pygame.draw.line(screen, grid, (i * square_width, 0), (i * square_width, screen.get_height()), line_width)
        pygame.draw.line(screen, grid, (0, i * square_height), (screen.get_width(), i * square_height), line_width)
def markers_appnd():
    for i in range(3):
        row = [0] * 3
        markers.append(row)

markers_appnd()

def draw_markers():
    for x_index, row in enumerate(markers):
        for y_index, cell in enumerate(row):
            center_x = x_index * screen.get_width() // 3 + screen.get_width() // 6
            center_y = y_index * screen.get_height() // 3 + screen.get_height() // 6

            # Determine the size of the X and O based on the cell size
            marker_size = min(screen.get_width(), screen.get_height()) // 3 // 3  # Ratio

            if cell == 1:
                # Draw X in the cell
                pygame.draw.line(screen, green, (center_x - marker_size, center_y - marker_size),
                                 (center_x + marker_size, center_y + marker_size), line_width)
                pygame.draw.line(screen, green, (center_x + marker_size, center_y - marker_size),
                                 (center_x - marker_size, center_y + marker_size), line_width)
            elif cell == -1:
                # Draw O in the cell
                pygame.draw.circle(screen, red, (center_x, center_y), marker_size,
                                   line_width)

def check_winner():

    global winner
    global game_over
    global leaderboard_p1
    global leaderboard_p2

    y_pos = 0
    for x in markers:
        # Check Collumns
        if sum(x) == 3:
            winner = 1
            leaderboard_p1 += 1
            game_over = True

        if sum(x) == -3:
            winner = 2
            leaderboard_p2 += 1
            game_over = True

        # Check Rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            leaderboard_p1 += 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            leaderboard_p2 += 1
            game_over = True
        y_pos += 1

    # Check Diagonals
    if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[0][2]+markers[1][1]+markers[2][0] == 3:
        winner = 1
        leaderboard_p1 += 1
        game_over = True
    if markers[0][0]+markers[1][1]+markers[2][2] == -3 or markers[0][2]+markers[1][1]+markers[2][0] == -3:
        winner = 2
        leaderboard_p2 += 1
        game_over = True

    # Check Draw
    if all(element != 0 for row in markers for element in row):
        winner = 4
        game_over = True
    else:
        return

def draw_Winner(winner):
    if winner == 4:
        win_txt = 'Draw!'
        win_img = font.render(win_txt, True, blue)
        pygame.draw.rect(screen, green, (screen.get_width() // 2 - 100, screen.get_height() // 2 - 130, 200, 50))
        screen.blit(win_img, (screen.get_width() // 2 - 45, screen.get_height() // 2 - 120))
    else:
        win_txt = 'Player ' + str(winner) + ' wins!'
        win_img = font.render(win_txt, True, blue)
        pygame.draw.rect(screen, green, (screen.get_width() // 2 -100, screen.get_height() // 2 - 130, 200, 50))
        screen.blit(win_img, (screen.get_width() // 2 - 96, screen.get_height() // 2 - 120))

    leaderboard_txt = 'Leaderboard:'
    leaderboard_img = font.render(leaderboard_txt, True, blue)
    pygame.draw.rect(screen, green, (screen.get_width() // 2 -100, screen.get_height() // 2 - 65, 200, 100))
    screen.blit(leaderboard_img, (screen.get_width() // 2 - 95, screen.get_height() // 2 - 60))

    p1_txt = 'Player 1 Score: ' + str(leaderboard_p1)
    p1_img = smlfont.render(p1_txt, True, blue)
    screen.blit(p1_img, (screen.get_width() // 2 - 90, screen.get_height() // 2 - 30))

    p2_txt = 'Player 2 Score: ' + str(leaderboard_p2)
    p2_img = smlfont.render(p2_txt, True, blue)
    screen.blit(p2_img, (screen.get_width() // 2 - 90, screen.get_height() // 2 - 0))

    again_text = 'Play Again'
    again_img = font.render(again_text, True, blue)
    again_rect = pygame.Rect(screen.get_width() // 2 - 90, screen.get_height() // 2 + 60, 165, 50)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen.get_width() // 2 - 80, screen.get_height() // 2 + 70))

run = True
while run:

    draw_grid()
    draw_markers()
    # Create again rect
    again_rect = pygame.Rect(screen.get_width() // 2 - 90, screen.get_height() // 2 + 60, 165, 50)

    # Add event handlers
    for event in pygame.event.get():
        # Quitting
        if event.type == pygame.QUIT:
            run = False

        # Resize window
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), HWSURFACE|DOUBLEBUF|RESIZABLE)

        # Mouse click
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            elif event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // (screen.get_width() // 3)
                cell_y = pos[1] // (screen.get_height() // 3)
                if markers[cell_x][cell_y] == 0:
                    markers[cell_x][cell_y] = player
                    player *= -1
                    check_winner()

    # Check user hit 'Play Again' button
    if game_over == True:
        draw_Winner(winner)
        # Check mouse click if user click on play again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # Reset variables
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                markers_appnd()

    pygame.display.update()

pygame.quit()