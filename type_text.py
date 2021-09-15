# will draw strings on a surface at a slower pace to simulate a typing effect. Can handle two lines.


import pygame


# simulate printing text one character at a time on the screen
class TextPrint:
    def __init__(self, xpos, ypos, fontSize, fontColor, string, gameSurface, speed, padding):
        self.xpos = xpos
        self.ypos = ypos
        self.font = pygame.font.SysFont('Lucida Console', fontSize)
        self.fontColor = fontColor
        self.displayText = string
        self.surf = pygame.Surface((0,0))
        self.rect = self.surf.get_rect()
        self.active = False # is the text area currently in use - NOT USED 9/15/2021
        self.activeIndex = 0 # index that is being added to current render
        self.gameSurface = gameSurface # pass in the surface you want to draw on
        self.timer = 0 # to slow the bliting to simulate type
        self.timerReset = speed # speed at which text prints to screen, lower is faster
        self.newLine = False # did text have to move to a new line?
        self.lastIndex = None # last index before moving to new line
        self.padding = padding # buffer so text doesn't run right to the edge of the screen
        self.finished = False # flag for determing if the string has reached the end of its updates, useful if looping through a list and don't want object drawing at the same itme
    

    def newLinePrep(self):
        self.newLineSurf = None
        self.newLineRect = None

    def update(self):
        if self.timer == 0:

            if not self.newLine: # if there is not a new line yet
                self.surf = self.font.render(self.displayText[:self.activeIndex], True, self.fontColor)
                self.rect = self.surf.get_rect(x=self.xpos,y=self.ypos)
                # handle if text grows larger than screen area
                # horizontal
                if self.surf.get_width() + self.rect.x >= self.gameSurface.get_width() - self.padding:
                    self.newLine = True

                    # handle new line in the middle of a word
                    # work in progess - 9/15/2021

                    self.lastIndex = self.activeIndex
                    self.newLinePrep()
                    
                
            
            else:
                self.newLineSurf = self.font.render(self.displayText[self.lastIndex:self.activeIndex], True, self.fontColor)
                self.newLineRect = self.newLineSurf.get_rect(x=self.xpos,y=self.ypos + self.surf.get_height())

            if self.activeIndex >= len(self.displayText): self.finished = True # stop advancing index when it reaches the end of string length
            else: self.activeIndex += 1

        self.timer += 1
        if self.timer == self.timerReset: self.timer = 0

    
    def draw(self):
        self.gameSurface.blit(self.surf, self.rect)
        if self.newLine and self.newLineSurf != None:
            self.gameSurface.blit(self.newLineSurf, self.newLineRect)



    


        

    





