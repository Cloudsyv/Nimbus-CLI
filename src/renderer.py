class Renderer:
    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height
        self.buffer = [[" " for _ in range(width)] for _ in range(height)]

    def clear_buffer(self):
        self.buffer = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def draw_point(self, x, y, char):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = char

    def render(self):
        output = "\033[H" 
        for row in self.buffer:
            output += "".join(row) + "\n"
        print(output, end="", flush=True)