"""The configuration parameters for our robots."""

import enum

class MotorControlMode(enum.Enum):
  """The supported motor control modes."""
  POSITION = 1

  # Apply motor torques directly.
  TORQUE = 2

  # Apply a tuple (q, qdot, kp, kd, tau) for each motor. Here q, qdot are motor
  # position and velocities. kp and kd are PD gains. tau is the additional
  # motor torque. This is the most flexible control mode.
  HYBRID = 3

  # PWM mode is only availalbe for Minitaur
  PWM = 4


# Each hybrid action is a tuple (position, position_gain, velocity,
# velocity_gain, torque)
HYBRID_ACTION_DIMENSION = 5


class HybridActionIndex(enum.Enum):
  # The index of each component within the hybrid action tuple.
  POSITION = 0
  POSITION_GAIN = 1
  VELOCITY = 2
  VELOCITY_GAIN = 3
  TORQUE = 4
