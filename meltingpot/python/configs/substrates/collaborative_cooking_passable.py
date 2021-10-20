# Copyright 2020 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Configuration for Collaborative Cooking: Passable.

Example video: https://youtu.be/R_TBitc3hto

Same as _Collaborative Cooking: Impassable_ except here players can pass each
other in the kitchen, allowing less coordinated yet inefficient strategies by
individual players.

See _Collaborative Cooking: Impassable_ for the recipe that players must follow.

This substrate is a pure common interest game. All players share all rewards.

Players have a `5 x 5` observation window.
"""

from meltingpot.python.configs.substrates import collaborative_cooking as base_config


def get_config():
    """Default config for training on collaborative cooking."""
    config = base_config.get_config("passable")
    return config
