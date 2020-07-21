from area import create_grid
from rover import Rover, populate

def main():
	grid = create_grid()
	rovers = populate(grid)
	for rover in rovers:
		while(rover.make_move()):
			pass
		print(rover.final_placement())

if __name__ == '__main__':
	main()