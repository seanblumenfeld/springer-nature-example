import cmd
from src import Drawer, Canvas, Line, DrawError


class CanvasPrompt(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = '(Canvas) '    
        self.cmdloop('Starting Canvas...')

    def _split_args(self, xargs, expected=1, msg=''):
        """split args in to a list"""
        a = xargs.split(' ')
        if len(a) != expected:
            raise DrawError('Invalid arguments supplied. {}'.format(msg))
        return a

    def do_C(self, xargs):
        """Create a new canvas with width w and height h.."""
        xargs = self._split_args(xargs, expected=2, msg='Expected args: C w h')        
        width = xargs[0]
        height = xargs[1]
        self.canvas = Canvas(width=width, height=height)
        print(self.canvas)

    def do_L(self, xargs):
        """Draw a line on the canvas"""
        try:
            xargs = self._split_args(xargs, expected=4, msg='Expected args: L x1 y1 x2 y2')
            line = Line(*xargs)
            Drawer.draw_line(self.canvas, line)
            print('Line drawn on canvas')
        except DrawError as e:
            print(e)
            print("Did not draw line")
        print(self.canvas)

    def do_R(self, xargs):
        """Draw a rectangle on the canvas"""
        try:
            xargs = self._split_args(xargs, expected=4, msg='Expected args: R x1 y1 x2 y2')
            rectangle = Rectangle(*xargs)
            

            Drawer.draw_line(self.canvas, line)
            print('Line drawn on canvas')
        except DrawError as e:
            print(e)
            print("Did not draw line")
        print(self.canvas)


    def do_Q(self, xargs):
        """Quits the program."""
        print('Quitting.')
        raise SystemExit


if __name__ == '__main__':
    prompt = CanvasPrompt()
