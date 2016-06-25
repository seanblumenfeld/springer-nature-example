import cmd
from src import Canvas


class CanvasPrompt(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = '(Canvas) '    
        self.cmdloop('Starting Canvas 1.0...')

    def _split_args(self, xargs):
        """split args in to a list"""
        return xargs.split(' ')

    def do_C(self, xargs):
        """Create a new canvas with width w and height h.."""
        xargs = self._split_args(xargs)        
        if len(xargs) != 2:
            print('Invalid arguments supplied. Expected args: C w h')
        width = xargs[0]
        height = xargs[1]
        self.canvas = Canvas(width=width, height=height)
        print(self.canvas)

    def do_S(self, xargs):
        """Display the canvas."""
        print(self.canvas)

    def do_quit(self, xargs):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = CanvasPrompt()
