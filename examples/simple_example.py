from PyUnityVibes.UnityFigure import UnityFigure
import time


if __name__ == "__main__":
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
