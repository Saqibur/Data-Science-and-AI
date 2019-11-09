import os
import numpy as np
import tensorflow as tf

class DeepQNetwork(object):
    def __init__(self, learning_rate, no_of_actions,
    name_of_network, fcl_dims=256, input_dims=(210, 160, 4),
    chkpt_dir='temp/dqn'):
        super().__init__(*args, **kwargs)