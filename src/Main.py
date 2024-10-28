"""
Filename: main.py
Author: David Zheng
Copyright: © 2024 David Zheng. All rights reserved.
Contact: dqzheng1996@gmail.com
Description: Main training script for the filter design project using DQN, instantiating the environment, callbacks, and plotting results.
"""
from stable_baselines3 import DQN
from src.env import FilterDesignEnv
from src.callback import RewardAndResponseLoggingCallback

# Instantiate environment and callback
env = FilterDesignEnv(target_cutoff=10000)
reward_callback = RewardAndResponseLoggingCallback()

# Train the agent
model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000, callback=reward_callback)

# Plot results
reward_callback.plot_all_responses()
reward_callback.plot_final_reward_vs_episodes()
