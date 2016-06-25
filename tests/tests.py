from src import Canvas
import unittest

class TestCanvas(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_can_create_canvas(self):
        c = Canvas(width=1, height=1)
        self.assertEquals(c.width, 1)
        self.assertEquals(c.height, 1)

    def test_canvas_str_for_1x1(self):
        c = Canvas(width=1, height=1)
        self.assertEquals(str(c), ' -\n| |\n -')

    def test_canvas_str_for_2x2(self):
        c = Canvas(width=2, height=2)
        self.assertEquals(str(c), ' --\n|  |\n|  |\n --')
    
    def test_canvas_str_for_0x0(self):
        c = Canvas(width=0, height=0)
        self.assertEquals(str(c), '')

    def test_canvas_str_for_0x1(self):
        c = Canvas(width=0, height=1)
        self.assertEquals(str(c), '')

    def test_canvas_str_for_1x0(self):
        c = Canvas(width=1, height=0)
        self.assertEquals(str(c), '')
