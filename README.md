<p align="center">
  <img width = "50%" src='/doc/static/thor-logo-main_1.0_thick.png' />
  </p>

--------------------------------------------------------------------------------

# AI2-THOR Docker

AI2-THOR Docker is a mini-framework that simplifies the task of running [AI2-THOR](https://ai2thor.allenai.org) within Docker. The primary feature this adds is configuring and running a X server to be used by Unity3d to render scenes. 

## Getting Started

To use AI2-THOR Docker you must have Docker installed on your host and a Nvidia GPU (required for 3D rendering).


1. Clone or fork this repository.

   ```bash
   git clone https://github.com/allenai/ai2thor-docker
   ```

2. Build the Docker container.

   ```
   cd ai2thor-docker
   ./scripts/build.sh
   ```

3. Run the example agent using Docker.

   ```
   ./scripts/run.sh
   ```

At this point you should see output that resembles the following: 
```

PlayerPrefs - Creating folder: /root/.config/unity3d/Allen Institute for Artificial Intelligence
PlayerPrefs - Creating folder: /root/.config/unity3d/Allen Institute for Artificial Intelligence/AI2-Thor
Logging to /root/.config/unity3d/Allen Institute for Artificial Intelligence/AI2-Thor/Player.log
Initialize return: {'cameraNearPlane': 0.1, 'cameraFarPlane': 20.0}
{'cameraHorizon': 0.0,
 'inHighFrictionArea': False,
 'isStanding': True,
 'name': 'agent',
 'position': {'x': -1.5, 'y': 0.9009982347488403, 'z': -1.5},
 'rotation': {'x': 0.0, 'y': 270.0, 'z': 0.0}}
```

## Docker

The Docker container is built with the highest version of CUDA that the host version's Nvidia driver will support.  In order to train/execute a model the code must either be explicitly copied into the container by adding an entry into the Dockerfile or by sharing a volume with your code to the container (see ./scripts/run.sh). 

## Example

The following is code for the example agent that executes a single command ```RotateRight```.  

```python
from pprint import pprint
import ai2thor.controller


if __name__ == '__main__':
    controller = ai2thor.controller.Controller(scene='FloorPlan28')
    event = controller.step(action='RotateRight')
    pprint(event.metadata['agent'])

```

