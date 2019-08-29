#Author: Tahfimul Latif
#Date Started: 08/05/2019
#Date Ended: 08/26/2019

import pygame, random, time, os

pygame.init()
w, h = 1000, 1000;
cx, cy = w/2, h/2

screen = pygame.display.set_mode((w,h))

MainBoundary1Verts = [(2, 20), (2, 21), (0, 21), (0, 0), (45, 0), (45, 15), (46, 15), (46, 16), (44, 16), (44, 1), (1, 1), (1, 20)]
MainBoundary2Verts = [(2, 23), (2, 24), (1, 24), (1, 44), (44, 44), (44, 18), (46, 18), (46, 19), (45, 19), (45, 45), (0, 45), (0, 23)]
Inner1BoundaryVerts = [(4, 4), (6, 4), (6, 9), (9, 9), (9, 10), (5, 10), (5, 16), (15, 16), (15, 18), (18, 18), (18, 20), (9, 20), (9, 25), (30, 25), (30, 18), (26, 18), (26, 13), (30, 13), (30, 10), (32, 10), (32, 13), (35, 13), (35, 18), (36, 18), (36, 20), (33, 20), (33, 25), (36, 25), (36, 34), (14, 34), (14, 39), (41, 39), (41, 4), (15, 4), (15, 10), (14, 10), (14, 4), (11, 4), (11, 3), (42, 3), (42, 42),  (4, 42)]
Inner2BoundaryVerts = [(8, 2), (9, 2), (9, 6), (12, 6), (12, 12), (17, 12),(17, 6), (39, 6), (39, 37), (16, 37), (16, 36), (38, 36), (38, 23), (35, 23), (35, 22), (38, 22), (38, 16), (37, 16), (37, 11), (34, 11), (34, 8), (28, 8), (28, 11), (24, 11), (24, 20), (28, 20), (28, 23), (11, 23), (11, 22), (20, 22), (20, 16), (17, 16), (17, 14), (7, 14), (7, 12), (11, 12), (11, 7), (8, 7)]
Track1Verts = [(3, 22), (3, 3), (7, 3), (7, 8), (10, 8), (10, 11), (6, 11), (6, 15), (16, 15), (16, 17), (19, 17), (19, 21), (10, 21), (10, 24), (29, 24), (29, 19), (25, 19), (25, 12), (29, 12), (29, 9), (33, 9), (33, 12), (36, 12), (36, 17), (37, 17), (37, 21), (34, 21), (34, 24), (37, 24), (37, 35), (15, 35), (15, 38), (40, 38), (40, 5), (34, 5), (28, 5), (22, 5), (16, 5), (16, 11), (13, 11), (13, 5), (10, 5), (10, 2), (43, 2), (43, 17)]
Track2Verts = [(0, 22), (3, 22),(3, 43),(43, 43), (43, 17), (46, 17)]

MainBoundaryEdges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 0)]
Inner1BoundaryEdges = [(0,1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 0)]
Inner2BoundaryEdges = [(0,1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 0)]
Track1Edges = [(0,1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 42), (42, 43), (43, 44)]
Track2Edges = [(0,1), (1, 2), (2, 3), (3, 4), (4, 5)]

MainBoundary1Moves = (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_UP), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_UP), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT)
MainBoundary2Moves = (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_UP), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_UP), (pygame.K_RIGHT)
Inner1BOundaryMoves = [(pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_UP), (pygame.K_LEFT), (pygame.K_UP) ,(pygame.K_RIGHT), (pygame.K_UP), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_UP), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_UP), (pygame.K_LEFT), (pygame.K_UP), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_UP)]
Inner2BoundaryMoves = [pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP ,pygame.K_RIGHT ,pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP]
Track1Moves = (pygame.K_UP),(pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_UP), (pygame.K_LEFT), (pygame.K_UP), (pygame.K_RIGHT), (pygame.K_UP), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_UP), (pygame.K_LEFT), (pygame.K_LEFT), (pygame.K_LEFT), (pygame.K_LEFT), (pygame.K_DOWN), (pygame.K_LEFT), (pygame.K_UP), (pygame.K_LEFT), (pygame.K_UP), (pygame.K_RIGHT), (pygame.K_DOWN)
Track2Moves = (pygame.K_RIGHT), (pygame.K_DOWN), (pygame.K_RIGHT), (pygame.K_UP), (pygame.K_RIGHT)

running = 1

BLUE= (32,32,222)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BEIGE = (245,245,220)
RED = (255, 0, 0)
ORANGE = (255, 182, 68)
PINK =  (255, 182, 222)
TEAL = (0, 255, 222)

screen.fill((BLACK))

#Sprite class types
TRACK = 0
BOUNDARY = 1
CHARACTER = 2
REWARD = 3

