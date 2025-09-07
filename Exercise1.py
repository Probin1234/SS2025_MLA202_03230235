import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode="human")

print("Action Space:", env.action_space)        # Discrete(2)
print("Observation Space:", env.observation_space)  # Box(4,)


state, info = env.reset()
done = False
reward_total = 0


while not done:
    action = env.action_space.sample()   
    state, reward, terminated, truncated, info = env.step(action)
    reward_total += reward

    if terminated or truncated:
        done = True

    time.sleep(0.05)   

print("Total reward for this random episode:", reward_total)

env.close()
