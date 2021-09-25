"""
 Simple graphics demo

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

Water Filter Simulator

author : Edison Qu
course: ICS3U
date: April 8th, 2021

references: Stack Overflow, https://stackoverflow.com/questions/23982907/pygame-how-to-center-text, Simpson College computer science, and Mr. Reid's Class Demos
"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BEIGE = (245,245,220)
DIRTYWATER = (222,184,135)
AQUA = (0,255,255)
LIGHTBLUE = (204,255,255)
WEIRDGREEN = (204,255,204)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TAN = (128,0,0)
POKEMON  = (0,0,0)
DECENTGRAY = (64,64,64)
LIGHTBLUE = (135,206,250)
CHARCOAL = (32,32,32)
STICKS = (153,76,0)
ROCK = (102,51,0)
GRAPHITE = (96,96,96)
DIRT = (51,25,0)
GRASS = (50,205,50)
#Pi
PI = 3.141592653


#classes for boxes and selection

class Boxes():
    def __init__(self):
        self.x = 15
        self.y = 15
        self.height = 80
        self.width = 150
        #different box color for each object
        self.boxcolor = LIGHTBLUE
        self.size = 0
        self.text = 'Sand'
        self.totalScore = 10
        #make sure that it is not repeated
        self.added = False

    def draw(self):
        #basic outline, depending on how big a person wants it, for this example it is 2
        #since the x and y are somewhat correlated to the width and height, you subtract 2 from both
        #so you can add two to the weidth and height so there would be 2 pixels popping out from the original box
        pygame.draw.rect(screen, BLACK, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(screen, self.boxcolor, [self.x, self.y,self.width,self.height],self.size)
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, (0,0,0))
        #centralizing text, taken from https://stackoverflow.com/questions/23982907/pygame-how-to-center-text
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def mouseClick(self,pos):
        #the x mouse's position is after the x coordinate but is still inside the length of the width
        if pos[0] < self.x + self.width and pos[0] > self.x:
            #the y mouse's position is after the y coordinate but is still inside the length of the height
            if pos[1] < self.y + self.height and pos[1] > self.y:
                #if all this is true, return true that it is infact inside the parameters of the box
                return True
        #if not, just ignore
        return False

    def drawTopBottle(self):
        pygame.draw.rect(screen,self.color, (265,100,270,100),0)

    def drawTopMidBottle(self):
        pygame.draw.rect(screen,self.color, (265,200,270,100),0)

    def drawBotMidBottle(self):
        pygame.draw.rect(screen,self.color, (265,300,270,100),0)

    def drawBotBottle(self):
        pygame.draw.rect(screen,self.color, (265,400,270,60),0)
        pygame.draw.polygon(screen,self.color, [[265,460],[535,460],[400,560]],0)



class Water(Boxes):
    def __init__(self):
        #inherit from boxes, as it is still a rectangle
        super().__init__()
        self.change_y = 0
        self.change_y2= 0
        self.color = AQUA
        self.y = 0
    def drawWater(self):
        # the exiting water that goes out
        pygame.draw.rect(screen,self.color, (363,465+self.change_y,75,400))
        #adding increments, to make animation
        self.change_y +=5
        # if it goes out side of where I want it to go, it just bounces back
        if self.change_y > 145 or self.change_y <100:
            #change direction each time it hits those parameters
            self.change_y*=-1
        #increment
        self.y += self.change_y


    def pouring(self, wonOrnot):
        #exiting screen, final scene where it clears everything
        screen.fill(wonOrnot)

        #the dirty water comes pouring in
        pygame.draw.rect(screen,DIRTYWATER,[265,0+self.change_y,270,100],0)

        self.change_y+=3
        # if it hits the cap, start the flowing of the clean/dirty water
        if self.change_y > 260:
            self.change_y = 260
            # turns to true if it hits the cap, so the scoreboard can come as well
            return True

        return False


class Buttons(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 520
        self.width = 100
        self.height = 75
        self.text = 'GO'
        self.boxcolor = DECENTGRAY

    def Button(self):
        super().draw()
        #go button, to start off the final scene of the water pouring
        pygame.draw.rect(screen,self.boxcolor,[self.x,self.y,self.width,self.height],self.size)
        #"GO"
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, (0,0,0))
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))



# all the materials, only documenting the first one as they are all similar, unless otherwise
class Charcoal(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15
        self.height = 80
        self.totalScore = 5
        # different y as it is a different box, adding 100 to increment
        self.y = 15+100
        self.totalScore = 5
        self.width = 150
        self.color = CHARCOAL
        self.text = 'Charcoal'


class Stick(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15
        self.height = 80
        self.y = 15+100+100
        self.width = 150
        self.totalScore = 0
        self.color = STICKS
        self.text = 'Stick'

class Cotton(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15
        self.height = 80
        self.y = 15+100+100+100
        self.width = 150
        self.color = WHITE
        self.text = 'Cotton'

class Rock(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15
        self.height = 80
        self.y = 15+100+100+100+100
        self.width = 150
        self.totalScore = 5

        self.color = ROCK
        self.text = 'Rock'

class Graphite(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15
        self.height = 80
        self.y = 15+100+100+100+100+100
        self.width = 150
        self.totalScore = 0
        self.color = GRAPHITE
        self.text = 'Graphite'

class Gravel(Boxes):
    def __init__(self):
        super().__init__()
        #different x as there needs to be boxes on the right as well
        self.x = 15+620

        self.height = 80
        self.y = 15
        self.width = 150
        self.color = DECENTGRAY
        self.text = 'Gravel'


class Paper(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15+620
        self.height = 80
        self.y = 15 +100
        self.totalScore = 5
        self.width = 150
        self.color = WHITE
        self.text = 'Paper'

class Dirt(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15+620
        self.height = 80
        self.y = 15 +100+100
        self.width = 150
        self.totalScore = 0
        self.color = DIRT
        self.text = 'Dirt'

class coffeeFilter(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15+620
        self.height = 80
        self.y = 15+100+100+100
        self.width = 150
        self.color = WHITE
        self.text = 'Coffee Filter'

class Grass(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15+620
        self.height = 80
        self.y = 15 +100+100+100+100
        self.width = 150
        self.totalScore = 5
        self.color = GRASS
        self.text = 'Grass'

class brokenGlass(Boxes):
    def __init__(self):
        super().__init__()
        self.x = 15+620
        self.height = 80
        self.y = 15 +100+100+100+100+100
        self.totalScore = 0
        self.width = 150
        self.color = (204,255,255)
        self.text = 'Broken Glass'


class Waterbottle():
    def __init__(self):
        self.x = 265
        self.x1 = 535
        self.x2 = 360
        self.y = 40
        self.y1 = 460
        self.y2 = 440
        self.color =LIGHTBLUE
        self.size = 5
        self.capsize = 0
        self.capcolor = LIGHTBLUE

    def draw_body(self):
        #draw the waterbottle
        pygame.draw.line(screen, self.color, [self.x,self.y],[self.x,self.y1],self.size)
        pygame.draw.line(screen, self.color, [self.x1,self.y],[self.x1,self.y1],self.size)

    def draw_neck(self):
        #draw the neck
        pygame.draw.line(screen,self.color, [self.x,self.y1],[self.x2,self.x1],self.size)
        pygame.draw.line(screen,self.color, [self.x1, self.y1],[self.y2,self.x1],self.size)

        pygame.draw.rect(screen,self.capcolor, [self.x2,self.x1,80,25],self.capsize)


class Scoreboard():
    def __init__(self):
        #the scoreboard of panels that say if the water is filtered well and if it is drinkable
        self.x = 580
        self.y = 100
        self.color = WHITE
        self.height = 400
        self. width= 200
    def displayScores(self,win):
        # if it is won, a parameter is here, displays the scores
        # if the score is greater than 75, player wins
        if win:
            self.x = 20
            #outline
            pygame.draw.rect(screen, self.color, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            pygame.draw.rect(screen, WHITE, [self.x,self.y,self.width,self.height])
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render('WATER IS DRINKABLE!', 1, self.color)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        else:
            self.x = 20
            pygame.draw.rect(screen, self.color, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            pygame.draw.rect(screen, WHITE, [self.x,self.y,self.width,self.height])
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render('WATER IS NOT DRINKABLE!', 1, self.color)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        #going back to the 580 parameters as it overwrites after the two scoreboards are put up
        self.x = 580

        pygame.draw.rect(screen, self.color, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(screen, WHITE, [self.x,self.y,self.width,self.height])
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, self.color)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))



#the waterbottle
waterbottle = Waterbottle()

#all the materials
sand = Boxes()
# sand is basically the parent, but the boxes all need to be aqua, here we change it to beige so it is different in waterbottle
sand.color = BEIGE

gravel = Gravel()
cotton = Cotton()
coffeeFilter = coffeeFilter()
paper = Paper()
charcoal = Charcoal()
rocks = Rock()
grass = Grass()
dirt = Dirt()
stick = Stick()
graphite = Graphite()
brokenGlass = brokenGlass()


#the buttons
#go button
go = Buttons()
#remove button
remove = Buttons()
remove.x = 500
remove.boxcolor = RED
remove.text = 'REMOVE'

#the pouring water color depending on the scores
clearWater = Water()

dirtyWater = Water()
dirtyWater.color = (210,180,140)

mediocreWater = Water()
mediocreWater.color = (153,153,0)

reallyDirtyWater = Water()

#scoreboard stuff
perfect = Scoreboard()
perfect.text = 'SCORE: PERFECT'
perfect.color = GREEN

mediocre = Scoreboard()
mediocre.text = 'SCORE: GOOD'
mediocre.color = (102,102,0)

bad = Scoreboard()
bad.text = 'SCORE: BAD'
bad.color = RED



# Set the height and width of the screen
size = (800, 610)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Clean Water Filter")

#counter in order to make sure the GO button isn't pressed before hand
counter = 0

#the scores after taking all the materials are clicked
totalScore = 0
#start when the water hits the cap
start = False
#the list of all the materials currently inside the bottle
inBottle =[]
tryAgain= False
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
# Loop as long as done == False
def wonOrnot(score):
    if score >75:
        return WEIRDGREEN

    elif score >=50 and score <=75:
        return (204,204,0)

    return (255,51,51)


while not tryAgain:
    while not done:


        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                tryAgain = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #make sure that the bottle is empty unless there will be an out of range error
                # make sure the pouring didn't start as the player used to be able to remove when it was poruing
                if inBottle != [] and not start:
                    if remove.mouseClick(pos):
                        #change the color of the box back to blue
                        inBottle[-1].boxcolor = LIGHTBLUE
                        #change it to false, as it was not added, but removed
                        inBottle[-1].added = False
                        #counter subtract so there could be all 4 materials added
                        counter -=1
                        #subtract the total score of the item removed
                        totalScore -= inBottle[-1].totalScore
                        #delete the last item in the list
                        del inBottle[-1]

                if counter == 4:
                    #if all the materials are in the bottle, it will start
                    if go.mouseClick(pos):
                        # if the go button is clicked, the pouring scene will start
                        start = True


                #only going through the first one, as the rest is all the same, unless otherwise
                elif counter <4:
                    # if it is clicked on the sand and if it wasn't already added
                    if sand.mouseClick(pos) and not sand.added:
                        # change the box color ot gray so it tells the user that it has been clicked
                        sand.boxcolor = DECENTGRAY
                        #change the counter to 1 as there is one more added to the list
                        counter +=1
                        #add the score of the score correspondant to the specific material value
                        totalScore += sand.totalScore
                        #make sure that it is added
                        sand.added = True
                        #make sure that it is added to the list
                        inBottle.append(sand)

                    elif gravel.mouseClick(pos) and not gravel.added:
                        gravel.boxcolor = DECENTGRAY
                        counter +=1
                        totalScore += gravel.totalScore


                        inBottle.append(gravel)
                        gravel.added = True

                    elif cotton.mouseClick(pos)and not cotton.added:
                        cotton.boxcolor = DECENTGRAY
                        counter +=1
                        totalScore += cotton.totalScore

                        inBottle.append(cotton)
                        cotton.added = True

                    elif coffeeFilter.mouseClick(pos)and not coffeeFilter.added:
                        coffeeFilter.boxcolor = DECENTGRAY
                        counter +=1
                        totalScore += coffeeFilter.totalScore

                        inBottle.append(coffeeFilter)
                        coffeeFilter.added = True

                    elif paper.mouseClick(pos) and not paper.added:
                        paper.boxcolor = DECENTGRAY
                        counter +=1
                        totalScore += paper.totalScore

                        inBottle.append(paper)
                        paper.added = True

                    elif charcoal.mouseClick(pos)and not charcoal.added:
                        charcoal.boxcolor = DECENTGRAY
                        counter +=1
                        totalScore += charcoal.totalScore

                        inBottle.append(charcoal)
                        charcoal.added = True

                    elif rocks.mouseClick(pos)and not rocks.added:
                        rocks.boxcolor = DECENTGRAY
                        counter +=1
                        totalScore += rocks.totalScore

                        inBottle.append(rocks)
                        rocks.added = True

                    elif grass.mouseClick(pos)and not grass.added:
                        grass.boxcolor = DECENTGRAY
                        counter +=1
                        totalScore += grass.totalScore
                        inBottle.append(grass)
                        grass.added = True

                    #there is no total scores here and below as it would just be 0
                    elif dirt.mouseClick(pos)and not dirt.added:
                        dirt.boxcolor = DECENTGRAY
                        counter +=1

                        inBottle.append(dirt)
                        dirt.added = True

                    elif stick.mouseClick(pos)and not stick.added:
                        stick.boxcolor = DECENTGRAY
                        counter +=1
                        inBottle.append(stick)
                        stick.added = True

                    elif graphite.mouseClick(pos)and not graphite.added:
                        graphite.boxcolor = DECENTGRAY
                        counter +=1
                        inBottle.append(graphite)
                        graphite.added = True

                    elif brokenGlass.mouseClick(pos)and not brokenGlass.added:
                        brokenGlass.boxcolor = DECENTGRAY
                        inBottle.append(brokenGlass)
                        counter +=1
                        brokenGlass.added = True

                    # if it clicked 4 times change the box color to green
                    if counter ==4:
                         go.boxcolor = GREEN
                    else:
                        go.boxcolor = DECENTGRAY


        # All drawing code happens after the for loop and but
        # inside the main while not done loop.
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        # Clear the screen and set the screen background
        screen.fill((224,224,224))

        #drawing the materials
        sand.draw()
        gravel.draw()
        cotton.draw()
        coffeeFilter.draw()
        paper.draw()
        charcoal.draw()
        rocks.draw()
        grass.draw()
        dirt.draw()
        stick.draw()
        graphite.draw()
        brokenGlass.draw()
        #drawing the buttons
        go.Button()
        remove.Button()


        #if go is pressed
        if start:
            score =round((totalScore / 40)*100,2)

                # if it is higher than 75%
            if score >75:
                #you win
                win= True
                #draw out the clean water coming out
                clearWater.drawWater()
                #display the winner scoreboard
                perfect.displayScores(win)

            elif score >=50 and score <=75:
                #win is false
                win = False
                #kinda dirty water
                mediocreWater.drawWater()
                #disdplay that you lost
                mediocre.displayScores(win)

            else:
                win = False
                dirtyWater.drawWater()
                bad.displayScores(win)
            #start the dirty water pouring
            #
            # wonOrnot(score)
            reallyDirtyWater.pouring(wonOrnot(score))

            #if reallydirty water returns as true
            if reallyDirtyWater.pouring(wonOrnot(score)):
                #change the capsize to 0
                waterbottle.capsize= 0
                #chagne the color to white
                waterbottle.capcolor =WHITE
                #round the score when divided to 40 as there are 4 items with teh highest being 10

                # if it is higher than 75%
                if score >75:
                    #you win
                    win= True
                    #draw out the clean water coming out
                    clearWater.drawWater()
                    #display the winner scoreboard
                    perfect.displayScores(win)

                elif score >=50 and score <=75:
                    #win is false
                    win = False
                    #kinda dirty water
                    mediocreWater.drawWater()
                    #disdplay that you lost
                    mediocre.displayScores(win)

                else:
                    win = False
                    dirtyWater.drawWater()
                    bad.displayScores(win)

        #cycle through the items in the bottle
        for item in inBottle:
            #if the item is first, you draw the bottom one
            if item == inBottle[0]:
                item.drawBotBottle()
            # if the item is second you draw the bottom middle one
            elif item == inBottle[1]:
                item.drawBotMidBottle()
            # if the item is third, you draw the top to middle one
            elif item == inBottle[2]:
                item.drawTopMidBottle()
            #if the item is last, you draw it on the top
            else:
                item.drawTopBottle()

        #drwaing the waterbottle, it is always there
        waterbottle.draw_body()
        waterbottle.draw_neck()


        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(60)

# Be IDLE friendly
pygame.quit()