#Indicator Types
LIFESAVER = 0
LIVE = 1

#Indicator class Msg Types
POINTS = 2
BLINK = 3

#Weights
THICKEST = 13
THICK = 8
THIN = 5
THINNEST = 3

# Pacman movement stuff

# Endzone Constants
ENDZ1 = 111111
ENDZ2 = 222222

Dirs = [pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_LEFT, pygame.K_LEFT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, ENDZ2, pygame.K_LEFT, pygame.K_UP, ENDZ1]

DirRs = [pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_RIGHT, pygame.K_RIGHT, pygame.K_RIGHT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, ENDZ2, pygame.K_UP, pygame.K_RIGHT, ENDZ1]

sparsedTrackLocations = [(3, 3), (7, 3), (7, 8), (10, 8), (10, 11), (6, 11), (6, 15), (16, 15), (16, 17), (19, 17), (19, 21), (10, 21), (10, 24), (29, 24), (29, 19), (25, 19), (25, 12), (29, 12), (29, 9), (33, 9), (33, 12), (36, 12), (36, 17), (37, 17), (37, 21), (34, 21), (34, 24), (37, 24), (37, 35), (15, 35), (15, 38), (40, 38), (40, 5), (34, 5), (28, 5), (22, 5), (16, 5), (16, 11), (13, 11), (13, 5), (10, 5), (10, 2), (43, 2), (43, 17), (43, 43),(3, 43), (3, 22), (0, 22), (46, 17)]

clock = time

class Indicators:
    def __init__(self):
        self.blinkerPos = 0
        self.pointsPos = 0
        self.lifeSaverPos = []
        self.livesPos = []
        self.generatePos()
        self.showing = False
        self.points = 0
        self.createBlinkTextSurface()

    def generatePos(self):
        self.blinkerPos = (0,0)
        self.pointsPos = (4, 0)
        self.lifeSaverPos = [(9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0)]
        self.livesPos = [(20, 0), (21, 0), (22, 0)]
        self.incrementPos()

    def incrementPos(self):

        x, y = self.pointsPos
        x=int((cx/2)+(x-12)*22)
        y=int((cy/2)+(y-10)*22)
        self.pointsPos = (x, y)


        x, y = self.blinkerPos
        x=int((cx/2)+(x-12)*22)
        y=int((cy/2)+(y-10)*22)
        self.blinkerPos = (x, y)

        for i in range(0, len(self.lifeSaverPos)):
            x, y = self.lifeSaverPos[i]
            x=int((cx/2)+(x-12)*22)
            y=int((cy/2)+(y-10)*22)
            self.lifeSaverPos[i] = (x, y)
        for i in range(0, len(self.livesPos)):
            x, y = self.livesPos[i]
            x=int((cx/2)+(x-12)*22)
            y=int((cy/2)+(y-10)*22)
            self.livesPos[i] = (x, y)

    def incrementPoints(self, amount):
        self.points +=amount

    def getLives(self):
        return len(self.livesPos)

    def remove(self, type):
        if type == LIFESAVER:
            del self.lifeSaverPos[0]
        else:
            del self.livesPos[0]

    def createBlinkTextSurface(self):
        currDir = os.path.dirname(os.path.abspath(__file__))
        fontDir = os.path.join(currDir, 'resources/font/ARCADE_N.TTF')
        largeText = pygame.font.Font(fontDir,20)
        TextSurf, TextRect = self.text_objects("1 UP", largeText)
        self.blinkTextSurface = TextSurf, TextRect


    def text_objects(self, text, font):
        textSurface = font.render(text, True, YELLOW)
        return textSurface, textSurface.get_rect()

    def showMsg(self, text, type):
        currDir = os.path.dirname(os.path.abspath(__file__))
        fontDir = os.path.join(currDir, 'resources/font/ARCADE_N.TTF')
        largeText = pygame.font.Font(fontDir,20)
        TextSurf, TextRect = self.text_objects(text, largeText)

        pos = -1
        if type == BLINK:
            pos = self.blinkerPos
            self.showing = True
        else:
            pos = self.pointsPos

        TextRect.center = ((pos))
        screen.blit(TextSurf, TextRect)


    def hideMsg(self):
        screen.blit(screen.copy(), (0,0))
        self.showing = False

    def showPoints(self):
        self.showMsg(str(self.points), POINTS)

    def blink1Up(self):
        shown = 0
        if self.showing:
            screen.blit(self.screen, (0,0))
            self.showing = False
            shown = 1
        if shown == 0:
            self.screen = screen.copy()
            screen.blit(self.blinkTextSurface[0], self.blinkTextSurface[1])
            self.showing = True

    def draw(self):
        self.blink1Up()
        self.showPoints()

        for x, y in self.lifeSaverPos:
            pygame.draw.circle(screen, YELLOW, (x, y), THICK)

        for x, y in self.livesPos:
            pygame.draw.circle(screen, RED, (x, y), THICK)

