# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license
#
# Modified by Beatzoid
# 7/1/21
# Modifications
# - Main Menu
# - Wall Wrapping
# - Bad and good apples

import random
import pygame
import sys
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 600
WINDOWHEIGHT = 400
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

TIMETOWAIT = 0
TIMEELAPSED = 0

#             R    G    B
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
DARKGREEN = (0, 155,   0)
DARKGRAY = (40,  40,  40)
YELLOW = (255, 255, 0)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0  # syntactic sugar: index of the worm's head


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    global FPS, TIMEELAPSED, TIMETOWAIT

    # Set a random start point.
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    # Start the apple in a random place.
    apple = {"position": getRandomLocation(), "type": "normal"}

    while True:  # main game loop
        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # If the worm collides with itself
        for wormBody in wormCoords[1:]:
            if wormBody["x"] == wormCoords[HEAD]["x"] and wormBody["y"] == wormCoords[HEAD]["y"]:
                return

        # Wrap the snake when it hits a wall
        if wormCoords[HEAD]["x"] == CELLWIDTH + 1:
            wormCoords[HEAD]["x"] = 0
        elif wormCoords[HEAD]["y"] == CELLHEIGHT + 1:
            wormCoords[HEAD]["y"] = 0
        elif wormCoords[HEAD]["x"] == -1:
            wormCoords[HEAD]["x"] = CELLWIDTH
        elif wormCoords[HEAD]["y"] == -1:
            wormCoords[HEAD]["y"] = CELLHEIGHT

        if TIMETOWAIT != 0:
            checkFPSResetTime()


        # check if worm has eaten an apple
        if wormCoords[HEAD]['x'] == apple["position"]["x"] and wormCoords[HEAD]["y"] == apple["position"]["y"]:
            if apple["type"] == "boost":
                FPS = 10 # Easier
                resetFPS()
            elif apple["type"] == "poison":
                FPS = 20 # Harder
                resetFPS()
            apple = generateApple()
        else:
            del wormCoords[-1]  # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]
                       ['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]
                       ['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def checkFPSResetTime():
    global TIMEELAPSED, TIMETOWAIT, FPS

    TIMEELAPSED += 100
    if TIMEELAPSED == TIMETOWAIT:
        TIMETOWAIT = 0
        TIMEELAPSED = 0
        FPS = 15


def resetFPS():
    global TIMETOWAIT, TIMEELAPSED
    TIMETOWAIT = 5000
    TIMEELAPSED = 0
    
def button(text, coords):
    font = pygame.font.Font('freesansbold.ttf', 30)
    buttonText = font.render(text, True, WHITE, DARKGREEN)
    buttonRect = buttonText.get_rect()
    buttonRect.topleft = coords
    DISPLAYSURF.blit(buttonText, buttonRect)
    return buttonRect

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        titleSurf = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
        playButton = titleSurf.get_rect()
        playButton.topleft = (120, 0)
        DISPLAYSURF.blit(titleSurf, playButton)

        playButton = button("Play", (270, 150))
        quitButton = button("Quit", (270, 200))

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if playButton.collidepoint(mouse):
                    return # Start the game
                elif quitButton.collidepoint(mouse):
                    terminate() # End the game

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3  # rotate by 3 degrees each frame
        degrees2 += 7  # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return


def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawLives(lives):
    livesSurf = BASICFONT.render('Lives: %s' % (lives), True, WHITE)
    livesRect = livesSurf.get_rect()
    livesRect.topleft = (WINDOWWIDTH - 120, 30)
    DISPLAYSURF.blit(livesSurf, livesRect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(
            x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)


def drawApple(apple):
    x = apple["position"]["x"] * CELLSIZE
    y = apple["position"]["y"] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

    if apple["type"] == "normal":
        pygame.draw.rect(DISPLAYSURF, RED, appleRect)
    elif apple["type"] == "boost":
        pygame.draw.rect(DISPLAYSURF, YELLOW, appleRect)
    elif apple["type"] == "poison":
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, appleRect)

def generateApple():
    if random.randint(1, 10) == 1: # 10%
        return {"position": getRandomLocation(), "type": "boost"}
    elif random.randint(1, 20) == 1: # 5%
        return {"position": getRandomLocation(), "type": "poison"}
    else:
        return {"position": getRandomLocation(), "type": "normal"}


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()
