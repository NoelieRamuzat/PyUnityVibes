from PyUnityVibes.UnityFigure import UnityFigure
import time, math
import numpy as np

# Function of the derivative of X
def xdot(x, u):
    return np.array([[x[3, 0]*math.cos(x[2, 0])], [x[3, 0]*math.sin(x[2, 0])], [u[0, 0]], [u[1, 0]]])

# Function witch return the command to follow to assure the trajectory
def control(x, w, dw):
    A = np.array([[-x[3, 0]*math.sin(x[2, 0]), math.cos(x[2, 0])], [x[3, 0]*math.cos(x[2, 0]), math.sin(x[2, 0])]])
    y = np.array([[x[0, 0]], [x[1, 0]]])
    dy = np.array([[x[3, 0]*math.cos(x[2, 0])], [x[3, 0]*math.sin(x[2, 0])]])
    v = w - y + 2*(dw - dy)
    return np.linalg.inv(A) @ v

# Function for the command with supervisor - alpha the time step between the follower and followed
def followSupervisor(alpha):
    w = np.array([[Lx * math.sin(0.1 * (t-alpha))], [Ly * math.cos(0.1 * (t-alpha))]])
    dw = np.array([[Lx * 0.1 * math.cos(0.1 * (t-alpha))], [-Ly * 0.1 * math.sin(0.1 * (t-alpha))]])
    return w, dw


if __name__ == "__main__":
    
    # Initialization of the figure
    # Parameters:
    #   figType: the dimension of the figure (see UnityFigure.FIGURE_*)
    #   scene: the scene to be loaded (see UnityFigure.SCENE_*)
    figure = UnityFigure(UnityFigure.FIGURE_3D, UnityFigure.SCENE_EMPTY)
    time.sleep(1)

    # Initialization variables
    dt = 0.16
    xa = np.array([[10], [0], [1], [1]])
    ua = np.array([[0], [0]])
    xb = np.array([[0], [0], [1], [2]])
    dxa, dxb = 0, 0
    dza, dzb = 0, 0
    s = (4, int(20/dt) + 1)
    l = 6
    Lx = 15
    Ly = 7

    # Creation of a submarine and a black box which represents the sensor
    anim = figure.createAnimation(dt)
    time.sleep(1)
    sub = figure.create(UnityFigure.OBJECT_3D_SUBMARINE, 0, -0.4, 0, dimX=5, dimY=5, dimZ=5)
    anim.addObject(sub)
    sensor = figure.create(UnityFigure.OBJECT_3D_CUBE, 0, -0.5, 0, dimX=0.2, dimY=0.2, dimZ=1, color=UnityFigure.COLOR_BLACK)
    anim.addObject(sensor)
    # Track the submarine with the camera
    # sub1.track()
    time.sleep(1)

    # Loop with the follow function
    for t in np.arange(0, 70, dt):
        # Ellipse to follow
        wa = np.array([[Lx * math.sin(0.1 * t)], [Ly * math.cos(0.1 * t)]])
        dwa = np.array([[Lx * 0.1 * math.cos(0.1 * t)], [-Ly * 0.1 * math.sin(0.1 * t)]])
        ua = control(xa, wa, dwa)

        # Sensor follow the submarine
        wb, dwb = followSupervisor(4)
        ub = control(xb, wb, dwb)

        # Evolution Equations
        xa = xa + dt * xdot(xa, ua)
        xb = xb + dt * xdot(xb, ub)

        # Append the new frame with calculated position to the submarine and sensor
        # Calculation of the rotation angle to maintain the direction of the objects
        angle1 = math.atan2(dxa - xa[0][0], dza - xa[1][0]) - math.pi
        angle2 = math.atan2(dxb - xb[0][0], dzb - xb[1][0]) - math.pi
        anim.appendFrame(sub, x=xa[0][0], y=-0.4, z=xa[1][0], rx=0, ry=math.degrees(angle1), rz=0)
        anim.appendFrame(sensor, x=xb[0][0], y=-0.4, z=xb[1][0], rx=0, ry=math.degrees(angle2), rz=0)
        # Updating the last position for the direction angle calculation
        dxa, dxb = xa[0][0], xb[0][0]
        dza, dzb = xa[1][0], xb[1][0]

    time.sleep(1)
    # Start the animation
    figure.animate(anim)