class Enemies:
    def __init__(self, trackLocations):
        self.colors = [RED, ORANGE, PINK, TEAL]
        self.weight = THICKEST
        self.trackVerts = trackLocations
        self.enemyStartPos = []
        self.enemyPos = []
        self.startingPoints = [(70, 110), (150, 110), (150, 210), (210, 210), (690, 150),(570, 150), (450, 150), (330, 150), (330, 270), (270, 270), (270, 150), (210, 150), (210, 90), (870, 90), (870, 910)]
        self.lifeSaverModeOn = 0
        self.lifeSaverModeOnTimestamp = -1
        self.lifeSaverModeOnColor = BLUE
        self.lifeSaverModeOnEaten = [0, 0, 0, 0]
        self.generateStartPositions()

    def generateStartPositions(self):
        for i in range(0, 4):
            while 1:
                num = random.randint(0, len(self.startingPoints)-1)
                location = self.startingPoints[num]
                trackLocationsIndex = self.trackVerts.index(location)
                if not trackLocationsIndex in self.enemyPos:
                    self.enemyPos+=[trackLocationsIndex]
                    self.enemyStartPos+=[trackLocationsIndex]
                    break

    def resetPos(self):
        for i in range(0, 4):
            self.enemyPos[i] = self.enemyStartPos[i]

    def move(self):
        for i in range(0, 4):
            print(str(self.lifeSaverModeOnEaten)+" lifeSaverModeOnEaten | move enemies lifeSaverModeOnEaten "+str(self.lifeSaverModeOnEaten[i])+" equality "+str(self.lifeSaverModeOnEaten[i] != 0))
            if self.lifeSaverModeOn == 1 and self.lifeSaverModeOnEaten[i] != 0:
                if self.lifeSaverModeOnEaten[i] is 1:
                    print("len of lifeSaverModeOnEaten "+str(len(self.lifeSaverModeOnEaten)))
                    if self.enemyPos[i] < self.enemyStartPos[i]-29 and self.enemyPos[i] < len(self.trackVerts)-29:
                        print("moving forward "+str(i))
                        self.enemyPos[i] += 30
                    if self.enemyPos[i] < self.enemyStartPos[i] and self.enemyPos[i] > self.enemyStartPos[i]-29 and self.enemyPos[i] < len(self.trackVerts)-29:
                        print("moving forward "+str(i))
                        self.enemyPos[i] += self.enemyStartPos[i] - self.enemyPos[i]
                if self.lifeSaverModeOnEaten[i] is -1:
                    if self.enemyPos[i] > self.enemyStartPos[i]+29 and self.enemyPos[i] > 30:
                        print("moving back "+str(i))
                        self.enemyPos[i] -= 30
                    if self.enemyPos[i] > self.enemyStartPos[i] and self.enemyPos[i] < self.enemyStartPos[i]+29 and self.enemyPos[i] > 0:
                        print("moving back "+str(i))
                        self.enemyPos[i] -= self.enemyPos[i] - self.enemyStartPos[i]

                if self.enemyPos[i] == self.enemyStartPos[i]:
                    print("Enemy Pos "+str(i)+" is "+str(self.enemyPos[i])+" starts Pos "+str(self.enemyStartPos))
                    self.lifeSaverModeOnEaten[i] = 0

            if self.lifeSaverModeOn == 0 or self.lifeSaverModeOn == 1 and self.lifeSaverModeOnEaten[i] == 0:
                if self.enemyPos[i] < len(self.trackVerts)-1:
                    print("moving forward regular"+str(i))
                    self.enemyPos[i] +=1

                else:
                    self.enemyPos[i] = 0


    def draw(self):
        if self.lifeSaverModeOn == 1:
            currTime = int(clock.time())
            timeDiff = currTime - self.lifeSaverModeOnTimestamp
            print("time diff "+str(timeDiff)+" enemyPos "+str(self.enemyPos)+" trackVerts len "+str(len(self.trackVerts))+" lifeSaverModeOnEaten "+str(self.lifeSaverModeOnEaten))
            if timeDiff <= 5:
                if self.lifeSaverModeOnColor == WHITE:
                    self.lifeSaverModeOnColor = BLUE
                for i in range(0, 4):
                    pygame.draw.circle(screen, self.lifeSaverModeOnColor, self.trackVerts[self.enemyPos[i]], self.weight)
            if timeDiff > 5 and timeDiff < 10:
                set = 0
                if self.lifeSaverModeOnColor == BLUE:
                    self.lifeSaverModeOnColor = WHITE
                    set = 1
                if set==0:
                    self.lifeSaverModeOnColor = BLUE

                for i in range(0, 4):
                    pygame.draw.circle(screen, self.lifeSaverModeOnColor, self.trackVerts[self.enemyPos[i]], self.weight)
            if timeDiff >= 10:
                self.setLifeSaverModeOff()
        if self.lifeSaverModeOn == 0:
            print(" enemyPos "+str(self.enemyPos)+" trackVerts len "+str(len(self.trackVerts)))
            for i in range(0, 4):
                pygame.draw.circle(screen, self.colors[i], self.trackVerts[self.enemyPos[i]], self.weight)

    def getLocations(self):
        return self.enemyPos

    def collided(self, location):
        val = (0, -1)

        for i in self.enemyPos:
            if location == self.trackVerts[i]:
                print("enemyPosI collided "+str(self.enemyPos.index(i)))
                val = (1, self.enemyPos.index(i))

        return val

    def setLifeSaverModeOn(self, timestamp):
        self.lifeSaverModeOn = 1
        self.lifeSaverModeOnTimestamp = timestamp

    def setLifeSaverModeOnEaten(self, PosI, dir):
        self.lifeSaverModeOnEaten[PosI] = dir

    def setLifeSaverModeOff(self):
        self.lifeSaverModeOn = 0
        self.lifeSaverModeOnTimestamp = -1
        self.lifeSaverModeOnColor = BLUE
        self.lifeSaverModeOnEaten = [0, 0, 0, 0]

    def getLifeSaverMode(self):
        return self.lifeSaverModeOn

    def remove(self, locationI):
        self.enemyPos.remove(locationI)

    def getStartPos(self, i):
        return self.enemyStartPos[i]


