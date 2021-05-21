import unittest
import pygame
from Tamagoc import *

class Test_test_main(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_test_main, self).__init__(*args, **kwargs)
        Tamainit()

    def test_ImagesPresents(self):
        self.assertIsNotNone(load_image('resources/fon_menu.jpg', None, False))
        self.assertIsNotNone(load_image('resources/bubble.png', None, False))
        self.assertIsNone(load_image('resources/bubble232345.png', None, False))
    
    
if __name__ == '__main__':
    unittest.main()
