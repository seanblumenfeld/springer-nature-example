from src import Drawer, Canvas, Cell, Line, Rectangle, DrawError
import unittest


class TestDrawer(unittest.TestCase):

    # Draw Lines
    def test_fill_horizontal_line_canvas_4x2(self):
        canvas = Canvas(width=4, height=2)
        line = Line(x1=1, y1=1, x2=3, y2=1)
        Drawer.draw_line(canvas, line)
        self.assertEquals(str(canvas), ' ----\n|xxx |\n|    |\n ----')

    def test_fill_vertical_line_canvas_4x2(self):
        canvas = Canvas(width=4, height=2)
        line = Line(x1=1, y1=1, x2=1, y2=2)
        Drawer.draw_line(canvas, line)
        self.assertEquals(str(canvas), ' ----\n|x   |\n|x   |\n ----')

    def test_cannot_draw_line_outsided_of_canvas_4x4(self):
        canvas = Canvas(width=4, height=2)
        line = Line(x1=1, y1=1, x2=5, y2=1)
        self.assertRaises(DrawError, Drawer.draw_line, canvas, line)
        # Canvas should still be empty
        self.assertEquals(str(canvas), ' ----\n|    |\n|    |\n ----')

    def test_fill_line_on_canvas_20x4(self):
        canvas = Canvas(width=20, height=4)
        canvas.draw_line(x1=1, y1=2, x2=6, y2=2)
        self.assertEquals(str(canvas), ' --\n|xx|\n|xx|\n --')

    # Draw Rectangle


class TestCanvas(unittest.TestCase):

    def test_can_create_canvas(self):
        canvas = Canvas(width=1, height=1)
        self.assertEquals(canvas.width, 1)
        self.assertEquals(canvas.height, 1)
    
    def test_empty_canvas_str_for_0x0(self):
        canvas = Canvas(width=0, height=0)
        self.assertEquals(str(canvas), '')

    def test_empty_canvas_str_for_0x1(self):
        canvas = Canvas(width=0, height=1)
        self.assertEquals(str(canvas), '')

    def test_empty_canvas_str_for_1x0(self):
        canvas = Canvas(width=1, height=0)
        self.assertEquals(str(canvas), '')

    def test_empty_canvas_str_for_1x1(self):
        canvas = Canvas(width=1, height=1)
        self.assertEquals(str(canvas), ' -\n| |\n -')

    def test_empty_canvas_str_for_2x2(self):
        canvas = Canvas(width=2, height=2)
        self.assertEquals(str(canvas), ' --\n|  |\n|  |\n --')

    def test_empty_canvas_str_for_3x1(self):
        #import pdb; pdb.set_trace()
        canvas = Canvas(width=3, height=1)
        self.assertEquals(str(canvas), ' ---\n|   |\n ---')

    def test_can_get_cell_state(self):
        canvas = Canvas(width=4, height=4)
        self.assertFalse(canvas[2, 2].state)

    def test_full_canvas_str_for_1x1(self):
        canvas = Canvas(width=1, height=1)
        canvas[0, 0].state = True
        self.assertEquals(str(canvas), ' -\n|x|\n -')

    def test_full_canvas_str_for_2x2(self):
        canvas = Canvas(width=2, height=2)
        canvas[0, 0].state = True
        canvas[0, 1].state = True
        canvas[1, 0].state = True
        canvas[1, 1].state = True
        self.assertEquals(str(canvas), ' --\n|xx|\n|xx|\n --')


class TestCell(unittest.TestCase):

    def test_cell_starts_in_blank_state(self):
        cell = Cell()
        self.assertFalse(cell.state)
        self.assertEquals(str(cell), ' ')

    def test_set_cell_state_filled(self):
        cell = Cell()
        cell.state = True
        self.assertTrue(cell.state)
        self.assertEquals(str(cell), 'x')

    def test_cell_state_filled_unfilled(self):
        cell = Cell()
        cell.state = True
        self.assertTrue(cell)
        self.assertEquals(str(cell), 'x')
        cell.state = False
        self.assertFalse(cell.state)
        self.assertEquals(str(cell), ' ')


class TestLine(unittest.TestCase):

    def test_line_length_set_correctly(self):
        line = Line(x1=0, y1=0, x2=0, y2=2)
        self.assertEquals(line.length, 3)

    def test_is_vertical(self):
        line = Line(x1=0, y1=0, x2=0, y2=2)
        self.assertEquals(line.orientation, 'vertical')

    def test_is_horizontal(self):
        line = Line(x1=0, y1=0, x2=2, y2=0)
        self.assertEquals(line.orientation, 'horizontal')

    def test_is_not_valid_line(self):
        line = Line(x1=0, y1=0, x2=1, y2=2)
        def local_orientation():
            line.orientation
        self.assertRaises(DrawError, local_orientation)
        
    def test_line_length(self):
        line = Line(x1=1, y1=3, x2=3, y2=3)
        self.assertEquals(line.length, 3)


class TestRectangle(unittest.TestCase):
    """
    TestCase for rectangle:
                     ----------
                    |xxx       |
                    |x x       |
                    |x x       |
                    |xxx       |
                     ----------
    """

    @classmethod
    def setUpClass(cls):
        cls.rectangle = Rectangle(x1=1, y1=1, x2=3, y2=4)
        
    def test_north_line(self):
        self.assertEquals(self.rectangle.north_line.x1, 1)
        self.assertEquals(self.rectangle.north_line.y1, 1)
        self.assertEquals(self.rectangle.north_line.x2, 3)
        self.assertEquals(self.rectangle.north_line.y2, 1)

    def test_south_line(self):
        self.assertEquals(self.rectangle.south_line.x1, 1)
        self.assertEquals(self.rectangle.south_line.y1, 4)
        self.assertEquals(self.rectangle.south_line.x2, 3)
        self.assertEquals(self.rectangle.south_line.y2, 4)

    def test_east_line(self):
        self.assertEquals(self.rectangle.east_line.x1, 3)
        self.assertEquals(self.rectangle.east_line.y1, 1)
        self.assertEquals(self.rectangle.east_line.x2, 3)
        self.assertEquals(self.rectangle.east_line.y2, 4)

    def test_west_line(self):
        self.assertEquals(self.rectangle.west_line.x1, 1)
        self.assertEquals(self.rectangle.west_line.y1, 1)
        self.assertEquals(self.rectangle.west_line.x2, 1)
        self.assertEquals(self.rectangle.west_line.y2, 4)
