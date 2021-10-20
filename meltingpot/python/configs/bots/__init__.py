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
"""Library of stored bots for MeltingPot scenarios."""

import re
from typing import Mapping, Optional

import dataclasses
import immutabledict

from meltingpot.python.utils.bots import puppeteer_functions


@dataclasses.dataclass(frozen=True)
class Bot:
    substrate: str
    puppeteer_fn: Optional[puppeteer_functions.PuppeteerFn]
    model: str


_saved_model = lambda **kwargs: Bot(puppeteer_fn=None, **kwargs)
_puppet = lambda **kwargs: Bot(model="puppet", **kwargs)

BOTS: Mapping[str, Bot] = immutabledict.immutabledict(
    # keep-sorted start numeric=yes block=yes
    ah3gs_bot_finding_berry_two_the_most_tasty_0=_saved_model(
        substrate="allelopathic_harvest",
        model="ah3gs_bot_finding_berry_two_the_most_tasty_0",
    ),
    ah3gs_bot_finding_berry_two_the_most_tasty_1=_saved_model(
        substrate="allelopathic_harvest",
        model="ah3gs_bot_finding_berry_two_the_most_tasty_1",
    ),
    ah3gs_bot_finding_berry_two_the_most_tasty_4=_saved_model(
        substrate="allelopathic_harvest",
        model="ah3gs_bot_finding_berry_two_the_most_tasty_4",
    ),
    ah3gs_bot_finding_berry_two_the_most_tasty_5=_saved_model(
        substrate="allelopathic_harvest",
        model="ah3gs_bot_finding_berry_two_the_most_tasty_5",
    ),
    arena_rws_free_0=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix", model="arena_rws_free_0",
    ),
    arena_rws_free_1=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix", model="arena_rws_free_1",
    ),
    arena_rws_free_2=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix", model="arena_rws_free_2",
    ),
    arena_rws_pure_paper_0=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_paper_0",
    ),
    arena_rws_pure_paper_1=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_paper_1",
    ),
    arena_rws_pure_paper_2=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_paper_2",
    ),
    arena_rws_pure_paper_3=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_paper_3",
    ),
    arena_rws_pure_rock_0=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_rock_0",
    ),
    arena_rws_pure_rock_1=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_rock_1",
    ),
    arena_rws_pure_rock_2=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_rock_2",
    ),
    arena_rws_pure_rock_3=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_rock_3",
    ),
    arena_rws_pure_scissors_0=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_scissors_0",
    ),
    arena_rws_pure_scissors_1=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_scissors_1",
    ),
    arena_rws_pure_scissors_2=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_scissors_2",
    ),
    arena_rws_pure_scissors_3=_saved_model(
        substrate="arena_running_with_scissors_in_the_matrix",
        model="arena_rws_pure_scissors_3",
    ),
    bach_fan_0=_saved_model(
        substrate="bach_or_stravinsky_in_the_matrix", model="bach_fan_0",
    ),
    bach_fan_1=_saved_model(
        substrate="bach_or_stravinsky_in_the_matrix", model="bach_fan_1",
    ),
    bach_fan_2=_saved_model(
        substrate="bach_or_stravinsky_in_the_matrix", model="bach_fan_2",
    ),
    chemistry_branched_chain_reaction_X_specialist_0=_saved_model(
        substrate="chemistry_branched_chain_reaction",
        model="chemistry_branched_chain_reaction_X_specialist_0",
    ),
    chemistry_branched_chain_reaction_X_specialist_1=_saved_model(
        substrate="chemistry_branched_chain_reaction",
        model="chemistry_branched_chain_reaction_X_specialist_1",
    ),
    chemistry_branched_chain_reaction_X_specialist_2=_saved_model(
        substrate="chemistry_branched_chain_reaction",
        model="chemistry_branched_chain_reaction_X_specialist_2",
    ),
    chemistry_branched_chain_reaction_Y_specialist_0=_saved_model(
        substrate="chemistry_branched_chain_reaction",
        model="chemistry_branched_chain_reaction_Y_specialist_0",
    ),
    chemistry_branched_chain_reaction_Y_specialist_1=_saved_model(
        substrate="chemistry_branched_chain_reaction",
        model="chemistry_branched_chain_reaction_Y_specialist_1",
    ),
    chemistry_branched_chain_reaction_Y_specialist_2=_saved_model(
        substrate="chemistry_branched_chain_reaction",
        model="chemistry_branched_chain_reaction_Y_specialist_2",
    ),
    chemistry_metabolic_cycles_food1_specialist_0=_saved_model(
        substrate="chemistry_metabolic_cycles",
        model="chemistry_metabolic_cycles_food1_specialist_0",
    ),
    chemistry_metabolic_cycles_food1_specialist_1=_saved_model(
        substrate="chemistry_metabolic_cycles",
        model="chemistry_metabolic_cycles_food1_specialist_1",
    ),
    chemistry_metabolic_cycles_food2_specialist_0=_saved_model(
        substrate="chemistry_metabolic_cycles",
        model="chemistry_metabolic_cycles_food2_specialist_0",
    ),
    chemistry_metabolic_cycles_food2_specialist_1=_saved_model(
        substrate="chemistry_metabolic_cycles",
        model="chemistry_metabolic_cycles_food2_specialist_1",
    ),
    chicken_free_0=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_free_0",
    ),
    chicken_free_1=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_free_1",
    ),
    chicken_free_2=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_free_2",
    ),
    chicken_free_3=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_free_3",
    ),
    chicken_puppet_grim=_puppet(
        substrate="chicken_in_the_matrix",
        puppeteer_fn=puppeteer_functions.GrimTwoResourceInTheMatrix(2),
    ),
    chicken_pure_dove_0=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_pure_dove_0",
    ),
    chicken_pure_dove_1=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_pure_dove_1",
    ),
    chicken_pure_dove_2=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_pure_dove_2",
    ),
    chicken_pure_dove_3=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_pure_dove_3",
    ),
    chicken_pure_hawk_0=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_pure_hawk_0",
    ),
    chicken_pure_hawk_1=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_pure_hawk_1",
    ),
    chicken_pure_hawk_2=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_pure_hawk_2",
    ),
    chicken_pure_hawk_3=_saved_model(
        substrate="chicken_in_the_matrix", model="chicken_pure_hawk_3",
    ),
    classic_rws_free_0=_saved_model(
        substrate="running_with_scissors_in_the_matrix", model="classic_rws_free_0",
    ),
    classic_rws_free_1=_saved_model(
        substrate="running_with_scissors_in_the_matrix", model="classic_rws_free_1",
    ),
    classic_rws_free_2=_saved_model(
        substrate="running_with_scissors_in_the_matrix", model="classic_rws_free_2",
    ),
    classic_rws_pure_paper_0=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_paper_0",
    ),
    classic_rws_pure_paper_1=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_paper_1",
    ),
    classic_rws_pure_paper_2=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_paper_2",
    ),
    classic_rws_pure_paper_3=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_paper_3",
    ),
    classic_rws_pure_rock_0=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_rock_0",
    ),
    classic_rws_pure_rock_1=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_rock_1",
    ),
    classic_rws_pure_rock_2=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_rock_2",
    ),
    classic_rws_pure_rock_3=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_rock_3",
    ),
    classic_rws_pure_scissors_0=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_scissors_0",
    ),
    classic_rws_pure_scissors_1=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_scissors_1",
    ),
    classic_rws_pure_scissors_2=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_scissors_2",
    ),
    classic_rws_pure_scissors_3=_saved_model(
        substrate="running_with_scissors_in_the_matrix",
        model="classic_rws_pure_scissors_3",
    ),
    cleanup_cleaner_1=_saved_model(substrate="clean_up", model="cleanup_cleaner_1",),
    cleanup_cleaner_2=_saved_model(substrate="clean_up", model="cleanup_cleaner_2",),
    cleanup_consumer_0=_saved_model(substrate="clean_up", model="cleanup_consumer_0",),
    cleanup_consumer_1=_saved_model(substrate="clean_up", model="cleanup_consumer_1",),
    cleanup_consumer_2=_saved_model(substrate="clean_up", model="cleanup_consumer_2",),
    cleanup_puppet_alternate_clean_first=_puppet(
        substrate="clean_up",
        puppeteer_fn=puppeteer_functions.cleanup_alternate_clean_first,
    ),
    cleanup_puppet_alternate_eat_first=_puppet(
        substrate="clean_up",
        puppeteer_fn=puppeteer_functions.cleanup_alternate_eat_first,
    ),
    cleanup_puppet_reciprocator_threshold_low=_puppet(
        substrate="clean_up", puppeteer_fn=puppeteer_functions.ConditionalCleaner(1),
    ),
    cleanup_puppet_reciprocator_threshold_mid=_puppet(
        substrate="clean_up", puppeteer_fn=puppeteer_functions.ConditionalCleaner(2),
    ),
    closed_commons_zapper_0=_saved_model(
        substrate="commons_harvest_closed", model="closed_commons_zapper_0",
    ),
    closed_commons_zapper_1=_saved_model(
        substrate="commons_harvest_closed", model="closed_commons_zapper_1",
    ),
    closed_commons_zapper_2=_saved_model(
        substrate="commons_harvest_closed", model="closed_commons_zapper_2",
    ),
    closed_commons_zapper_3=_saved_model(
        substrate="commons_harvest_closed", model="closed_commons_zapper_3",
    ),
    collaborative_cooking_impassable_vmpo_pop_size_ten_0=_saved_model(
        substrate="collaborative_cooking_impassable",
        model="collaborative_cooking_impassable_vmpo_pop_size_ten_0",
    ),
    collaborative_cooking_impassable_vmpo_pop_size_ten_2=_saved_model(
        substrate="collaborative_cooking_impassable",
        model="collaborative_cooking_impassable_vmpo_pop_size_ten_2",
    ),
    collaborative_cooking_impassable_vmpo_pop_size_ten_3=_saved_model(
        substrate="collaborative_cooking_impassable",
        model="collaborative_cooking_impassable_vmpo_pop_size_ten_3",
    ),
    collaborative_cooking_impassable_vmpo_pop_size_ten_4=_saved_model(
        substrate="collaborative_cooking_impassable",
        model="collaborative_cooking_impassable_vmpo_pop_size_ten_4",
    ),
    collaborative_cooking_impassable_vmpo_pop_size_ten_6=_saved_model(
        substrate="collaborative_cooking_impassable",
        model="collaborative_cooking_impassable_vmpo_pop_size_ten_6",
    ),
    collaborative_cooking_impassable_vmpo_pop_size_ten_7=_saved_model(
        substrate="collaborative_cooking_impassable",
        model="collaborative_cooking_impassable_vmpo_pop_size_ten_7",
    ),
    collaborative_cooking_impassable_vmpo_pop_size_ten_9=_saved_model(
        substrate="collaborative_cooking_impassable",
        model="collaborative_cooking_impassable_vmpo_pop_size_ten_9",
    ),
    collaborative_cooking_passable_vmpo_pop_size_ten_5=_saved_model(
        substrate="collaborative_cooking_passable",
        model="collaborative_cooking_passable_vmpo_pop_size_ten_5",
    ),
    ctf_pseudorewards_for_main_game_events_a3c_2=_saved_model(
        substrate="capture_the_flag",
        model="ctf_pseudorewards_for_main_game_events_a3c_2",
    ),
    ctf_pseudorewards_for_main_game_events_a3c_6=_saved_model(
        substrate="capture_the_flag",
        model="ctf_pseudorewards_for_main_game_events_a3c_6",
    ),
    ctf_pseudorewards_for_main_game_events_vmpo_0=_saved_model(
        substrate="capture_the_flag",
        model="ctf_pseudorewards_for_main_game_events_vmpo_0",
    ),
    ctf_pseudorewards_for_main_game_events_vmpo_3=_saved_model(
        substrate="capture_the_flag",
        model="ctf_pseudorewards_for_main_game_events_vmpo_3",
    ),
    ctf_pseudorewards_for_main_game_events_vmpo_4=_saved_model(
        substrate="capture_the_flag",
        model="ctf_pseudorewards_for_main_game_events_vmpo_4",
    ),
    ctf_pseudorewards_for_main_game_events_vmpo_6=_saved_model(
        substrate="capture_the_flag",
        model="ctf_pseudorewards_for_main_game_events_vmpo_6",
    ),
    ctf_pseudorewards_for_main_game_events_vmpo_7=_saved_model(
        substrate="capture_the_flag",
        model="ctf_pseudorewards_for_main_game_events_vmpo_7",
    ),
    koth_default_vmpo_0=_saved_model(
        substrate="king_of_the_hill", model="koth_default_vmpo_0",
    ),
    koth_default_vmpo_1=_saved_model(
        substrate="king_of_the_hill", model="koth_default_vmpo_1",
    ),
    koth_default_vmpo_2=_saved_model(
        substrate="king_of_the_hill", model="koth_default_vmpo_2",
    ),
    koth_default_vmpo_3=_saved_model(
        substrate="king_of_the_hill", model="koth_default_vmpo_3",
    ),
    koth_default_vmpo_4=_saved_model(
        substrate="king_of_the_hill", model="koth_default_vmpo_4",
    ),
    koth_default_vmpo_5=_saved_model(
        substrate="king_of_the_hill", model="koth_default_vmpo_5",
    ),
    koth_default_vmpo_6=_saved_model(
        substrate="king_of_the_hill", model="koth_default_vmpo_6",
    ),
    koth_default_vmpo_7=_saved_model(
        substrate="king_of_the_hill", model="koth_default_vmpo_7",
    ),
    koth_zap_while_in_control_a3c_0=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_a3c_0",
    ),
    koth_zap_while_in_control_a3c_1=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_a3c_1",
    ),
    koth_zap_while_in_control_a3c_2=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_a3c_2",
    ),
    koth_zap_while_in_control_a3c_3=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_a3c_3",
    ),
    koth_zap_while_in_control_a3c_4=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_a3c_4",
    ),
    koth_zap_while_in_control_a3c_5=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_a3c_5",
    ),
    koth_zap_while_in_control_a3c_6=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_a3c_6",
    ),
    koth_zap_while_in_control_a3c_7=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_a3c_7",
    ),
    koth_zap_while_in_control_vmpo_0=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_vmpo_0",
    ),
    koth_zap_while_in_control_vmpo_1=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_vmpo_1",
    ),
    koth_zap_while_in_control_vmpo_2=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_vmpo_2",
    ),
    koth_zap_while_in_control_vmpo_3=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_vmpo_3",
    ),
    koth_zap_while_in_control_vmpo_4=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_vmpo_4",
    ),
    koth_zap_while_in_control_vmpo_5=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_vmpo_5",
    ),
    koth_zap_while_in_control_vmpo_6=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_vmpo_6",
    ),
    koth_zap_while_in_control_vmpo_7=_saved_model(
        substrate="king_of_the_hill", model="koth_zap_while_in_control_vmpo_7",
    ),
    open_commons_zapper_0=_saved_model(
        substrate="commons_harvest_open", model="open_commons_zapper_0",
    ),
    open_commons_zapper_1=_saved_model(
        substrate="commons_harvest_open", model="open_commons_zapper_1",
    ),
    partnership_commons_putative_good_partner_4=_saved_model(
        substrate="commons_harvest_partnership",
        model="partnership_commons_putative_good_partner_4",
    ),
    partnership_commons_putative_good_partner_5=_saved_model(
        substrate="commons_harvest_partnership",
        model="partnership_commons_putative_good_partner_5",
    ),
    partnership_commons_putative_good_partner_7=_saved_model(
        substrate="commons_harvest_partnership",
        model="partnership_commons_putative_good_partner_7",
    ),
    partnership_commons_zapper_1=_saved_model(
        substrate="commons_harvest_partnership", model="partnership_commons_zapper_1",
    ),
    partnership_commons_zapper_2=_saved_model(
        substrate="commons_harvest_partnership", model="partnership_commons_zapper_2",
    ),
    prisoners_dilemma_cooperator_2=_saved_model(
        substrate="prisoners_dilemma_in_the_matrix",
        model="prisoners_dilemma_cooperator_2",
    ),
    prisoners_dilemma_cooperator_4=_saved_model(
        substrate="prisoners_dilemma_in_the_matrix",
        model="prisoners_dilemma_cooperator_4",
    ),
    prisoners_dilemma_defector_0=_saved_model(
        substrate="prisoners_dilemma_in_the_matrix",
        model="prisoners_dilemma_defector_0",
    ),
    prisoners_dilemma_defector_2=_saved_model(
        substrate="prisoners_dilemma_in_the_matrix",
        model="prisoners_dilemma_defector_2",
    ),
    prisoners_dilemma_free_0=_saved_model(
        substrate="prisoners_dilemma_in_the_matrix", model="prisoners_dilemma_free_0",
    ),
    prisoners_dilemma_free_1=_saved_model(
        substrate="prisoners_dilemma_in_the_matrix", model="prisoners_dilemma_free_1",
    ),
    prisoners_dilemma_free_2=_saved_model(
        substrate="prisoners_dilemma_in_the_matrix", model="prisoners_dilemma_free_2",
    ),
    prisoners_dilemma_puppet_grim_threshold_high=_puppet(
        substrate="prisoners_dilemma_in_the_matrix",
        puppeteer_fn=puppeteer_functions.GrimTwoResourceInTheMatrix(2),
    ),
    prisoners_dilemma_puppet_grim_threshold_low=_puppet(
        substrate="prisoners_dilemma_in_the_matrix",
        puppeteer_fn=puppeteer_functions.GrimTwoResourceInTheMatrix(1),
    ),
    pure_coordination_type_1_specialist_0=_saved_model(
        substrate="pure_coordination_in_the_matrix",
        model="pure_coordination_type_1_specialist_0",
    ),
    pure_coordination_type_1_specialist_1=_saved_model(
        substrate="pure_coordination_in_the_matrix",
        model="pure_coordination_type_1_specialist_1",
    ),
    pure_coordination_type_2_specialist_0=_saved_model(
        substrate="pure_coordination_in_the_matrix",
        model="pure_coordination_type_2_specialist_0",
    ),
    pure_coordination_type_2_specialist_1=_saved_model(
        substrate="pure_coordination_in_the_matrix",
        model="pure_coordination_type_2_specialist_1",
    ),
    pure_coordination_type_3_specialist_0=_saved_model(
        substrate="pure_coordination_in_the_matrix",
        model="pure_coordination_type_3_specialist_0",
    ),
    pure_coordination_type_3_specialist_1=_saved_model(
        substrate="pure_coordination_in_the_matrix",
        model="pure_coordination_type_3_specialist_1",
    ),
    rationalizable_coordination_type_1_specialist_0=_saved_model(
        substrate="rationalizable_coordination_in_the_matrix",
        model="rationalizable_coordination_type_1_specialist_0",
    ),
    rationalizable_coordination_type_1_specialist_1=_saved_model(
        substrate="rationalizable_coordination_in_the_matrix",
        model="rationalizable_coordination_type_1_specialist_1",
    ),
    rationalizable_coordination_type_2_specialist_0=_saved_model(
        substrate="rationalizable_coordination_in_the_matrix",
        model="rationalizable_coordination_type_2_specialist_0",
    ),
    rationalizable_coordination_type_2_specialist_1=_saved_model(
        substrate="rationalizable_coordination_in_the_matrix",
        model="rationalizable_coordination_type_2_specialist_1",
    ),
    rationalizable_coordination_type_3_specialist_0=_saved_model(
        substrate="rationalizable_coordination_in_the_matrix",
        model="rationalizable_coordination_type_3_specialist_0",
    ),
    rationalizable_coordination_type_3_specialist_1=_saved_model(
        substrate="rationalizable_coordination_in_the_matrix",
        model="rationalizable_coordination_type_3_specialist_1",
    ),
    stag_hunt_hare_specialist_0=_saved_model(
        substrate="stag_hunt_in_the_matrix", model="stag_hunt_hare_specialist_0",
    ),
    stag_hunt_hare_specialist_1=_saved_model(
        substrate="stag_hunt_in_the_matrix", model="stag_hunt_hare_specialist_1",
    ),
    stag_hunt_hare_specialist_2=_saved_model(
        substrate="stag_hunt_in_the_matrix", model="stag_hunt_hare_specialist_2",
    ),
    stag_hunt_puppet_grim=_puppet(
        substrate="stag_hunt_in_the_matrix",
        puppeteer_fn=puppeteer_functions.GrimTwoResourceInTheMatrix(1),
    ),
    stag_hunt_stag_specialist_3=_saved_model(
        substrate="stag_hunt_in_the_matrix", model="stag_hunt_stag_specialist_3",
    ),
    stag_hunt_stag_specialist_5=_saved_model(
        substrate="stag_hunt_in_the_matrix", model="stag_hunt_stag_specialist_5",
    ),
    stravinsky_fan_0=_saved_model(
        substrate="bach_or_stravinsky_in_the_matrix", model="stravinsky_fan_0",
    ),
    stravinsky_fan_1=_saved_model(
        substrate="bach_or_stravinsky_in_the_matrix", model="stravinsky_fan_1",
    ),
    stravinsky_fan_2=_saved_model(
        substrate="bach_or_stravinsky_in_the_matrix", model="stravinsky_fan_2",
    ),
    territory_closed_reply_to_zapper_0=_saved_model(
        substrate="territory_rooms", model="territory_closed_reply_to_zapper_0",
    ),
    territory_closed_reply_to_zapper_1=_saved_model(
        substrate="territory_rooms", model="territory_closed_reply_to_zapper_1",
    ),
    territory_open_painter_0=_saved_model(
        substrate="territory_open", model="territory_open_painter_0",
    ),
    territory_open_painter_1=_saved_model(
        substrate="territory_open", model="territory_open_painter_1",
    ),
    territory_open_painter_2=_saved_model(
        substrate="territory_open", model="territory_open_painter_2",
    ),
    territory_open_painter_3=_saved_model(
        substrate="territory_open", model="territory_open_painter_3",
    ),
    # keep-sorted end
)
