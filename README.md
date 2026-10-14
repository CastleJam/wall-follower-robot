# Wall Follower Robot

A Webots robotics project exploring autonomous wall following with a Python controller and distance sensors.

The goal is to make a differential-drive robot follow a wall, maintain a target separation, and adjust its direction when approaching obstacles or corners.

## Project Status

This project is in its initial setup stage. Robot configuration, sensor readings, and wall-following behavior will be developed and committed incrementally. Reliable wall following has not yet been validated.

## Planned Behavior

- Read distance sensors to detect nearby walls and obstacles.
- Adjust the left and right wheel speeds to follow a wall.
- Correct the robot's path when it gets too close to or too far from the wall.
- Handle corners and obstacles during navigation.

## Requirements

- Webots with Python controller support.
- Python 3 configured as the Python interpreter in Webots.
- Git or GitHub Desktop to clone the repository and track changes.

The controller uses the `controller` module provided by Webots. A separate pip installation of this module is not required.

## Project Organization

The repository root should also be the Webots project directory.

| Directory | Purpose |
| --- | --- |
| `controllers/` | Python robot controllers |
| `worlds/` | Webots simulation worlds (`.wbt` files) |
| `protos/` | Custom reusable robot and environment models, if needed |
| `libraries/` | Project libraries, if needed |
| `plugins/` | Webots plugins, if needed |

Optional directories may be empty or absent until they are used. A `.gitkeep` file can be used to retain an empty directory in Git.

## Getting Started

1. Clone this repository using GitHub Desktop or Git.
2. Open Webots and select **File → Open World**.
3. Open the project's `.wbt` file from `worlds/` once it has been added.
4. Select the robot in the Scene Tree and check that its `controller` field matches the controller directory in `controllers/`.
5. Run the simulation and inspect the Webots console for sensor readings or errors.

If no world or controller has been committed yet, create them in the corresponding directories before running the simulation.

## Configuration and Testing

When implementing the controller, check that device names match the robot model. Inspect the sensors' orientation and range, then use their readings to tune the wall-following thresholds and wheel speeds.

Start with a low forward speed and test straight walls before introducing corners. Record the sensor settings and control parameters alongside each working version so that the behavior can be reproduced.

## Development Roadmap

- [ ] Set up the simulation world and robot.
- [ ] Configure motors and distance sensors.
- [ ] Read and inspect sensor values.
- [ ] Implement basic wall-following control.
- [ ] Tune the target wall separation and steering response.
- [ ] Test corners and obstacles.
- [ ] Add a GIF or video demonstrating the robot's behavior.

## Tutorial Reference

This learning project follows the tutorial linked below:

[Watch the tutorial on YouTube](https://www.youtube.com/watch?v=tHENC-HEIW8)

Implementation details and parameter tuning will be documented as the project progresses. Any reused code or assets should retain their original attribution and license notices.
