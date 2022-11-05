import pygame
import function
from config import *
from sprite import *

class main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920,1080))
        self.clock = pygame.time.Clock()

        self.map = function.create_map(80,45)
        self.create_sprite()
        self.mouse = [0,0,False]
        self.start = False
        self.save_map = self.map

        self.spaceDown = False
        self.sta = 0

        self.gameloop()

    def create_sprite(self):
        self.sprites = []
        self.Sprites = pygame.sprite.Group()
        
        for i in range(45):
            for j in range(80):
                new = sprite((j,i),self.Sprites,self.map)
                self.sprites.append(new)
        
    def gameloop(self):
        while True:
            self.clock.tick(60)
            self.update()
            self.screen.fill((86,86,86))
            self.draw()
            pygame.display.update()

    def update(self):
        self.mouse[0],self.mouse[1] = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                function.save(self.map)
                pygame.quit()
                import sys;sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse[2] = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse[2] = False

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.spaceDown:
            self.spaceDown = True
            self.start = not self.start
            if self.start:
                function.save(self.map);print(True)
            else:
                self.map = function.create_map(80,45)

        elif not(key[pygame.K_SPACE]):
            self.spaceDown = False

        if self.start:
            self.sta +=1
            if self.sta >= SPEED:
                add = []
                for i in range(45):
                    for j in range(80):
                        grid = self.get_grid(j,i)
                        if grid == 3:
                            add.append((j,i))

                delete = []
                for i in range(45):
                    for j in range(80):
                        grid = self.get_grid(j,i)
                        if not(grid == 2 or grid == 3):
                            delete.append((j,i))

                for  a in add:
                    self.map[a[1]][a[0]] = True
                for  b in delete:
                    self.map[b[1]][b[0]] = False
                self.sta = 0

        for Sprite in self.sprites:
            Sprite.update(self.map,self.start,self.mouse)

    def draw(self):
        self.Sprites.draw(self.screen)

    def get_grid(self,x,y):
        grid = []
        if x-1<0:
            grid.append(0)
        elif self.map[y][x-1]:
            grid.append(1)
        else:
            grid.append(0)
        
        if x-1<0 or y-1<0:
            grid.append(0)
        elif self.map[y-1][x-1]:
            grid.append(1)
        else:
            grid.append(0)
        
        if y-1<0:
            grid.append(0)
        elif self.map[y-1][x]:
            grid.append(1)
        else:
            grid.append(0)
        
        if x+1>=80:
            grid.append(0)
        elif self.map[y][x+1]:
            grid.append(1)
        else:
            grid.append(0)
        
        if x+1>=80 or y+1>=45:
            grid.append(0)
        elif self.map[y+1][x+1]:
            grid.append(1)
        else:
            grid.append(0)
        
        if x+1>=80 or y-1<0:
            grid.append(0)
        elif self.map[y-1][x+1]:
            grid.append(1)
        else:
            grid.append(0)
        
        if y+1>=45:
            grid.append(0)
        elif self.map[y+1][x]:
            grid.append(1)
        else:
            grid.append(0)

        if  x-1<0 or y+1>=45:
            grid.append(0)
        elif self.map[y+1][x-1]:
            grid.append(1)
        else:
            grid.append(0)

        gg = 0
        for d in grid:
            gg+=d
        return gg

if __name__=='__main__':
    main()