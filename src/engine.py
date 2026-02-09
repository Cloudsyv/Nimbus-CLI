import math

class Point3D:
    def __init__(self, x, y, z, char="@"):
        self.x = x
        self.y = y
        self.z = z
        self.char = char

def project(point, width, height, field_of_view=256):
    factor = field_of_view / (point.z + 0.001)
    
    x_2d = point.x * factor + width // 2
    y_2d = -point.y * factor + height // 2
    
    return int(x_2d), int(y_2d)

def rotate(x, y, z, angle_x, angle_y, angle_z):
    # X-axis
    rad = angle_x
    ny = y * math.cos(rad) - z * math.sin(rad)
    nz = y * math.sin(rad) + z * math.cos(rad)
    y, z = ny, nz

    # Y-axis
    rad = angle_y
    nx = x * math.cos(rad) + z * math.sin(rad)
    nz = -x * math.sin(rad) + z * math.cos(rad)
    x, z = nx, nz

    # Z-axis
    rad = angle_z
    nx = x * math.cos(rad) - y * math.sin(rad)
    ny = x * math.sin(rad) + y * math.cos(rad)
    x, y = nx, ny

    return x, y, z