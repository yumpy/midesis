from __future__ import print_function

import sys
import time
import random
import mido
import logging
import pygame
import json

from mido import Message
from pygame.locals import *


from kinesis.producer import KinesisProducer

logging.basicConfig(level=logging.DEBUG, format='%(created)f %(levelname)s %(process)d %(name)s:%(lineno)d %(message)s')
logging.getLogger('botocore').level = logging.INFO
logging.getLogger('botocore.vendored.requests.packages.urllib3').level = logging.WARN
producer = KinesisProducer('borgstrom-test')

random.seed(42)

for idx in range(5):

    button = random.randrange(9)

    gh_event = {
        "type": JOYBUTTONDOWN,
        "button": button
    }

    msg = json.dumps(gh_event)
    print("v:", msg)
    

    producer.put(msg)

    sleep(5)

    gh_event = {
        "type": JOYBUTTONUP,
        "button": button
    }

    msg = json.dumps(gh_event)
    print("v:", msg)
                    
    # producer.put("^")
    producer.put(msg)

    sleep(0.1)

