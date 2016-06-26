class DrawError(Exception): 
    pass


class Shape:

    def __init__(self, x1, y1, x2, y2):
        # Input x's and y's are human friendly; [1, 2, 3...]
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def __repr__(self):
        return '<Shape: x1-{}, y1-{}, x2-{}, y2-{}>'.format(self.x1, self.y1, self.x2, self.y2)

    def __str__(self):
        return 'x1-{}, y1-{}, x2-{}, y2-{}'.format(self.x1, self.y1, self.x2, self.y2)

    @property
    def start_coordinate(self):
        """Coordinates are array indexes; [0, 1, 2...].

        Eg: 
            x1, y1, x2, y2 = 1, 1, 5, 5
            ==
            start, end = (0, 0), (5, 5) 
        """
        return (self.x1-1, self.y1-1)
    
    @property
    def end_coordinate(self):
        """Coordinates are array indexes; [0, 1, 2...]. 
        Human friendly x's and y's are considered inclusive.

        Eg: 
            x1, y1, x2, y2 = 1, 1, 5, 5
            ==
            start, end = (0, 0), (5, 5) 
        """
        return (self.x2, self.y2)


class Rectangle(Shape):
    
    @property
    def north_line(self):
        return Line(x1=self.x1, y1=self.y1, x2=self.x2, y2=self.y1)
    
    @property
    def south_line(self):
        return Line(x1=self.x1, y1=self.y2, x2=self.x2, y2=self.y2)
    
    @property
    def east_line(self):
        return Line(x1=self.x2, y1=self.y1, x2=self.x2, y2=self.y2)
    
    @property
    def west_line(self):
        return Line(x1=self.x1, y1=self.y1, x2=self.x1, y2=self.y2)


class Line(Shape):

    @property
    def length(self):
        return max(abs(self.x1 - self.x2)+1, abs(self.y1 - self.y2)+1)

    @property
    def orientation(self):
        if self.x1 == self.x2:
            return 'vertical'
        if self.y1 == self.y2:
            return 'horizontal'
        else:
            raise DrawError('Line is not straight')


class Cell:
    
    def __init__(self):
        self._state = False

    @property
    def state(self):
        """Cell state is either filled or empty"""
        return self._state

    @state.setter
    def state(self, new_state):
        """flip the state of the cell"""
        self._state = new_state

    def __str__(self):
        if self.state:
            return 'x'
        return ' '


class Canvas:

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self._boarder_line = ' {}'.format('-' * self.width)

        self._canvas = [[Cell() for y in range(self.height)]
                                for x in range(self.width)]

    def __getitem__(self, coordinate):
        """return the cell at coordinate [x, y]."""
        x, y = coordinate
        return self._canvas[x][y]

    def __setitem__(self, coordinate, state):
        """set the state of cell at coordinate [x, y]."""
        x, y = coordinate
        self._canvas[x][y].state = state

    def __str__(self):
        """Show a nice picture of the current state of canvas"""

        # display empty canvas if height or widtch is 0
        if any([self.width == 0, self.height == 0]):
            return ''

        rows = []
        # Top boarder
        rows.append(self._boarder_line)
        
        #The canvas
        for y in range(self.height):
            row = '|'
            for x in range(self.width):
                row += str(self._canvas[x][y])
            row += '|'
            rows.append(row)
        
        # Bottom boarder
        rows.append(self._boarder_line)
        
        return '\n'.join(rows)


class Drawer:
    
    @staticmethod
    def draw_line(canvas, line):
        #first check if line fits on canvas
        if any([line.x2 > canvas.width, line.y2 > canvas.height]):
            raise DrawError('Line is larger than canvas')

        if line.orientation == 'horizontal':
            for p in range(line.start_coordinate[0], line.end_coordinate[0]):
                canvas[p, line.start_coordinate[1]].state = True
        else:
            for p in range(line.start_coordinate[1], line.end_coordinate[1]):
                canvas[line.start_coordinate[0], p].state = True
