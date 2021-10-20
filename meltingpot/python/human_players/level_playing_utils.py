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
"""A simple human player for testing a Melting Pot level.

Use `WASD` keys to move the character around.
Use `Q and E` to turn the character.
Use `SPACE` to fire the zapper.
Use `TAB` to switch between players.
"""

import collections
import enum

from typing import Any, Callable, Dict, Mapping, Optional, Sequence, Tuple
import dm_env

from ml_collections import config_dict
import numpy as np
import pygame

import dmlab2d
from meltingpot.python.utils.substrates import builder

WHITE = (255, 255, 255)

MOVEMENT_MAP = {
    "NONE": 0,
    "FORWARD": 1,
    "RIGHT": 2,
    "BACKWARD": 3,
    "LEFT": 4,
}


EnvBuilder = Callable[..., dmlab2d.Environment]  # Only supporting kwargs.

ActionMap = Mapping[str, Callable[[], int]]


class RenderType(enum.Enum):
    NONE = 0
    PYGAME = 1


def get_random_direction() -> int:
    """Gets a random direction."""
    return np.random.choice(list(MOVEMENT_MAP.values()))


def get_random_turn() -> int:
    """Gets a random turn."""
    return np.random.choice([-1, 0, 1])


def get_random_fire() -> int:
    """Gets a random fire."""
    return np.random.choice([0, 1])


def get_direction_pressed() -> int:
    """Gets direction pressed."""
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
        return MOVEMENT_MAP["FORWARD"]
    if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
        return MOVEMENT_MAP["RIGHT"]
    if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
        return MOVEMENT_MAP["BACKWARD"]
    if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
        return MOVEMENT_MAP["LEFT"]
    return MOVEMENT_MAP["NONE"]


def get_turn_pressed() -> int:
    """Calculates turn increment."""
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_DELETE] or key_pressed[pygame.K_q]:
        return -1
    if key_pressed[pygame.K_PAGEDOWN] or key_pressed[pygame.K_e]:
        return 1
    return 0


def get_space_key_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_SPACE] else 0


def get_key_number_pressed() -> int:
    number_keys = [
        pygame.K_0,
        pygame.K_1,
        pygame.K_2,
        pygame.K_3,
        pygame.K_4,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
        pygame.K_8,
        pygame.K_9,
    ]
    for num in range(len(number_keys)):
        if pygame.key.get_pressed()[number_keys[num]]:
            return num
    return -1


def get_key_number_one_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_1] else 0


def get_key_number_two_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_2] else 0


def get_key_number_three_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_3] else 0


def get_key_number_four_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_4] else 0


def get_key_number_five_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_5] else 0


def get_left_control_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_LCTRL] else 0


def get_left_shift_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_LSHIFT] else 0


def get_right_shift_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_RSHIFT] else 0


def get_key_z_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_z] else 0


def get_key_x_pressed() -> int:
    return 1 if pygame.key.get_pressed()[pygame.K_x] else 0


def _split_key(key: str) -> Tuple[int, str]:
    """Splits the key into player index and name."""
    tokens = key.split(".")
    return int(tokens[0]), ".".join(tokens[1:])


def _get_rewards(timestep: dm_env.TimeStep) -> Sequence[float]:
    """Gets the list of rewards, one for each player."""
    rewards = {}
    for key in timestep.observation.keys():
        if key.endswith(".REWARD"):
            lua_index, name = _split_key(key)
            if name == "REWARD":
                rewards[lua_index] = timestep.observation[key]
    reward_list = [0.0] * len(rewards)
    for lua_index, reward in rewards.items():
        reward_list[lua_index - 1] = reward
    return reward_list


class ActionReader(object):
    """Convert keyboard actions to environment actions."""

    def __init__(self, env: dmlab2d.Environment, action_map: ActionMap):
        # Actions are named "<lua_player_index>.<action_name>"
        self._action_map = action_map
        self._action_spec = env.action_spec()
        assert isinstance(self._action_spec, dict)
        self._action_names = set()
        for action_key in self._action_spec.keys():
            _, action_name = _split_key(action_key)
            self._action_names.add(action_name)

    def step(self, player_index: int) -> Sequence[Sequence[Mapping[str, int]]]:
        """Update the actions of player `player_index`."""
        actions = {action_key: 0 for action_key in self._action_spec.keys()}
        for action_name in self._action_names:
            actions[f"{player_index + 1}.{action_name}"] = self._action_map[
                action_name
            ]()
        return actions


