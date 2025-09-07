import gymnasium as gym
import numpy as np

env = gym.make("FrozenLake-v1", is_slippery=True)

num_episodes = 1000
rewards_per_episode = []

for episode in range(num_episodes):
    observation, info = env.reset()
    terminated, truncated = False, False
    episode_reward = 0

    while not terminated and not truncated:
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        episode_reward += reward

    rewards_per_episode.append(episode_reward)

average_reward = sum(rewards_per_episode) / num_episodes
print(f"Average reward over {num_episodes} episodes: {average_reward:.4f}")
