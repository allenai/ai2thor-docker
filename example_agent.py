from ai2thor_docker.x_server import startx
import ai2thor.controller
from pprint import pprint


if __name__ == '__main__':
    startx()
    controller = ai2thor.controller.Controller(scene='FloorPlan28')
    event = controller.step(action='RotateRight')
    pprint(event.metadata['agent'])

