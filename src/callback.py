import numpy as np
import matplotlib.pyplot as plt
from stable_baselines3.common.callbacks import BaseCallback

class RewardAndResponseLoggingCallback(BaseCallback):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.episode_rewards = []
        self.all_frequencies = []
        self.all_magnitudes = []
        self.all_cumulative_rewards = []

    def _on_step(self):
        self.episode_rewards.append(self.locals['rewards'][0])
        return True

    def _on_rollout_end(self):
        cumulative_reward = sum(self.episode_rewards)
        self.all_cumulative_rewards.append(cumulative_reward)
        self.episode_rewards = []

        env = self.training_env.envs[0]
        frequencies, magnitudes = env.run_simulation(env.state)
        self.all_frequencies.append(frequencies)
        self.all_magnitudes.append(magnitudes)

        print(f"Episode {len(self.all_cumulative_rewards)} - Cumulative Reward: {cumulative_reward}")

    def plot_final_reward_vs_episodes(self):
        plt.figure(figsize=(10, 6))
        plt.plot(np.arange(len(self.all_cumulative_rewards)), self.all_cumulative_rewards, 'b-', label="Cumulative Reward")
        plt.xlabel("Episode")
        plt.ylabel("Cumulative Reward")
        plt.title("Reward vs. Training Episodes")
        plt.legend()
        plt.grid()
        plt.show()

    def plot_all_responses(self):
        best_episode_index = np.argmax(self.all_cumulative_rewards)
        best_frequencies = self.all_frequencies[best_episode_index]
        best_magnitudes = self.all_magnitudes[best_episode_index]

        plt.figure(figsize=(10, 6))
        for frequencies, magnitudes in zip(self.all_frequencies, self.all_magnitudes):
            plt.plot(frequencies, magnitudes, color="gray", linewidth=0.5, alpha=0.5)
        
        plt.plot(best_frequencies, best_magnitudes, color="blue", linewidth=2, label="Best Frequency Response")
        plt.xscale("log")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude (dB)")
        plt.title("Frequency Responses Across Episodes")
        plt.legend()
        plt.grid(which="both", linestyle="--", linewidth=0.5)
        plt.show()
