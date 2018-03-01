# PyUnityVibes
![Status](https://img.shields.io/badge/Status-In%20Development-red.svg)
![Python2](https://img.shields.io/badge/Python2-v2.6+-green.svg)
![Python3](https://img.shields.io/badge/Python3-v3.4+-green.svg)

PyUnityVibes aims at providing a simple and powerful GUI interface for [Unity](https://unity3d.com) using Python.  
It can display 2D and 3D figures and offers a wide range of shapes and meshes to make simple simulations with a great visual.   Several environments are available.



## Installation


### Python package
You can install the package with pip:
```shell
pip install PyUnityVibes
```
Other downloads can be found on the [Python Package Index page for PyUnityVibes](https://pypi.org/project/PyUnityVibes).  


### UnityVibes viewer
It is necessary to download the UnityVibes viewer, see the dedicated [GitHub page](https://github.com/RemiRigal/Unity-Vibes). Binaries are available for most platforms (Linux, Windows, OS X).  
The viewer must be running to execute python scripts.  



## Getting Started
Several examples can be found in the `examples` directory, here is a sample of a simple PyUnityVibes script:
```python
from PyUnityVibes.UnityFigure import UnityFigure
import time

# Initialization of the figure
# Parameters:
#   figType: the dimension of the figure (see UnityFigure.FIGURE_*)
#   scene: the scene to be loaded (see UnityFigure.SCENE_*)
figure = UnityFigure(UnityFigure.FIGURE_3D, UnityFigure.SCENE_EMPTY)
time.sleep(1)

# Creation of an object
# Parameters:
#   meshType: the mesh of the object (see UnityFigure.OBJECT_*)
#   x: the x coordinate
#   y: the y coordinate
#   z: the z coordinate
#   [rotX: the x euler angle]
#   [rotY: the y euler angle]
#   [rotZ: the z euler angle]
#   [dimX: the x scale]
#   [dimY: the y scale]
#   [dimZ: the z scale]
#   [color: the color of the mesh (see UnityFigure.COLOR_*)]
boat = figure.create(UnityFigure.OBJECT_3D_BOAT, 0, 0, 0)
time.sleep(1)

# Update of an object's position
# Parameters:
#   x: the new x coordinate
#   y: the new y coordinate
#   z: the new z coordinate
boat.updatePosition(1, 1, 1)
time.sleep(1)

# Update of an object's rotation
# Parameters:
#   x: the new x euler angle
#   y: the new y euler angle
#   z: the new z euler angle
boat.updateRotation(45, 90, 0)
time.sleep(1)

# Deletion of an object
boat.delete()
```