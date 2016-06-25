
class Canvas():

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    #def __repr__(self):
    #    return '------------'

    def __str__(self):
        lines = []

        # display empty canvas if height or widtch is 0
        if not any([self.width == 0, self.height == 0]):
            boarder_line = ' {}'.format('-' * self.width)
            # Top boarder
            lines.append(boarder_line)
            # The canvas
            for _ in range(self.height):
                lines.append('|{}|'.format(' ' * self.width))
            # Bottom boarder
            lines.append(boarder_line)
        
        return '\n'.join(lines)
