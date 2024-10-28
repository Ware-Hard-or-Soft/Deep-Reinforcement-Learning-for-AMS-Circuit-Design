"""
Filename: env.py
Author: David Zheng
Copyright: © 2024 David Zheng. All rights reserved.
Contact: dqzheng1996@gmail.com
Description: Environment class (FilterDesignEnv) for designing a low-pass filter using RL.
"""

import numpy as np
from gym import Env, spaces
import subprocess

class FilterDesignEnv(Env):
    def __init__(self, target_cutoff):
        super(FilterDesignEnv, self).__init__()
        self.target_cutoff = target_cutoff
        self.action_space = spaces.Discrete(4)  # Actions to adjust R1, R2, C1, C2
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(4,), dtype=np.float32)
        self.state = np.array([12000, 12000, 1e-9, 1e-9], dtype=np.float32)

    def step(self, action):
        if action == 0:
            self.state[0] += 500
        elif action == 1:
            self.state[1] += 500
        elif action == 2:
            self.state[2] += 5e-11
        elif action == 3:
            self.state[3] += 5e-11

        frequencies, magnitudes = self.run_simulation(self.state)
        reward = reward_function(frequencies, magnitudes, self.target_cutoff)
        done = False
        return self.state, reward, done, {}

    def reset(self):
        self.state = np.array([1200, 1200, 1e-10, 1e-10], dtype=np.float32)
        return self.state

    def run_simulation(self, component_values):
        r1, r2, c1, c2 = component_values
        netlist = f"""
* Low-pass filter circuit with OPAMP
V1 1 0 AC 1
R1 1 2 {r1}
C2 2 0 {c2}
R2 2 3 {r2}
C1 3 0 {c1}
X1 3 0 4 OPAMP
.subckt OPAMP 1 2 3
E1 3 0 1 2 100k
.ends OPAMP
.ac dec 10 1k 100Meg
.print ac vdb(3)
.end
"""
        with open("data/netlists/filter_netlist.sp", "w") as file:
            file.write(netlist)

        command = "ngspice -b data/netlists/filter_netlist.sp -o data/output/output.raw"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print("NgSpice failed:", result.stderr.decode())
            return [], []

        return parse_output("data/output/output.raw")