class Coins:
    def __init__(self, trackLocations):
        self.locations = trackLocations
        self.color = YELLOW
        self.weight = THINNEST
        self.drawnPos = []
        self.generateLocations()

    def generateLocations(self):
        self.drawnPos = []
        i = 50
        for location in self.locations:
            if i is 50:
                self.drawnPos += [location]
                i = 0
            else:
                i+=1

    def remove(self, location):
        self.drawnPos.remove(location)

    def eaten(self, location):
        return location in self.drawnPos

    def draw(self):
        print(str(len(self.drawnPos))+" len drawnPos | len locations "+str(len(self.locations)))
        for pos in self.drawnPos:
            pygame.draw.circle(screen, self.color, pos, self.weight)

class LifeSavers:
    def __init__(self, trackLocations):
        self.color = BEIGE
        self.weight = THICK
        self.trackLocations = trackLocations
        self.locations = []
        self.generateLocations()

    def generateLocations(self):
        self.locations = []
        for i in range(0, 8):
            while 1:
                location = self.generateLocation()
                if not location in self.locations:
                    self.append(location)
                    break;

    def generateLocation(self):
        num = random.randint(0, len(self.trackLocations)-1)
        return self.trackLocations[num]

    def append(self, location):
        self.locations+=[location]
        self.trackLocations.remove(location)


    def remove(self, location):
        self.locations.remove(location)

    def getTrackLocations(self):
        return self.trackLocations

    def draw(self):
        for location in self.locations:
            pygame.draw.circle(screen, self.color, location, self.weight)

    def eaten(self, location):
        return location in self.locations

class Sprite:
    def __init__(self, pos, color, type):
        self.pos = pos
        pygame.display.update()
        self.locations = [pos]
        self.color = color
        if type == TRACK:
            self.thickness = THICKEST
        if type == BOUNDARY:
            self.thickness = THICK
        if type == CHARACTER:
            self.thickness = THICK
        if type == REWARD:
            self.thickness = THIN

        self.draw()

    def move(self, key, val):
        if(key==pygame.K_UP):
            y = self.pos[1]-val
            self.pos=(self.pos[0], y)
            print('move up')
        if(key==pygame.K_DOWN):
            y = self.pos[1]+val
            self.pos=(self.pos[0], y)
            print('move down')
        if(key==pygame.K_RIGHT):
            x = self.pos[0]+val
            self.pos=(x, self.pos[1])
            print('move right')
        if(key==pygame.K_LEFT):
            x = self.pos[0]-val
            self.pos=(x, self.pos[1])
            print('move left')
        self.draw()
        pygame.display.update()
        self.appendToLocations()

    def moveTo(self, location):
        self.pos = location
        self.draw()

    def draw(self):
        self.shape = pygame.draw.circle(screen, self.color, self.pos, self.thickness)

    def appendToLocations(self):
        self.locations += [self.pos]

    def getPos(self):
        return self.pos

    def getLocations(self):
        return self.locations

