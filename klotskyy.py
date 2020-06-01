import pygame as pg
import sys

pg.init() # Needed to initialize pygame library

WIDTH = 500 # Width of the game's screen
HEIGHT = 500 # Height of the game's screen

screen = pg.display.set_mode((WIDTH, HEIGHT)) # Creating the screen

pg.display.set_caption("Klotski") # Setting the game's name

#Some Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
PINK = (255,182,193)
GREEN = (178,255,102)
BLACK = (0,0,0)
BROWN = (166,128,100)

FPS = 15#Game Speed 

gap = 5#Gap between blocks

clock = pg.time.Clock() # Creating clock object

# List of points inside the board
listOfCoordinates = [(100,100),(155,100),(210,100),(265,100),(100,155),(155,155),(210,155),(265,155),(100,210),(155,210),(210,210),(265,210),(100,265),(155,265),(210,265),(265,265),(100,320),(155,320),(210,320),(265,320),(155,375),(210,375),(155,430),(210,430)]

# List to keep track if a certain coordinate is occupied(True) or not occupied(False) by a block
listOfCoordinatesBool =[False, False, False,False, False, False,False, False, False,False, False, False,False, False, False,False, False, False,False, False, False, False, False, False]

moves = 0 # Number of moves done since the starting board position

class Block():
	
	def __init__(self,x,y): 			
		self.color = color # Color of the block
		self.sizex = 0 # Width of the block
		self.sizey = 0 # Height of the block
		self.x = x # Position x of the block on the screen
		self.y = y # Position y of the block on the screen
		self.rect = pg.Rect(self.x,self.y,self.sizex,self.sizey) # Create a rectangle to manipulate the block 
		self.clicked = False # Check if the block is being clicked(True) or not being clicked(False)
		self.movement = 55 # How much the blocks move(distance between coordinates)
		self.position() # Calls position() when instanciating a block object 


	def position(self): # Determines the coordinates the block is on
		for i, coord in enumerate(listOfCoordinates):
			if self.rect.collidepoint(coord):
				listOfCoordinatesBool[i] = True
		

	def update(self): # Method that calls other needed methods
		self.draw()
		self.move()
		self.position()

	def draw(self): # Draws the block
		pg.draw.rect(screen, self.color, self.rect)


	def possible(self,x,y): # Determines if a block can move to a certain position
		destination = (x,y)
		for i,coord in enumerate(listOfCoordinates):
			if destination == coord:
				if listOfCoordinatesBool[i] == False:
					return True
				else:
					return False
		

	def move(self): # Makes the block slide to where the user drags it
		global moves
		if click: # If the mleft mouse button is clicked
			mx,my = pg.mouse.get_pos() # Get x and y coordinates of the mouse
			if self.rect.collidepoint(mx,my): # If mouse cursor is on the block
				self.clicked = True # The block is being clicked
				self.tupla = (mx,my) # Save cordinates
		elif not click:
			self.clicked = False

		if self.clicked: # If block is being clicked
			mx,my = pg.mouse.get_pos()
			if (mx - self.tupla[0]) > 0: # If the user moves the mouse to the right
				if  my - self.tupla[1] < 0: # If the user moves the mouse up
					if self.rect.left < mx < self.rect.right: # User is moving the block up
						if self.possible(self.rect.x,self.rect.y - self.movement): # Check if that position is clear	
							self.rect.y -= self.movement # Move the block
							self.clicked = False  # The block is no long being clicked 
							resetBool() # Resets listOfCoordinatesBool to then reset the state of the board with self.position() 
							moves += 1 # User made a move
					else: # User is moving the block right
						if self.possible(self.rect.x + self.movement,self.rect.y):
							self.rect.x += self.movement
							self.clicked = False
							resetBool()
							moves += 1
					
				elif my - self.tupla[1] > 0: # If the user moves the mouse down
					if self.rect.left < mx < self.rect.right: # User is moving the block down
						if self.possible(self.rect.x,self.rect.y + self.movement):
							self.rect.y += self.movement
							self.clicked = False
							resetBool()
							moves += 1
					else: # User is moving the block right
						if self.possible(self.rect.x + self.movement,self.rect.y):
							self.rect.x += self.movement
							self.clicked = False
							resetBool()
							moves += 1
				else: # User is only moving the mouse to the right so is moving the block to the right
					if self.possible(self.rect.x + self.movement,self.rect.y):
						self.rect.x += self.movement
						self.clicked = False
						resetBool()
						moves += 1


			if (mx - self.tupla[0] < 0): # If the user moves the mouse to the left
				if my - self.tupla[1] < 0:# If the user moves the mouse up
					if self.rect.left < mx < self.rect.right: # User is moving the block up
						if self.possible(self.rect.x,self.rect.y - self.movement):
							self.rect.y -= self.movement
							self.clicked = False
							resetBool()
							moves += 1
		
					else: # User is moving the block left
						if self.possible(self.rect.x - self.movement, self.rect.y):
							self.rect.x -= self.movement
							self.clicked = False
							resetBool()
							moves += 1
					
				elif my - self.tupla[1] > 0: # If the user moves the mouse down
					if self.rect.left < mx < self.rect.right: # User is moving the block down
						if self.possible(self.rect.x,self.rect.y + self.movement):
							self.rect.y += self.movement
							self.clicked = False
							resetBool()
							moves += 1
					else: # User is moving the block left
						if self.possible(self.rect.x - self.movement, self.rect.y):
							self.rect.x -= self.movement
							self.clicked = False
							resetBool()
							moves += 1
				else: # User is only moving the mouse to the left so is moving the block to the left
					if self.possible(self.rect.x - self.movement, self.rect.y):
						self.rect.x -= self.movement
						self.clicked = False
						resetBool()
						moves += 1

			if my - self.tupla[1] > 0 and mx - self.tupla[0] == 0: # User is only moving the mouse down
				if self.possible(self.rect.x, self.rect.y + self.movement):
					self.rect.y += self.movement
					self.clicked = False
					resetBool()
					moves += 1
					
			if my - self.tupla[1] < 0 and mx - self.tupla[0] == 0: # User is only moving the mouse up
				if self.possible(self.rect.x, self.rect.y - self.movement):
					self.rect.y -= self.movement
					self.clicked = False
					resetBool()
					moves += 1



