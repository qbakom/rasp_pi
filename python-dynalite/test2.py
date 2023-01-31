#!/usr/bin/env python3
import json
import logging
import asyncio
from dynalite_lib import Dynalite

logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s")
LOG = logging.getLogger(__name__)

OPTIONS_FILE = 'test/options.json'

loop = asyncio.get_event_loop()
dynalite = None


def handleEvent(event=None, dynalite=None):
    LOG.debug(event.toJson())


def handleConnect(event=None, dynalite=None):
    LOG.info("Connected to Dynalite")
    # dynalite.devices['area'][8].preset[10].turnOn()
    dynalite.state()


if __name__ == '__main__':
    with open(OPTIONS_FILE, 'r') as f:
        cfg = json.load(f)

    dynalite = Dynalite(config=cfg, loop=loop)

    bcstr = dynalite.addListener(listenerFunction=handleEvent)
    bcstr.monitorEvent('*')

    onConnect = dynalite.addListener(listenerFunction=handleConnect)
    onConnect.monitorEvent('CONNECTED')

    dynalite.start()
    loop.run_forever()

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
