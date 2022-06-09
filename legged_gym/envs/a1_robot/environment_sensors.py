"""Simple sensors related to the environment."""
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0, parentdir)

import numpy as np
import typing

from legged_gym.envs.a1_robot import sensor

_ARRAY = typing.Iterable[float] # pylint:disable=invalid-name
_FLOAT_OR_ARRAY = typing.Union[float, _ARRAY] # pylint:disable=invalid-name
_DATATYPE_LIST = typing.Iterable[typing.Any] # pylint:disable=invalid-name


class LastActionSensor(sensor.BoxSpaceSensor):
  """A sensor that reports the last action taken."""

  def __init__(self,
               num_actions: int,
               scale=None,
               default_pose=None,
               lower_bound: _FLOAT_OR_ARRAY = -1.0,
               upper_bound: _FLOAT_OR_ARRAY = 1.0,
               name: typing.Text = "LastAction",
               dtype: typing.Type[typing.Any] = np.float64) -> None:
    """Constructs LastActionSensor.

    Args:
      num_actions: the number of actions to read
      lower_bound: the lower bound of the actions
      upper_bound: the upper bound of the actions
      name: the name of the sensor
      dtype: data type of sensor value
    """
    self._num_actions = num_actions
    self._env = None

    self.default_pose = default_pose
    self.scale = scale

    super(LastActionSensor, self).__init__(name=name,
                                           shape=(self._num_actions,),
                                           lower_bound=lower_bound,
                                           upper_bound=upper_bound,
                                           dtype=dtype)

  def on_reset(self, env):
    """From the callback, the sensor remembers the environment.

    Args:
      env: the environment who invokes this callback function.
    """
    self._env = env

  def _get_observation(self) -> _ARRAY:
    """Returns the last action of the environment."""
    return (self._env.last_action - self.default_pose) / self.scale