def run_episode(
    render_observation: str,
    config_overrides: Dict[str, Any],
    action_map: ActionMap,
    full_config: config_dict.ConfigDict,
    interactive: RenderType = RenderType.PYGAME,
    screen_width: int = 800,
    screen_height: int = 600,
    fps: int = 8,
    verbose_fn: Optional[Callable[[dm_env.TimeStep, int], None]] = None,
    text_display_fn: Optional[Callable[[dm_env.TimeStep, int], str]] = None,
    text_font_size: int = 36,
    text_x_pos: int = 20,
    text_y_pos: int = 20,
    text_color: Tuple[int, ...] = WHITE,
    env_builder: EnvBuilder = builder.builder,
    print_events: Optional[bool] = False,
) -> None:
    """Run multiplayer environment, with per player rendering and actions.

  This function initialises a Melting Pot environment with the given
  configuration (including possible config overrides), and optionally launches
  the episode as an interactive game using pygame.  The controls are described
  in the action_map, whose keys correspond to discrete actions of the
  environment.

  Args:
    render_observation: A string consisting of the observation name to render.
        Usually 'RGB' for the third person world view.
    config_overrides: A dictionary of settings to override from the original
        `full_config.lab2d_settings`. Typically these are used to set the number
        of players.
    action_map: A dictionary of (discrete) action names to functions that detect
        the keys that correspond to its possible action values.  For example,
        for movement, we might want to have WASD navigation tied to the 'move'
        action name using `get_direction_pressed`.  See examples in the various
        play_*.py scripts.
    full_config: The full configuration for the Melting Pot environment.  These
        usually come from meltingpot/python/configs/environments.
    interactive: A RenderType representing whether the episode should be run
        with PyGame, or without any interface.  Setting interactive to false
        enables running e.g. a random agent via the action_map returning actions
        without polling PyGame (or any human input).  Non interactive runs
        ignore the screen_width, screen_height and fps parameters.
    screen_width: Width, in pixels, of the window to render the game.
    screen_height: Height, in pixels, of the window to render the game.
    fps: Frames per second of the game.
    verbose_fn: An optional function that will be executed for every step of
        the environment.  It receives the environment and the player index. This
        is typically used to print extra information that would be useful for
        debugging a running episode.
    text_display_fn: An optional function for displaying text on screen. It
        receives the environment and the player index, and returns a string to
        display on the pygame screen.
    text_font_size: the font size of onscreen text (from `text_display_fn`)
    text_x_pos: the x position of onscreen text (from `text_display_fn`)
    text_y_pos: the x position of onscreen text (from `text_display_fn`)
    text_color: RGB color of onscreen text (from `text_display_fn`)
    env_builder: The environment builder function to use. By default it is
      meltingpot.builder.
    print_events: An optional bool that if enabled will print events captured
      from the dmlab2d events API on any timestep where they occur.
  """
    full_config.lab2d_settings.update(config_overrides)
    player_count = full_config.lab2d_settings.get("numPlayers", 1)
    print(f"Running an episode with {player_count} players.")
    env = env_builder(**full_config)

    player_index = 0
    timestep = env.reset()

    score = collections.defaultdict(float)
    action_reader = ActionReader(env, action_map)

    if interactive == RenderType.PYGAME:
        pygame.init()
        pygame.display.set_caption(
            "Melting Pot: {}".format(full_config.lab2d_settings.levelName)
        )
        font = pygame.font.SysFont(None, text_font_size)

    scale = 1
    observation_spec = env.observation_spec()
    if render_observation in observation_spec:
        obs_spec = observation_spec[render_observation]
    elif f"1.{render_observation}" in observation_spec:
        # This assumes all players have the same observation, which is true for
        # MeltingPot environments.
        obs_spec = observation_spec[f"1.{render_observation}"]

    observation_shape = obs_spec.shape
    observation_height = observation_shape[0]
    observation_width = observation_shape[1]
    scale = min(screen_height // observation_height, screen_width // observation_width)
    if interactive == RenderType.PYGAME:
        game_display = pygame.display.set_mode(
            (observation_width * scale, observation_height * scale)
        )
        clock = pygame.time.Clock()
    stop = False

    # Game loop
    while True:

        # Check for pygame controls
        if interactive == RenderType.PYGAME:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        player_index = (player_index + 1) % player_count
                    break

        if stop:
            break

        # Compute next timestep
        actions = action_reader.step(player_index) if player_count else []
        timestep = env.step(actions)
        if timestep.step_type == dm_env.StepType.LAST:
            break

        rewards = _get_rewards(timestep)
        for player in range(player_count):
            if verbose_fn:
                verbose_fn(timestep, player)
            score[player] += rewards[player]
            if player == player_index and rewards[player] != 0:
                print(f"{player} Score: {score[player]}")

        # Print events if applicable
        if print_events and hasattr(env, "events"):
            events = env.events()
            # Only print events on timesteps when there are events to print.
            if events:
                print(events)

        # pygame display
        if interactive == RenderType.PYGAME:
            # show visual observation
            if render_observation in timestep.observation:
                obs = timestep.observation[render_observation]
            elif f"{player_index + 1}.{render_observation}" in timestep.observation:
                obs = timestep.observation[f"{player_index + 1}.{render_observation}"]
            obs = np.transpose(obs, (1, 0, 2))  # PyGame is column major!

            surface = pygame.surfarray.make_surface(obs)
            rect = surface.get_rect()

            surf = pygame.transform.scale(surface, (rect[2] * scale, rect[3] * scale))
            game_display.blit(surf, dest=(0, 0))

            # show text
            if text_display_fn:
                if player_count == 1:
                    text_str = text_display_fn(timestep, 0)
                else:
                    text_str = text_display_fn(timestep, player_index)
                img = font.render(text_str, True, text_color)
                game_display.blit(img, (text_x_pos, text_y_pos))

            # tick
            pygame.display.update()
            clock.tick(fps)

    if interactive == RenderType.PYGAME:
        pygame.quit()
    for player in range(player_count):
        print("Player %d: score is %g" % (player, score[player]))
