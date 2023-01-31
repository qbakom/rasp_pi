import pytest
from asynctest import CoroutineMock
import asyncio
from unittest.mock import patch, Mock
import logging

from dynalite_lib.dynet import DynetControl, OpcodeType

LOGGER = logging.getLogger(__name__)

loop = asyncio.get_event_loop()
area = 4
fade = 11.0 # equals to 550 in 0.02 increments = 2*256 + 38
area_def = Mock()
for preset in [1,14]:
    dynet = Mock()
    dyn_control = DynetControl(dynet, loop, area_def)
    await dyn_control.areaPreset(area, preset, fade)
    dynet.write.assert_called_once()
    packet = dynet.write.mock_calls[0][1][0]
