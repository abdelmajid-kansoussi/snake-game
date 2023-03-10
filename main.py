import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGTH = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (40, 40, 40)
GREEN = (0, 255, 0)
DARKGREEN = (0, 140, 0)
RED = (255, 0, 0)

FPS = 15

RIGHT = "right"
LEFT = "left"
DOWN = "down"
UP = "up"

BOARDWIDTH = 30
BOARDHEIGHT = 30
CELLSIZE = WINDOWWIDTH / BOARDWIDTH

HEAD = -1
TAIL = 0

def main():
    global CLOCK, DISPLAYSURF
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGTH))
    pygame.display.set_caption("snake game")
    CLOCK = pygame.time.Clock()

    DISPLAYSURF.fill(BLACK)
    drawKeyPressMsg()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                runGame()
                drawKeyPressMsg()
                drawGameOverMsg()
        pygame.display.update()
        CLOCK.tick(FPS)

def runGame():
    score = 0
    snake = [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}]
    apple = getRandomCell(snake)
    direction = RIGHT

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP and event.key == K_UP and direction != DOWN:
                direction = UP
            elif event.type == KEYUP and event.key == K_DOWN and direction != UP:
                direction = DOWN
            elif event.type == KEYUP and event.key == K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.type == KEYUP and event.key == K_RIGHT and direction != LEFT:
                direction = RIGHT

        if snake[HEAD]["x"] == -1 or snake[HEAD]["x"] >= BOARDWIDTH or snake[HEAD]["y"] == -1 or snake[HEAD]["y"] >= BOARDHEIGHT:
            return
        if snake[HEAD] in snake[:HEAD]:
            return

        if snake[HEAD]["x"] == apple["x"] and snake[HEAD]["y"] == apple["y"]:
            score += 1
            apple = getRandomCell(snake)
        else:
            del snake[TAIL]

        if direction == LEFT:
            snake.append({"x": snake[HEAD]["x"] - 1, "y": snake[HEAD]["y"]})
        elif direction == RIGHT:
            snake.append({"x": snake[HEAD]["x"] + 1, "y": snake[HEAD]["y"]})
        elif direction == UP:
            snake.append({"x": snake[HEAD]["x"], "y": snake[HEAD]["y"] - 1})
        elif direction == DOWN:
            snake.append({"x": snake[HEAD]["x"], "y": snake[HEAD]["y"] + 1})

        

        DISPLAYSURF.fill(BLACK)
        drawGrid()
        drawApple(apple)
        drawSnake(snake)
        drawScore(score)

        pygame.display.update()
        CLOCK.tick(FPS)

def drawKeyPressMsg():
    font = pygame.font.Font("freesansbold.ttf", 20)
    pressKeySurf = font.render("PRESS ANY KEY TO START", False, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.center = (WINDOWWIDTH / 2, WINDOWHEIGTH / 2 + 50)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def getRandomCell(snakeCoords):
    cells = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            cell = {"x": x, "y": y}
            if cell not in snakeCoords:
                cells.append(cell)
    random.shuffle(cells)
    return cells[0]

def drawGrid():
    for x in range(BOARDWIDTH):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (CELLSIZE * x, 0), (CELLSIZE * x, WINDOWHEIGTH))
    for y in range(BOARDHEIGHT):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, CELLSIZE * y), (WINDOWWIDTH, CELLSIZE * y))

def drawApple(appleCoord):
    pygame.draw.rect(DISPLAYSURF, RED, (CELLSIZE * appleCoord["x"], CELLSIZE * appleCoord["y"], CELLSIZE, CELLSIZE))

def drawSnake(snakeCoord):
    for coord in snakeCoord:
        pygame.draw.rect(DISPLAYSURF, GREEN, (CELLSIZE * coord["x"], CELLSIZE * coord["y"], CELLSIZE, CELLSIZE))
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, (CELLSIZE * coord["x"], CELLSIZE * coord["y"], CELLSIZE, CELLSIZE), 3)

def drawScore(score):
    font = pygame.font.Font("freesansbold.ttf", 20)
    scoreSurf = font.render("score: " + str(score), False, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawGameOverMsg():
    font = pygame.font.Font("freesansbold.ttf", 80)
    gameOverSurf = font.render("GAME OVER", False, WHITE)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (WINDOWWIDTH / 2, WINDOWHEIGTH / 2 - 50)
    DISPLAYSURF.blit(gameOverSurf, gameOverRect)



main()