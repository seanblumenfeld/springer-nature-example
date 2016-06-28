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
        self._colour = 'x'

    @property
    def colour(self):
        """Cell colour; default is 'x'"""
        return self._colour

    @colour.setter
    def colour(self, new_colour):
        if len(new_colour) != 1:
            raise AttributeError('Colour must be a single character')
        if self._colour == new_colour:
            raise Warning('Colour already set to {}'.format(new_colour))
        self._colour = new_colour

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
            return self.colour
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

    def exists_on_canvas(self, x, y):
        """return whether a given coordinate exists on the canvas"""
        x_exists = x in range(0, self.width)
        y_exists = y in range(0, self.height)
        return all([x_exists, y_exists])


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

    @staticmethod
    def draw_rectangle(canvas, rectangle):
        """We can draw a rectangle by just drawing all 4 sides/lines"""
        Drawer.draw_line(canvas, rectangle.north_line)
        Drawer.draw_line(canvas, rectangle.south_line)
        Drawer.draw_line(canvas, rectangle.east_line)
        Drawer.draw_line(canvas, rectangle.west_line)
        
    @staticmethod
    def draw_bucket_fill(canvas, coords, colour):
        """Bucket fill an area of cells

        Args:
            coords - Set of coordinates; set()
            colour - colour to fill; Char
        """
        result_coords = set()

        for _x,_y in coords:
            new_coords = Drawer.find_surrounding_coords(canvas, _x, _y)
            result_coords = new_coords.union(coords)

            if result_coords:
                Drawer.fill_colour(canvas, result_coords, colour)

        Drawer.draw_bucket_fill(canvas, result_coords, colour)

    @staticmethod
    def find_surrounding_coords(canvas, x, y):
        """Get the coordinates of cells surrounding (x, y) on canvas which have
        the same colour as the (x, y) coordinate
        """
        coords = set()
        possible_coords = [(x+i,y+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]
        
        for _x,_y in possible_coords:
            if canvas.exists_on_canvas(_x, _y) and canvas[x, y].colour == canvas[_x, _y].colour:
                coords.add((_x, _y))
        
        return coords

    @staticmethod
    def fill_colour(canvas, coords, colour):
        """fill a set of coordinates with colour on canvas"""
        for x,y in coords:
            canvas[x, y].colour = colour
            canvas[x, y].state = True
