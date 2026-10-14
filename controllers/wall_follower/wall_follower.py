"""wall_follower controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


def run_robot(robot):
    
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28 # angular_velocity
    
    # create motor instances.
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
        

    #Enable proximity sensors
    prox_sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDevice(sensor_name))
        prox_sensors[ind].enable(timestep)
    
    
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
    
        # Process sensor data here.
    
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        pass
    
    # Enter here exit cleanup code.

if __name__ == "__main__":
    
    
    # create the Robot instance.
    robot = Robot()
    run_robot(robot)