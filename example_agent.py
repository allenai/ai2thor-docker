from ai2thor_docker.x_server import startx
import time
import threading
import os
from pprint import pprint
import ai2thor.controller

def setup_env():
    if 'DISPLAY' not in os.environ:
        xthread = threading.Thread(target=startx)
        xthread.daemon = True
        xthread.start()
        # wait for server to start
        time.sleep(4)



if __name__ == '__main__':
    setup_env()
    controller = ai2thor.controller.Controller(scene='FloorPlan28')
    event = controller.step(action='RotateRight')
    pprint(event.metadata['agent'])

