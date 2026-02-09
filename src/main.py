import time
import random
from src.engine import Point3D, project, rotate
from src.renderer import Renderer

def run():
    renderer = Renderer(width=100, height=40)
    
    while True:
        renderer.clear_buffer()
        
        renderer.render()
        time.sleep(0.03)
        
    

if __name__ == "__main__":
    run()