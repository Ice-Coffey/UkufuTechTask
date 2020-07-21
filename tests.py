import unittest
import utils
import area
import rover
from unittest.mock import patch
import random
import numpy

#selects a random choice between two options
#used in this program to randomize incorrect inputs
def fifty_fifty(one, two):
    return random.choice((one, two))

class TestStringMethods(unittest.TestCase):

    #tests to make sure we only accept case insensitive letters from the set "LRM"
    def test_utils(self):

        self.assertTrue(utils.check_letters('lmRRlMLRRLMrmlRmlMR'))
        self.assertTrue(utils.check_letters(''))
        self.assertTrue(utils.check_letters('LMRrml'))
        self.assertFalse(utils.check_letters('0'))
        self.assertFalse(utils.check_letters('LMRrml0'))
        self.assertFalse(utils.check_letters('lmRRlMLRRLMrmlRmlMR '))


    #tests to determine that upper edge returns dimensions of (x+1, y+1)
    def test_area(self):

        original_input = __builtins__.input
        __builtins__.input = lambda _: '6 6'
        self.assertEqual(area.upper_edge(), (7,7))

        __builtins__.input = lambda _: '0 0'
        self.assertEqual(area.upper_edge(), (1,1))

        __builtins__.input = lambda _: '1 1'
        self.assertEqual(area.upper_edge(), (2,2))

        #uses fifty_fifty to give an impossible input of "-1 -1" which is off the grid
        __builtins__.input = lambda _: fifty_fifty('-1 -1','0 0')
        self.assertEqual(area.create_grid(), numpy.zeros((1,1), dtype=str))

        #uses fifty_fifty to give an impossible input of "-1 -1 -1" which is too many inputs
        __builtins__.input = lambda _: fifty_fifty('-1 -1 -1','0 0')
        self.assertEqual(area.create_grid(), numpy.zeros((1,1), dtype=str))

        #uses fifty_fifty to give an impossible input of "-1" which is too few inputs
        __builtins__.input = lambda _: fifty_fifty('-1','0 0')
        self.assertEqual(area.create_grid(), numpy.zeros((1,1), dtype=str))

        __builtins__.input = lambda _: '7 6'
        a = area.create_grid()
        self.assertIsInstance(a, numpy.ndarray)
        self.assertEqual(len(a), 8)
        self.assertEqual(len(a[0]), 7)
        
        __builtins__.input = original_input

    
    #comprehensive step by step of a single rover run
    def test_rover_run(self):

        original_input = __builtins__.input
        __builtins__.input = lambda _: '6 6'

        #creates 7x7 grid
        grid = area.create_grid()

        #checks to make sure the rovers internal elements are all correct
        r = rover.Rover('1', '5', 'S', 'LLLLRLMMMMRRMRM', grid)
        self.assertIsInstance(r, rover.Rover)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.direction, 'S')
        self.assertEqual(r.instructions, 'LLLLRLMMMMRRMRM')

        #makes a single move and makes sure there are are still more instructions it can follow
        self.assertTrue(r.make_move())

        #checks that it only changed the direction it's facing, and has fewer instructions left to complete
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.direction, 'E')
        self.assertEqual(r.instructions, 'LLLRLMMMMRRMRM')

        #makes 5 moves
        for x in range(5):
            self.assertTrue(r.make_move())

        #checks for correct placement, direction, and instructions left
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.direction, 'S')
        self.assertEqual(r.instructions, 'MMMMRRMRM')

        #makes 6 moves
        for x in range(6):
            self.assertTrue(r.make_move())

        #checks for correct placement, direction, and instructions left
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.direction, 'N')
        self.assertEqual(r.instructions, 'MRM')

        #makes 2 moves
        for x in range(2):
            self.assertTrue(r.make_move())

        #makes one move and checks to make sure it is finished moving
        #then checks for correct placement, direction, and instructions left
        self.assertFalse(r.make_move())
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.direction, 'E')
        self.assertEqual(r.instructions, '')

        __builtins__.input = original_input


    #tests the program with 9998 rovers moving in series 
    #then checks for correct placement, direction
    def test_stress_rover(self):
        original_input = __builtins__.input
        __builtins__.input = lambda _: '10000 10000'

        grid = area.create_grid()
        rovers = [rover.Rover(i, i, 'n', 'MRrMlmllmmrrM', grid) for i in range(1,9999)]
        for r in rovers:
            for i in range(4):
                self.assertTrue(r.make_move())
            self.assertEqual(r.x, r.y)
            self.assertTrue(r.direction, 'S')
            for i in range(8):
                self.assertTrue(r.make_move())
            self.assertFalse(r.make_move())

            self.assertEqual(r.x, r.y)
            self.assertTrue(r.direction, 'W')


        __builtins__.input = original_input


    #test to make sure rovers don't crash into each other or fall off the grid
    def test_crash_and_fall(self):

        original_input = __builtins__.input
        __builtins__.input = lambda _: '0 1'
        grid = area.create_grid()
        __builtins__.input = original_input

        #fills a 1x2 grid with north facing rovers who have instructions to move forward
        r1 = rover.Rover(0, 0, 'N', 'M', grid)
        r2 = rover.Rover(0, 1, 'n', 'M', grid)
        self.assertEqual(grid[0][0],'N')
        self.assertEqual(grid[0][1],'N')

        #attempts to push one rover over the edge, and push one rover into the other
        self.assertFalse(r1.make_move())
        self.assertFalse(r2.make_move())
        self.assertEqual(grid[0][0],'N')
        self.assertEqual(grid[0][1],'N')

        #checks to make sure they haven't moved
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 1)

        #checks correct direction
        self.assertEqual(r2.direction, 'N')
        self.assertEqual(r1.direction, 'N')


if __name__ == '__main__':
    unittest.main()