class Map:

    def __init__(self):
        self.i = 0
        self.trackLocations = []
        self.textShown = False
        self.screen = screen.copy()

    def resetI(self):
        self.i = 0

    def incrementI(self):
        self.i += 1

    def text_objects(self, text, font):
        textSurface = font.render(text, True, YELLOW)
        return textSurface, textSurface.get_rect()

    def showMessage(self):
        self.screen = screen.copy()
        text = "Loading..."
        currDir = os.path.dirname(os.path.abspath(__file__))
        fontDir = os.path.join(currDir, 'resources/font/ARCADE_N.TTF')
        largeText = pygame.font.Font(fontDir,50)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((cx),(cy))
        screen.blit(TextSurf, TextRect)
        self.textShown = True

    def hideMessage(self):
        screen.blit(self.screen, (0,0))
        self.textShown = False

    def drawMap(self):
        self.incrementVerts()
        self.createSprites()
        self.drawOutlines()

    def incrementVerts(self):
        self.incrementMainBoundary1Verts()
        self.incrementMainBoundary2Verts()
        self.incrementTrack1Verts()
        self.incrementTrack2Verts()
        self.incrementInner1BoundaryVerts()
        self.incrementInner2BoundaryVerts()

    def createSprites(self):
        self.MainBoundary1 = Sprite((int(MainBoundary1Verts[0][0]), int(MainBoundary1Verts[0][1])), BLUE, BOUNDARY)
        self.MainBoundary2 = Sprite((int(MainBoundary2Verts[0][0]), int(MainBoundary2Verts[0][1])), BLUE, BOUNDARY)
        self.track1 = Sprite((Track1Verts[0][0], Track1Verts[0][1]), BLACK, TRACK)
        self.track2 = Sprite((Track2Verts[0][0], Track2Verts[0][1]), BLACK, TRACK)
        self.Inner1Boundary = Sprite((int(Inner1BoundaryVerts[0][0]), int(Inner1BoundaryVerts[0][1])), BLUE, BOUNDARY)
        self.Inner2Boundary = Sprite((int(Inner2BoundaryVerts[0][0]), int(Inner2BoundaryVerts[0][1])), BLUE, BOUNDARY)

    def drawOutlines(self):
        self.outlineMainBoundary1Moves()
        self.outlineMainBoundary2Moves()
        self.outlineTrack1Moves()
        self.outlineTrack2Moves()
        self.outlineInner1BoundaryMoves()
        self.outlineInner2BoundaryMoves()

    def incrementMainBoundary1Verts(self):
        for x, y in MainBoundary1Verts:
                x=int((cx/2)+(x-12)*20)
                y=int((cy/2)+(y-10)*20)
                MainBoundary1Verts[self.i] = (x, y)
                self.incrementI()

        self.resetI()

    def incrementMainBoundary2Verts(self):
        for x, y in MainBoundary2Verts:
                x=int((cx/2)+(x-12)*20)
                y=int((cy/2)+(y-10)*20)
                MainBoundary2Verts[self.i] = (x, y)
                self.incrementI()
        self.resetI()

    def incrementTrack1Verts(self):
        for x,y in Track1Verts:
            x=int((cx/2)+(x-12)*20)
            y=int((cy/2)+(y-10)*20)
            Track1Verts[self.i] = (x, y)
            self.incrementI()
        self.resetI()

    def incrementTrack2Verts(self):
        for x,y in Track2Verts:
            x=int((cx/2)+(x-12)*20)
            y=int((cy/2)+(y-10)*20)
            Track2Verts[self.i] = (x, y)
            self.incrementI()
        self.resetI()

    def incrementInner1BoundaryVerts(self):
        for x, y in Inner1BoundaryVerts:
                x=int((cx/2)+(x-12)*20)
                y=int((cy/2)+(y-10)*20)
                Inner1BoundaryVerts[self.i] = (x, y)
                self.incrementI()
        self.resetI()

    def incrementInner2BoundaryVerts(self):
        for x, y in Inner2BoundaryVerts:
                x=int((cx/2)+(x-12)*20)
                y=int((cy/2)+(y-10)*20)
                Inner2BoundaryVerts[self.i] = (x, y)
                self.incrementI()
        self.resetI()

    def outlineMainBoundary1Moves(self):
        for move in MainBoundary1Moves:
            while 1:
                shown = 0
                if self.textShown:
                    self.hideMessage()
                    shown = 1
                if shown == 0:
                    self.showMessage()


                print(str(self.MainBoundary1.getPos())+' Main Boundary 1 verts '+str(MainBoundary1Verts[MainBoundaryEdges[self.i][1]]) + ' point ' + str(self.i))

                if self.MainBoundary1.getPos() == MainBoundary1Verts[MainBoundaryEdges[self.i][1]]:
                    break

                self.MainBoundary1.move(move, 1)

            self.incrementI()
        self.resetI()

    def outlineMainBoundary2Moves(self):
        for move in MainBoundary2Moves:
            while 1:
                shown = 0
                if self.textShown:
                    self.hideMessage()
                    shown = 1
                if shown == 0:
                    self.showMessage()
                print(str(self.MainBoundary2.getPos())+' MainBoundary2 verts '+str(MainBoundary2Verts[MainBoundaryEdges[self.i][1]]) + ' point ' + str(self.i))

                if self.MainBoundary2.getPos() == MainBoundary2Verts[MainBoundaryEdges[self.i][1]]:
                    break

                self.MainBoundary2.move(move, 1)

            self.incrementI()
        self.resetI()

    def outlineTrack1Moves(self):
        for move in Track1Moves:
            while 1:
                shown = 0
                if self.textShown:
                    self.hideMessage()
                    shown = 1
                if shown == 0:
                    self.showMessage()
                print(str(self.track1.getPos())+' track verts '+str(Track1Verts[Track1Edges[self.i][1]]))

                if self.track1.getPos() == Track1Verts[Track1Edges[self.i][1]]:
                    break

                self.track1.move(move, 1)
                self.trackLocations += [self.track1.getPos()]

            self.incrementI()
        self.resetI()

    def outlineTrack2Moves(self):
        for move in Track2Moves:
            while 1:
                shown = 0
                if self.textShown:
                    self.hideMessage()
                    shown = 1
                if shown == 0:
                    self.showMessage()

                print(str(self.track2.getPos())+' track verts '+str(Track2Verts[Track2Edges[self.i][1]]))

                if self.track2.getPos() == Track2Verts[Track2Edges[self.i][1]]:
                    break

                self.track2.move(move, 1)
                self.trackLocations += [self.track2.getPos()]
            self.incrementI()
        self.resetI()

    def outlineInner1BoundaryMoves(self):
        for move in Inner1BOundaryMoves:
            while 1:
                shown = 0
                if self.textShown:
                    self.hideMessage()
                    shown = 1
                if shown == 0:
                    self.showMessage()
                print(str(self.Inner1Boundary.getPos())+' Inner1Boundary verts '+str(Inner1BoundaryVerts[Inner1BoundaryEdges[self.i][1]]) + ' point ' + str(self.i))

                if self.Inner1Boundary.getPos() == Inner1BoundaryVerts[Inner1BoundaryEdges[self.i][1]]:
                    break

                self.Inner1Boundary.move(move, 1)

            self.incrementI()
        self.resetI()

    def outlineInner2BoundaryMoves(self):
        for move in Inner2BoundaryMoves:
            while 1:
                shown = 0
                if self.textShown:
                    self.hideMessage()
                    shown = 1
                if shown == 0:
                    self.showMessage()
                print(str(self.Inner2Boundary.getPos())+' Inner2Boundary verts '+str(Inner2BoundaryVerts[Inner2BoundaryEdges[self.i][1]]) + ' point ' + str(self.i))

                if self.Inner2Boundary.getPos() == Inner2BoundaryVerts[Inner2BoundaryEdges[self.i][1]]:
                    screen.blit(self.screen, (0,0))
                    break

                self.Inner2Boundary.move(move, 1)
            self.incrementI()
        self.resetI()
    def getTrackLocations(self):
        return self.trackLocations

