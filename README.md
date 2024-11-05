# Project Overview: A reinforcement learning-based AMS design optimizer.

## Installation: Steps for setting up the environment, including requirements.txt.

## Usage: 
* Input the netlist or generate by build in funciton in env.py
* Running the analog simualtion by ngspice
* Setting the reward function based on PPAR metric
* Check the real time result via callback

## Similar resuls/notebooks are provided

* Features and Roadmap: Guide the design of AMS circuits for better PPAR, can be generalized to other AMS circuits by inputting the netlist and reward funciton

## Code Structure: 

* src/                     -- Code files

  1.1 env.py               -- Custom environment class (FilterDesignEnv)
  
  1.2 callback.py          -- Reward logging and response plotting callback
  
  1.3 utils.py             -- Helper functions like `reward_function` and `estimate_cutoff_frequency`
  
  1.4 main.py              -- Main training script to run the DQN agent

* models/                  -- Directory to save trained models

  2.1 checkpoints/         -- Optional: save periodic checkpoints here

* data/                    -- Stores data generated during simulations

  3.1 netlists/            # SPICE netlists generated for each episode

  3.2 output/              # Store output logs from simulations here

* notebooks/               # Jupyter notebooks for experiments and exploratory analysis

* requirements.txt         # Dependencies for the project

* README.md                # Main project documentation

* .gitignore               # Files and directories to ignore in GitHub
