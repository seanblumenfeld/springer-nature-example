import cmd
from src import Drawer, Canvas, Line, Rectangle, DrawError


class CanvasPrompt(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = '(enter command) '    
        self.cmdloop('Starting Canvas...')

    def _split_args(self, xargs, expected=1, msg=''):
        """split args in to a list"""
        a = xargs.split(' ')
        if len(a) != expected:
            raise DrawError('Invalid arguments supplied. {}'.format(msg))
        return a

    def do_C(self, xargs):
        """Create a canvas with width w and height h.

        xargs: 'w h'
            w - width
            h - height

        Should create a new canvas of width w and height h.
        """
        xargs = self._split_args(xargs, expected=2, msg='Expected args: C w h')        
        width = xargs[0]
        height = xargs[1]
        self.canvas = Canvas(width=width, height=height)

    def do_L(self, xargs):
        """Draw a line on the canvas

        xargs: 'x1 y1 x2 y2'
            x1 - position on x-axis of start coordinate
            y1 - position on y-axis of start coordinate
            x2 - position on x-axis of end coordinate
            y2 - position on y-axis of end coordinate

        Should create a new line from (x1,y1) to (x2,y2). Currently only horizontal or
        vertical lines are supported. Horizontal and vertical lines will be drawn using the 'x'
        character.
        """
        try:
            xargs = self._split_args(xargs, expected=4, msg='Expected args: L x1 y1 x2 y2')
            line = Line(*xargs)
            Drawer.draw_line(self.canvas, line)
            print('Line drawn on canvas')
        except DrawError as e:
            print(e)
            print("Line not drawn on canvas")

    def do_R(self, xargs):
        """Draw a rectangle on the canvas

        xargs: 'x1 y1 x2 y2'
            x1 - position on x-axis of upper left corner
            y1 - position on y-axis of upper left corner
            x2 - position on x-axis of bottom right corner
            y2 - position on y-axis of bottom right corner

        Should create a new rectangle, whose upper left corner is (x1,y1) and lower right
        corner is (x2,y2). Horizontal and vertical lines will be drawn using the 'x' character.
        """
        try:
            xargs = self._split_args(xargs, expected=4, msg='Expected args: R x1 y1 x2 y2')
            rectangle = Rectangle(*xargs)
            Drawer.draw_rectangle(self.canvas, rectangle)
            print('Rectangle drawn on canvas')
        except DrawError as e:
            print(e)
            print("Rectangle not drawn on canvas")

    def do_B(self, xargs):
        """Bucket Fill command. 
        
        xargs: 'x y c'
            x - position on x-axis
            y - position on y-axis
            c - colour of fill, single character string

        Fill the entire area connected to (x,y) with colour 'c'.
        """
        try:
            xargs = self._split_args(xargs, expected=4, msg='Expected args: B x y c')
            Drawer.draw_bucket_fill(self.canvas, *xargs)
            print('Bucket Fill drawn on canvas')
        except DrawError as e:
            print(e)
            print("Bucket Fill drawn not drawn")

    def postcmd(self, stop, line):
        """Print the canvas after every command from user"""
        print(self.canvas)
        return cmd.Cmd.postcmd(self, stop, line)

    def do_Q(self, xargs):
        """Quits the program."""
        print('Quitting.')
        raise SystemExit


if __name__ == '__main__':
    prompt = CanvasPrompt()
