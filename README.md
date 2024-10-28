*Project Overview: A reinforcement learning-based active low-pass filter design optimizer.
*Installation: Steps for setting up the environment, including requirements.txt.
*Usage: 
Input the netlist or generate by build in funciton in env.py
Running the analog simualtion by ngspice
Setting the reward function based on PPAR metric
Check the real time result via callback
*Features and Roadmap: Guide the design of AMS circuits for better PPAR, can be generalized to other AMS circuits by inputting the netlist and reward funciton
*Code Structure: .
├── src/                     # Code files
│   ├── env.py               # Custom environment class (FilterDesignEnv)
│   ├── callback.py          # Reward logging and response plotting callback
│   ├── utils.py             # Helper functions like `reward_function` and `estimate_cutoff_frequency`
│   └── main.py              # Main training script to run the DQN agent
├── models/                  # Directory to save trained models
│   ├── checkpoints/         # Optional: save periodic checkpoints here
├── data/                    # Stores data generated during simulations
│   ├── netlists/            # SPICE netlists generated for each episode
│   └── output/              # Store output logs from simulations here
├── notebooks/               # Jupyter notebooks for experiments and exploratory analysis
├── requirements.txt         # Dependencies for the project
├── README.md                # Main project documentation
└── .gitignore               # Files and directories to ignore in GitHub