class Game:
    def __init__(self):
        self.map = Map()
        self.map.drawMap()
        self.Background = screen.copy()
        self.LifeSavers = LifeSavers(self.map.getTrackLocations())
        self.Coins = Coins(self.LifeSavers.getTrackLocations())
        self.pac = Sprite((Track1Verts[29]), YELLOW, CHARACTER)
        self.enemies = Enemies(self.map.getTrackLocations())
        self.indicators = Indicators()
        self.initialBG = screen.copy()
        self.msgShown = 0
        self.collisionPosI = 0
        self.incrementSparsedTrackVerts()
        self.gameOverSfx = 'resources/sfx/game_over.wav'
        self.coinEatenSfxI = -1
        self.coinEatenSfx = ['resources/sfx/coin_eaten_0.wav','resources/sfx/coin_eaten_1.wav', 'resources/sfx/coin_eaten_2.wav', 'resources/sfx/coin_eaten_3.wav']
        self.inGameSfx = 'resources/sfx/in_game.wav'
        self.gameStartSfx = 'resources/sfx/game_start.wav'
        self.enemyEatenSfx = 'resources/sfx/enemy_eaten.wav'
        self.inGameSfxPlayed = 0
        pygame.mixer.init()

    def init(self):
        self.drawScreen()
        key = -1
        pygame.mixer.music.load(self.gameStartSfx)
        pygame.mixer.music.play()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    break

            if key != -1:
                break

            game.preStart()
            self.drawScreen()

        game.startGame()

    def playNextCoinEatenSfx(self):
        if self.coinEatenSfxI < len(self.coinEatenSfx)-1:
            self.coinEatenSfxI+=1
        else:
            self.coinEatenSfxI = 0
        pygame.mixer.music.load(self.coinEatenSfx[self.coinEatenSfxI])
        pygame.mixer.music.play()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, YELLOW)
        return textSurface, textSurface.get_rect()

    def showMsg(self, text):
        currDir = os.path.dirname(os.path.abspath(__file__))
        fontDir = os.path.join(currDir, 'resources/font/ARCADE_N.TTF')
        largeText = pygame.font.Font(fontDir,50)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((cx),(cy))
        screen.blit(TextSurf, TextRect)
        self.msgShown = True

        pygame.display.update()


    def hideMsg(self, BG):
        screen.blit(BG, (0,0))
        self.msgShown = False
        pygame.display.update()

    def preStart(self):
        pygame.time.delay(1000)
        shown = 0
        if self.msgShown:
            print("hiding Msg")
            self.hideMsg(self.initialBG)
            shown = 1
        if shown == 0:
            print("showing msg")
            self.showMsg("Press a key...")

    def incrementSparsedTrackVerts(self):
        i = 0
        for x, y in sparsedTrackLocations:
                x=int((cx/2)+(x-12)*20)
                y=int((cy/2)+(y-10)*20)
                sparsedTrackLocations[i] = (x, y)
                i+=1

    def gameOver(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.gameOverSfx)
        pygame.mixer.music.play()
        self.showMsg("Game Over")
        pygame.time.delay(4000)

        self.pac.moveTo((Track1Verts[29]))
        self.enemies.resetPos()
        self.Coins.generateLocations()
        self.LifeSavers.generateLocations()
        self.indicators.generatePos()
        self.init()

    def draw(self, key, nextPos):
        while 1:
            if clock.time()-self.inGameSfxPlayed >= 1:
                pygame.mixer.music.load(self.inGameSfx)
                self.inGameSfxPlayed = clock.time()
                pygame.mixer.music.play()
            if self.collision():
                if self.enemies.getLifeSaverMode() == 0:
                    if self.indicators.getLives() == 1:
                        break
                    else:
                        self.indicators.remove(LIVE)
                        self.resetGame()
                    break

                else:
                    self.setEnemyEaten()
                    self.indicators.incrementPoints(200)

            if self.pac.getPos() == nextPos:
                break
            self.pac.move(key, 1)
            if self.collision():
                if self.enemies.getLifeSaverMode() == 0:
                    self.resetGame()
                    break

                else:
                    self.setEnemyEaten()

            self.check()
            print("key in Dirs "+str(self.pac.getPos())+" nextPos "+str(nextPos)+" currLocationI "+str(self.currLocationI)+" currLocationI + 1 "+str(self.currLocationI+1))
            self.drawScreen()

    def drawScreen(self):
        screen.blit(self.Background, (0,0))
        self.pac.draw()
        self.enemies.move()
        self.enemies.draw()
        self.Coins.draw()
        self.LifeSavers.draw()
        self.indicators.draw()


    def resetGame(self):
        if pygame.mixer.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(self.gameOverSfx)
        pygame.mixer.music.play()
        pygame.time.delay(4000)
        self.pac.moveTo((Track1Verts[29]))
        self.enemies.resetPos()

    def setEnemyEaten(self):
        print("collisionPosI "+str(self.collisionPosI)+" enemyPos[collisionPosI] "+str(self.enemies.getLocations()[self.collisionPosI])+" enemyStartPos[collisionPosI] "+str(self.enemies.getStartPos(self.collisionPosI)))
        if self.enemies.getLocations()[self.collisionPosI] < self.enemies.getStartPos(self.collisionPosI):
            self.enemies.setLifeSaverModeOnEaten(self.collisionPosI, 1)
            print("collisionPosI "+str(self.collisionPosI)+" enemyPos[collisionPosI] "+str(self.enemies.getLocations()[self.collisionPosI])+" enemyStartPos[collisionPosI] "+str(self.enemies.getStartPos(self.collisionPosI))+" dir 1")
        if self.enemies.getLocations()[self.collisionPosI] > self.enemies.getStartPos(self.collisionPosI):
            self.enemies.setLifeSaverModeOnEaten(self.collisionPosI, -1)
            print("collisionPosI "+str(self.collisionPosI)+" enemyPos[collisionPosI] "+str(self.enemies.getLocations()[self.collisionPosI])+" enemyStartPos[collisionPosI] "+str(self.enemies.getStartPos(self.collisionPosI))+" dir -1")


    def collision(self):
        pacPos = self.pac.getPos()
        bool, i = self.enemies.collided(pacPos)
        if bool == 1:
            self.collisionPosI = i
            return True

        return False


    def checkLifeSaverEaten(self):
        if self.LifeSavers.eaten(self.pac.getPos()):
            print("eaten called")
            pygame.mixer.music.load(self.enemyEatenSfx)
            pygame.mixer.music.play()
            self.indicators.remove(LIFESAVER)
            self.LifeSavers.remove(self.pac.getPos())
            self.enemies.setLifeSaverModeOn(clock.time())

    def checkCoinEaten(self):
        if self.Coins.eaten(self.pac.getPos()):
            if pygame.mixer.get_busy():
                pygame.mixer.music.stop()
            self.playNextCoinEatenSfx()
            self.Coins.remove(self.pac.getPos())
            self.indicators.incrementPoints(10)

    def check(self):
        self.checkLifeSaverEaten()
        self.checkCoinEaten()


    def startGame(self):
        screen.blit(self.Background, (0,0))
        self.inGameSfxPlayed = clock.time()
        while 1:
            if self.collision():
                print("collision DETECTED | lifeSaverModeOn "+str(self.enemies.getLifeSaverMode()))
                if self.enemies.getLifeSaverMode() == 0:
                    if self.indicators.getLives() == 1:
                        break
                    else:
                        self.indicators.remove(LIVE)
                        self.resetGame()

                if self.enemies.getLifeSaverMode() == 1:
                    self.setEnemyEaten()
                    self.indicators.incrementPoints(200)

            print(str(pygame.mixer.get_busy())+" mixer MSUIC")

            if clock.time()-self.inGameSfxPlayed >= 1:
                pygame.mixer.music.load(self.inGameSfx)
                self.inGameSfxPlayed = clock.time()
                pygame.mixer.music.play()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pacPos = self.pac.getPos()
                    self.currLocationI = sparsedTrackLocations.index(pacPos)
                    key = event.key
                    print(str(self.currLocationI)+" currLocationI | Dirs[currLocationI] "+str(Dirs[self.currLocationI])+" equals "+ str(Dirs[self.currLocationI]==key) +" | DirRs[currLocationI] "+str(DirRs[self.currLocationI])+" key "+str(key))
                    if Dirs[self.currLocationI] == key:
                        print("key in Dirs ")
                        nextPos = sparsedTrackLocations[self.currLocationI+1]
                        self.draw(key, nextPos)
                        print(str(pacPos)+" nextPos "+str(nextPos)+" point "+str(self.currLocationI+1))
                        key = 999999
                    if DirRs[self.currLocationI] == key:
                        print("key in DirRs ")
                        if self.currLocationI == 0:
                            nextPos = sparsedTrackLocations[46]
                        else:
                            nextPos = sparsedTrackLocations[self.currLocationI-1]
                        self.draw(key, nextPos)
                        key = 999999
                    if DirRs[self.currLocationI] == ENDZ1 or Dirs[self.currLocationI] == ENDZ1:
                        print("ENDZ1 ")
                        if key == pygame.K_LEFT:
                            print(" LEFT ")
                            nextPos = sparsedTrackLocations[47]
                            self.draw(key, nextPos)
                            self.drawScreen()
                            self.pac.moveTo(sparsedTrackLocations[48])
                            nextPos = sparsedTrackLocations[43]
                            self.draw(key, nextPos)
                        if key == pygame.K_DOWN:
                            nextPos = sparsedTrackLocations[45]
                            self.draw(key, nextPos)
                        if key == pygame.K_UP:
                            nextPos = sparsedTrackLocations[0]
                            self.draw(key, nextPos)
                        key = 999999


                    if DirRs[self.currLocationI] == ENDZ2 or Dirs[self.currLocationI] == ENDZ2:
                        print("ENDZ2 ")
                        if key == pygame.K_RIGHT:
                            nextPos = sparsedTrackLocations[48]
                            self.draw(key, nextPos)
                            self.drawScreen()
                            self.pac.moveTo(sparsedTrackLocations[47])
                            nextPos = sparsedTrackLocations[46]
                            self.draw(key, nextPos)
                        if key == pygame.K_UP:
                            nextPos = sparsedTrackLocations[42]
                            self.draw(key, nextPos)

                        if key == pygame.K_DOWN:
                            nextPos = sparsedTrackLocations[44]
                            self.draw(key, nextPos)
                        key = 999999
            self.drawScreen()
            pygame.display.update()
        self.gameOver()

game = Game()

game.init()
