from utils import check_letters
from errors import ValueTooSmallError, ValueTooLargeError, AlphaError, OffGridError, CrashError

class Rover:
	def __init__(self, x, y, direction, instructions, grid):
		self.x = int(x)
		self.y = int(y)
		self.direction = direction.upper()
		self.instructions = instructions
		self.grid = grid
		self.grid[self.x][self.y] = self.direction

	def make_move(self):
		if(not len(self.instructions)):
			return False
		move = self.instructions[0]
		self.instructions = self.instructions[1:]
		d = ('N', 'E', 'S', 'W')

		if(move.lower() == 'l'):
			ind = d.index(self.direction)
			self.direction = d[ind-1]
			self.grid[self.x][self.y] = self.direction

		elif(move.lower() == 'r'):
			ind = d.index(self.direction)
			self.direction = d[(ind+1)%4]
			self.grid[self.x][self.y] = self.direction

		else:
			try:
				if(self.direction.lower() == 'n'):
					if(self.y+1==len(self.grid[0])):
						raise OffGridError
					if(self.grid[self.x][self.y+1] == ''):
						self.grid[self.x][self.y] = ''
						self.y+=1
						self.grid[self.x][self.y] = self.direction
					else:
						raise CrashError

				elif(self.direction.lower() == 'e'):
					if(self.x+1==len(self.grid)):
						raise OffGridError
					if(self.grid[self.x+1][self.y] == ''):
						self.grid[self.x][self.y] = ''
						self.x+=1
						self.grid[self.x][self.y] = self.direction
					else:
						raise CrashError

				elif(self.direction.lower() == 's'):
					if(self.y==0):
						raise OffGridError
					if(self.grid[self.x][self.y-1] == ''):
						self.grid[self.x][self.y] = ''
						self.y-=1
						self.grid[self.x][self.y] = self.direction
					else:
						raise CrashError

				else:
					if(self.x==0):
						raise OffGridError
					if(self.grid[self.x-1][self.y] == ''):
						self.grid[self.x][self.y] = ''
						self.x-=1
						self.grid[self.x][self.y] = self.direction
					else:
						raise CrashError

			except OffGridError:
				print('About to fall off grid. Aborting execution.')
				return False

			except CrashError:
				print("About to crash into another rover. Aborting execution.")
				return False
		
		if(not self.instructions):
			return False
		return True

	def final_placement(self):
		return "{} {} {}".format(self.x, self.y, self.direction)

def populate(g):
	directions = ('n','s','e','w')
	moves = ('l', 'r', 'm')
	rovers = []
	coordinates = None
	sequence = None
	cont = '1'
	while(cont!='0'):
		while(True):
			location = input('Please give the X and Y coordinates of the rover, as well as the cardinal direction (single letter) the rover is facing "X Y D": ')
			try:
				coordinates = location.split()
				if (len(coordinates)<3):
					raise ValueTooSmallError
				elif (len(coordinates)>3):
					raise ValueTooLargeError
				elif(int(coordinates[0])<0 or int(coordinates[1])<0):
					raise ValueError
				elif(coordinates[2].lower() not in directions):
					raise AlphaError
				break

			except ValueTooSmallError:
				print('\nYou entered too few arguments, please give both an X and Y coordinate, and direction.')
			except ValueTooLargeError:
				print('\nYou entered too many arguments, please give only an X and Y coordinate, and direction.')
			except ValueError as e:
				print("\nThe coordinates you entered were not non negative integers. Please make sure that your X and Y arguments are both non negative integers.")
			except NumericError:
				print("\nThe direction you entered was not N, S, E, or W. Please make sure it is a direction")

		while(True):
			sequence = input('Please give the sequence of moves you would like to give the rover in a 1 string sequence (eg. "LMMRRM"): ')
			if(check_letters(sequence)):
				break
			print("Invalid sequence, your sequence must contain only the letters 'L', 'R', and 'M'\n")
		rovers.append(Rover(coordinates[0],coordinates[1],coordinates[2], sequence, g))
		cont = input('Rover added. Enter 0 if you have no more rovers, enter anything else to add another: ')
	return rovers
