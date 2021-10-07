import ai2thor.controller
import ai2thor.platform
from pprint import pprint


if __name__ == '__main__':
    controller = ai2thor.controller.Controller(platform=ai2thor.platform.CloudRendering, scene='FloorPlan28')
    event = controller.step(action='RotateRight')
    pprint(event.metadata['agent'])
