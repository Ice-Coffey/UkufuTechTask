import errors
from errors import ValueTooSmallError, ValueTooLargeError, AlphaError
import numpy
from utils import check_letters

def upper_edge():
	while(True):
		edge = input('Please give the X and Y coordinates of the upper right edge of the area in the format "X Y": ')
		try:
			coordinates = edge.split()
			if (len(coordinates)<2):
				raise ValueTooSmallError
			elif (len(coordinates)>2):
				raise ValueTooLargeError
			elif(not (int(coordinates[0]) and int(coordinates[1]))):
				raise ValueError
			return (int(coordinates[0])+1, int(coordinates[1])+1)

		except ValueTooSmallError:
			print('\nYou entered too few arguments, please give both an X and Y coordinate.')
		except ValueTooLargeError:
			print('\nYou entered too many arguments, please give only an X and Y coordinate.')
		except ValueError:
			print("\nThe coordinates you entered were not integers. Please make sure that your X and Y arguments are both integers.")

def create_grid():
	dimensions = upper_edge()
	return numpy.zeros(dimensions, dtype=str)

if __name__ == '__main__':
	create_grid()