###Subclasses of Block class
class Red_Block(Block):
	def __init__(self,x,y):	
		self.color = RED
		self.sizex = 105
		self.sizey = 105
		self.x = x
		self.y = y
		self.rect = pg.Rect(self.x,self.y,self.sizex,self.sizey)
		self.movement = 55
		self.position()


	def possible(self,x,y): 
		if y > self.rect.y: 
			destination = (x,y + self.movement)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if not listOfCoordinatesBool[i] and not listOfCoordinatesBool[i+1]:
						return True
					else:
						return False
		elif y < self.rect.y:
			destination = (x,y)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if not listOfCoordinatesBool[i] and not listOfCoordinatesBool[i+1]:
						return True
					else:
						return False
		elif x > self.rect.x: # going right
			destination = (x + self.movement,y)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if not listOfCoordinatesBool[i] and not listOfCoordinatesBool[i+4]:
						return True
					else:
						return False
		else:
			destination = (x,y)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if not listOfCoordinatesBool[i] and not listOfCoordinatesBool[i+4]:
						return True
					else:
						return False
	

class Blue_Block(Block):
	def __init__(self,x,y):	
		self.color = BLUE
		self.sizex = 50
		self.sizey = 105
		self.x = x
		self.y = y
		self.rect = pg.Rect(self.x,self.y,self.sizex,self.sizey) 
		self.movement = 55
		self.position()


	def possible(self,x,y):
		if y > self.rect.y: 
			destination = (x,y + self.movement)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if listOfCoordinatesBool[i] == False:
						return True
					else:
						return False
		elif x > self.rect.x or x < self.rect.x:
			destination = (x,y)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if not listOfCoordinatesBool[i] and not listOfCoordinatesBool[i+4]:
						return True
					else:
						return False
		else:
			destination = (x,y)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if listOfCoordinatesBool[i] == False:
						return True
					else:
						return False


class Green_Block(Block):
	def __init__(self,x,y):		
		self.color = GREEN
		self.sizex = 50
		self.sizey = 50
		self.x = x
		self.y = y
		self.rect = pg.Rect(self.x,self.y,self.sizex,self.sizey)
		self.clicked = False
		self.count = 0
		self.movement = 55
		self.position()
				

class Pink_Block(Block):
	def __init__(self,x,y):		
		self.color = PINK
		self.sizex = 105
		self.sizey = 50
		self.x = x
		self.y = y
		self.rect = pg.Rect(self.x,self.y,self.sizex,self.sizey)
		self.movement = 55
		self.position()


	def possible(self,x,y):
		if x > self.rect.x: 
			destination = (x + self.movement,y)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if listOfCoordinatesBool[i] == False:
						return True
					else:
						return False
		elif y < self.rect.y or y > self.rect.y:
			destination = (x,y)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if not listOfCoordinatesBool[i] and not listOfCoordinatesBool[i+1]:
						return True
					else:
						return False
		else:
			destination = (x,y)
			for i,coord in enumerate(listOfCoordinates):
				if destination == coord:
					if listOfCoordinatesBool[i] == False:
						return True
					else:
						return False

