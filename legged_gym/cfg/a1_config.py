# SPDX-FileCopyrightText: Copyright (c) 2021 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2021 ETH Zurich, Nikita Rudin

from legged_gym.cfg.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO
import glob
MOTION_FILES = glob.glob('datasets/model_base_motions/*')

class A1RoughCfg( LeggedRobotCfg ):

    class env( LeggedRobotCfg.env ):
        # num_envs = 5480
        # include_history_steps = None  # Number of steps of history to include.
        # num_observations = 235
        # num_privileged_obs = 235
        # reference_state_initialization = False
        # # reference_state_initialization_prob = 0.85
        # # amp_motion_files = MOTION_FILES

        num_envs = 4096
        include_history_steps = None  # Number of steps of history to include.
        num_observations = 235
        num_privileged_obs = 235
        reference_state_initialization = False
        # reference_state_initialization_prob = 0.85
        amp_motion_files = MOTION_FILES


    class init_state( LeggedRobotCfg.init_state ):
        # pos = [0.0, 0.0, 0.42] # x,y,z [m]
        # default_joint_angles = { # = target angles [rad] when action = 0.0
        #     'FL_hip_joint': 0.1,   # [rad]
        #     'RL_hip_joint': 0.1,   # [rad]
        #     'FR_hip_joint': -0.1 ,  # [rad]
        #     'RR_hip_joint': -0.1,   # [rad]

        #     'FL_thigh_joint': 0.8,     # [rad]
        #     'RL_thigh_joint': 1.,   # [rad]
        #     'FR_thigh_joint': 0.8,     # [rad]
        #     'RR_thigh_joint': 1.,   # [rad]

        #     'FL_calf_joint': -1.5,   # [rad]
        #     'RL_calf_joint': -1.5,    # [rad]
        #     'FR_calf_joint': -1.5,  # [rad]
        #     'RR_calf_joint': -1.5,    # [rad]
        # }

        pos = [0.0, 0.0, 0.42] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            'FL_hip_joint': -0.20,   # [rad]
            'RL_hip_joint': -0.20,   # [rad]
            'FR_hip_joint':  0.20,  # [rad]
            'RR_hip_joint':  0.20,   # [rad]

            'FL_thigh_joint': 0.72,     # [rad]
            'RL_thigh_joint': 0.72,   # [rad]
            'FR_thigh_joint': 0.72,     # [rad]
            'RR_thigh_joint': 0.72,   # [rad]

            'FL_calf_joint': -1.44,   # [rad]
            'RL_calf_joint': -1.44,    # [rad]
            'FR_calf_joint': -1.44,  # [rad]
            'RR_calf_joint': -1.44,    # [rad]
        }

    class control( LeggedRobotCfg.control ):
        # # PD Drive parameters:
        # control_type = 'P'
        # stiffness = {'joint': 20.}  # [N*m/rad]
        # damping = {'joint': 0.5}     # [N*m*s/rad]
        # # action scale: target angle = actionScale * action + defaultAngle
        # action_scale = 0.25
        # # decimation: Number of control action updates @ sim DT per policy DT
        # decimation = 4

        # PD Drive parameters:
        control_type = 'P'
        stiffness = {'joint': 20.}  # [N*m/rad]
        damping = {'joint': 1.0}     # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/a1/urdf/a1.urdf'
        foot_name = "foot"
        penalize_contacts_on = ["thigh", "calf"]
        terminate_after_contacts_on = ["base"]
        self_collisions = 1 # 1 to disable, 0 to enable...bitwise filter
    
    # class domain_rand:
    #     randomize_friction = True
    #     friction_range = [0.25, 1.75]
    #     randomize_base_mass = True
    #     added_mass_range = [-1., 1.]
    #     push_robots = True
    #     push_interval_s = 15
    #     max_push_vel_xy = 1.0
    #     randomize_gains = True
    #     stiffness_multiplier_range = [0.9, 1.1]
    #     damping_multiplier_range = [0.9, 1.1]

    # class noise:
    #     add_noise = True
    #     noise_level = 1.0 # scales other values
    #     class noise_scales:
    #         dof_pos = 0.03
    #         dof_vel = 1.5
    #         lin_vel = 0.1
    #         ang_vel = 0.3
    #         gravity = 0.05
    #         height_measurements = 0.1




    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.25
        class scales( LeggedRobotCfg.rewards.scales ):
            torques = -0.0002
            dof_pos_limits = -10.0

    class commands:
        curriculum = False
        max_curriculum = 1.
        num_commands = 4 # default: lin_vel_x, lin_vel_y, ang_vel_yaw, heading (in heading mode ang_vel_yaw is recomputed from heading error)
        resampling_time = 10. # time before command are changed[s]
        heading_command = False # if true: compute ang vel command from heading error
        class ranges:
            lin_vel_x = [-1.0, 2.0] # min max [m/s]
            lin_vel_y = [-0.3, 0.3]   # min max [m/s]
            ang_vel_yaw = [-1.57, 1.57]    # min max [rad/s]
            heading = [-3.14, 3.14]


class A1RoughCfgPPO( LeggedRobotCfgPPO ):

    # class policy( LeggedRobotCfgPPO.policy ):
    #     actor_hidden_dims = [256, 128, 64]

    class algorithm( LeggedRobotCfgPPO.algorithm ):
        entropy_coef = 0.01

    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'rough_a1'

  