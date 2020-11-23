from ai2thor_docker.x_server import startx
import ai2thor.controller
import os
import time
from pprint import pprint


if __name__ == '__main__':
    startx()
    c = ai2thor.controller.Controller(renderObjectImage=True, renderClassImage=True)
    c.reset('FloorPlan28')
    for i in range(10000):
        c.step('RotateRight')
        total = len(c.last_event.metadata['colorBounds'])
        print("%s length %s"  % (os.getpid(), total))
        time.sleep(2.0)