###


fontMR = pg.font.SysFont(None, 40) # Font used to write number of moves and reset
fontG = pg.font.SysFont(None, 20) # Font used to write the goal


click = False # Variable to know if the left mouse button is clicked(True) or not clicked(False) 


def resetBool(): # Makes every item == False in listOfCoordinatesBool
	for i in range(23):
		listOfCoordinatesBool[i] = False

def draw_text(text, font, color, surface, x, y): # Writes text
	textobj = font.render(text,True,color)
	text_rect = textobj.get_rect()
	text_rect.topleft = (x,y)
	surface.blit(textobj, text_rect) 


def game_over(): # Game Over screen

	fontGM = pg.font.SysFont(None,60) # Font used to write on the game over screen

	while True: # Game Over loop
		for event in pg.event.get():
			if event.type == pg.QUIT: # If "X" button on window tab is pressed
				sys.exit() # Exit the game
				pg.quit()

			if event.type == pg.KEYDOWN and event.key == K_ESCAPE: # If "esc" key is pressed
				sys.exit() # Exit the game
				pg.quit()

		screen.fill(BLACK) # Fills the whole screen on black

### Drawing all texts to the screen
		draw_text("Congrats!!! ", fontGM, WHITE, screen, 100, 100)
		draw_text("You won with " + str(moves) + " moves!!!", fontGM, WHITE, screen, 0, 160)
###

		pg.display.update() # Necessary funtion to update the screen
	


def main():
	global click, moves
	### Instanciating all blocks in their starting location
	blueBlock = Blue_Block(100,100)
	blueBlock1 = Blue_Block(265,100)
	blueBlock2 = Blue_Block(100,210)
	blueBlock3 = Blue_Block(265,210)
	redBlock = Red_Block(155,100)
	pinkBlock = Pink_Block(155,210)
	greenBlock = Green_Block(155,265)
	greenBlock1 = Green_Block(210,265)
	greenBlock2 = Green_Block(100,320)
	greenBlock3 = Green_Block(265,320)
	###

	while True: # Game loop

		resetButton = pg.Rect(0,WIDTH - 50,120,50) # Creating a rectangle to manipulate the button

		for event in pg.event.get():
			if event.type == pg.QUIT: # If "X" button on window tab is pressed
				sys.exit() # Exit the game
				pg.quit()
	
			if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: # If "esc" key is pressed
					sys.exit() # Exit the game
					pg.quit()

			if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # If left mouse button is pressed
				click = True
			if event.type == pg.MOUSEBUTTONUP and event.button == 1: # If left mouse button is unpressed
				click = False

		mx,my = pg.mouse.get_pos() # Get coordinate x and y of the mouse position
		if resetButton.collidepoint(mx,my): # If the mouse is on top of the sete button
			if click: # If left mouse button is clicked
				moves = 0
				resetBool() 
				break


		if redBlock.rect.y == 375: # If the red block reaches its goal
			game_over() # Game is over

		screen.fill(BLACK) # Fills the whole screen on black

	
		pg.draw.rect(screen,WHITE,resetButton) # Drawing the reset button
		

### Drawing all texts to the screen
		draw_text("Reset", fontMR, BLACK, screen, 0,WIDTH - 40) # Writing reset on the reset button

		draw_text("Moves : " + str(moves), fontMR, WHITE, screen, 0, 0)

		draw_text("Bring The Red", fontG, RED, screen, 160, 395)
		draw_text("Square Here", fontG, RED, screen, 165, 415)	
###

### Drawing the lines to delimit the board space
		pg.draw.line(screen, BROWN, (95,95), (95,375), 5)
		pg.draw.line(screen, BROWN, (95,95), (320,95), 5)
		pg.draw.line(screen, BROWN, (320,95), (320,375), 5)
		pg.draw.line(screen, BROWN, (95,375), (150,375), 5)
		pg.draw.line(screen, BROWN, (265,375), (320,375), 5)
### 
	

		blueBlock.update()
		redBlock.update()
		blueBlock1.update()
		blueBlock2.update()
		pinkBlock.update()
		blueBlock3.update()
		greenBlock.update()
		greenBlock1.update()
		greenBlock2.update()
		greenBlock3.update()

				
		pg.display.update() # Necessary function to update the screen
	
		clock.tick(FPS) # Set the FPS that the game is going to be ran with


while True:
	main()
